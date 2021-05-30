import discord
import asyncio

from discord.ext import commands


class EntriesPaginator:
    def __init__(self, ctx, **kwargs):
        self.bot = ctx.bot

        self.message = ctx.message
        self.channel = ctx.channel
        self.context = ctx

        self.entries = kwargs.get('entries')
        self.per_page = kwargs.get('per_page', 2)

        self.show_entry_count = kwargs.get('show_entry_count', True)
        self.paginating = True

        self.author = kwargs.get("author", ctx.author)

        self.embed_colour = kwargs.get('colour', discord.Colour.blue())
        self.title = kwargs.get('title', None)
        self.thumbnail = kwargs.get('thumbnail', None)
        self.embed_author = kwargs.get('author', None)
        self.footericon = kwargs.get('footericon', None)
        self.footertext = kwargs.get('footertext', None)

        self.delete_after = kwargs.get('delete_after', 300)

        pages, left_over = divmod(len(self.entries), self.per_page)
        if left_over:
            pages += 1

        self.maximum_pages = pages
        self.embed = discord.Embed(colour=self.embed_colour)
        self.reaction_emojis = [
            ('⏮️', self.first_page),
            ('◀️', self.previous_page),
            ('⏹️', self.stop_pages),
            ('▶️', self.next_page),
            ('⏭️', self.last_page)
        ]

        if ctx.guild is not None:
            self.permissions = self.channel.permissions_for(ctx.guild.me)
        else:
            self.permissions = self.channel.permissions_for(ctx.bot.user)

        if not self.permissions.embed_links:
            raise commands.BotMissingPermissions(['embed_links'])

        if not self.permissions.send_messages:
            raise commands.BotMissingPermissions('Bot cannot send messages.')

        if self.paginating:
            if not self.permissions.add_reactions:
                raise commands.BotMissingPermissions(
                    'I do not have permissions to add reactions.')

            if not self.permissions.read_message_history:
                raise commands.BotMissingPermissions(
                    'I do not have permissions to Read Message History.')

    def get_page(self, page):
        base = (page - 1) * self.per_page
        return self.entries[base:base + self.per_page]

    def get_content(self, entries, page, *, first=False):
        return None

    def get_embed(self, entries, page, *, first=False):
        self.prepare_embed(entries, page, first=first)
        return self.embed

    def prepare_embed(self, entries, page, *, first=False):
        p = []
        for index, entry in enumerate(entries, 1 + ((page - 1) * self.per_page)):
            p.append(f'{entry}')

        if self.maximum_pages > 1 and not self.footertext:
            if self.show_entry_count:
                text = f'Showing page {page}/{self.maximum_pages} ({len(self.entries)} entries)'
            else:
                text = f'Showing page {page}/{self.maximum_pages}'

            self.embed.set_footer(text=text)

        if self.paginating and first:
            p.append('')

        self.embed.description = ''.join(p)
        self.embed.title = self.title or discord.Embed.Empty
        if self.thumbnail:
            self.embed.set_thumbnail(url=self.thumbnail)
        if self.embed_author:
            self.embed.set_author(
                icon_url=self.author.avatar_url, name=self.embed_author)

    async def show_page(self, page, *, first=False):
        self.current_page = page
        entries = self.get_page(page)
        content = self.get_content(entries, page, first=first)
        embed = self.get_embed(entries, page, first=first)

        if not first:
            await self.message.edit(content=content, embed=embed)
            return

        self.message = await self.channel.send(content=content, embed=embed)
        for (reaction, _) in self.reaction_emojis:
            if self.maximum_pages == 2 and reaction in ('◀️', '▶️'):
                continue

            if self.maximum_pages == 1 and reaction in ('◀️', '▶️', '⏮️', '⏭️'):
                continue

            await self.message.add_reaction(reaction)

    async def checked_show_page(self, page):
        if page != 0 and page <= self.maximum_pages:
            await self.show_page(page)

    async def first_page(self):
        """goes to the first page"""
        await self.show_page(1)

    async def last_page(self):
        """goes to the last page"""
        await self.show_page(self.maximum_pages)

    async def next_page(self):
        """goes to the next page"""
        await self.checked_show_page(self.current_page + 1)

    async def previous_page(self):
        """goes to the previous page"""
        await self.checked_show_page(self.current_page - 1)

    async def show_current_page(self):
        if self.paginating:
            await self.show_page(self.current_page)

    async def numbered_page(self):
        """lets you type a page number to go to"""
        to_delete = []
        to_delete.append(await self.channel.send('What page do you want to go to?'))

        def message_check(m):
            return m.author == self.author and \
                self.channel == m.channel and \
                m.content.isdigit()

        try:
            msg = await self.bot.wait_for('message', check=message_check, timeout=30.0)
        except asyncio.TimeoutError:
            to_delete.append(await self.channel.send('Took too long.'))
            await asyncio.sleep(5)
        else:
            page = int(msg.content)
            to_delete.append(msg)
            if page != 0 and page <= self.maximum_pages:
                await self.show_page(page)
            else:
                to_delete.append(await self.channel.send(f'Invalid page given. ({page}/{self.maximum_pages})'))
                await asyncio.sleep(5)

        try:
            await self.channel.delete_messages(to_delete)
        except Exception:
            pass

    async def stop_pages(self):
        """stops the interactive pagination session"""
        await self.message.delete()
        self.paginating = False

    def react_check(self, reaction, user):
        if user is None or user.id != self.author.id:
            return False

        if reaction.message.id != self.message.id:
            return False

        for (emoji, func) in self.reaction_emojis:
            if str(reaction.emoji) == emoji:
                self.match = func
                return True
        return False

    async def paginate(self):
        """Actually paginate the entries and run the interactive loop if necessary."""
        first_page = self.show_page(1, first=True)
        self.bot.loop.create_task(first_page)

        while self.paginating:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=self.react_check, timeout=self.delete_after)
            except asyncio.TimeoutError:
                self.paginating = False
                try:
                    await self.message.delete()
                except Exception:
                    pass
                finally:
                    break
            try:
                await self.message.remove_reaction(reaction, user)
            except Exception:
                pass

            await self.match()


class EmbedPaginator:
    def __init__(self, ctx, **kwargs):
        self.bot = ctx.bot

        self.message = ctx.message
        self.channel = ctx.channel
        self.context = ctx

        self.embeds = kwargs.get('embeds')

        self.show_entry_count = kwargs.get('show_entry_count', True)
        self.paginating = True

        self.author = kwargs.get("author", ctx.author)

        self.delete_after = kwargs.get('delete_after', 300)

        pages, left_over = divmod(len(self.embeds), 1)
        if left_over:
            pages += 1

        self.maximum_pages = pages
        self.reaction_emojis = [
            ('⏮️', self.first_page),
            ('◀️', self.previous_page),
            ('⏹️', self.stop_pages),
            ('▶️', self.next_page),
            ('⏭️', self.last_page)
        ]

        if ctx.guild is not None:
            self.permissions = self.channel.permissions_for(ctx.guild.me)
        else:
            self.permissions = self.channel.permissions_for(ctx.bot.user)

        if not self.permissions.embed_links:
            raise commands.BotMissingPermissions(['embed_links'])

        if not self.permissions.send_messages:
            raise commands.BotMissingPermissions('Bot cannot send messages.')

        if self.paginating:
            if not self.permissions.add_reactions:
                raise commands.BotMissingPermissions(
                    'I do not have permissions to add reactions.')

            if not self.permissions.read_message_history:
                raise commands.BotMissingPermissions(
                    'I do not have permissions to Read Message History.')

    def get_embed(self, page):
        base = (page - 1) * 1
        embed = self.embeds[base]

        if self.show_entry_count:
            text = f'Showing page {page}/{self.maximum_pages}'
            embed.set_footer(text=text)

        return embed

    async def show_page(self, page, *, first=False):
        self.current_page = page
        embed = self.get_embed(page)

        if not first:
            await self.message.edit(embed=embed)
            return

        self.message = await self.channel.send(embed=embed)
        for (reaction, _) in self.reaction_emojis:
            if self.maximum_pages == 2 and reaction in ('◀️', '▶️'):
                continue

            if self.maximum_pages == 1 and reaction in ('◀️', '▶️', '⏮️', '⏭️'):
                continue

            await self.message.add_reaction(reaction)

    async def checked_show_page(self, page):
        if page != 0 and page <= self.maximum_pages:
            await self.show_page(page)

    async def first_page(self):
        """goes to the first page"""
        await self.show_page(1)

    async def last_page(self):
        """goes to the last page"""
        await self.show_page(self.maximum_pages)

    async def next_page(self):
        """goes to the next page"""
        await self.checked_show_page(self.current_page + 1)

    async def previous_page(self):
        """goes to the previous page"""
        await self.checked_show_page(self.current_page - 1)

    async def show_current_page(self):
        if self.paginating:
            await self.show_page(self.current_page)

    async def numbered_page(self):
        """lets you type a page number to go to"""
        to_delete = []
        to_delete.append(await self.channel.send('What page do you want to go to?'))

        def message_check(m):
            return m.author == self.author and \
                self.channel == m.channel and \
                m.content.isdigit()

        try:
            msg = await self.bot.wait_for('message', check=message_check, timeout=30.0)
        except asyncio.TimeoutError:
            to_delete.append(await self.channel.send('Took too long.'))
            await asyncio.sleep(5)
        else:
            page = int(msg.content)
            to_delete.append(msg)
            if page != 0 and page <= self.maximum_pages:
                await self.show_page(page)
            else:
                to_delete.append(await self.channel.send(f'Invalid page given. ({page}/{self.maximum_pages})'))
                await asyncio.sleep(5)

        try:
            await self.channel.delete_messages(to_delete)
        except Exception:
            pass

    async def stop_pages(self):
        """stops the interactive pagination session"""
        await self.message.delete()
        self.paginating = False

    def react_check(self, reaction, user):
        if user is None or user.id != self.author.id:
            return False

        if reaction.message.id != self.message.id:
            return False

        for (emoji, func) in self.reaction_emojis:
            if str(reaction.emoji) == emoji:
                self.match = func
                return True
        return False

    async def paginate(self):
        """Actually paginate the embeds and run the interactive loop if necessary."""
        first_page = self.show_page(1, first=True)
        self.bot.loop.create_task(first_page)

        while self.paginating:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=self.react_check, timeout=self.delete_after)
            except asyncio.TimeoutError:
                self.paginating = False
                try:
                    await self.message.delete()
                except Exception:
                    pass
                finally:
                    break
            try:
                await self.message.remove_reaction(reaction, user)
            except Exception:
                pass

            await self.match()
