import requests
import random

import json
from aiohttp import ClientSession

from asyncio import AbstractEventLoop, get_event_loop
from discord_utils.exceptions import MissingArgumentError, FetchError


class MyClient():

    def __init__(self, session: ClientSession = None, loop: AbstractEventLoop = None) -> None:
        self.session = ClientSession(loop=get_event_loop() or loop) or session
        self._api_url = "soon"

    async def request_url(self, url, headers=None, params=None):
        return await self.session.get(url, headers=headers, params=params)

    async def eight_ball(self, question):
        choices = ['🟢 It is certain.',
                   '🟢 It is decidedly so.',
                   '🟢 Without a doubt.',
                   '🟢 Yes – definitely.',
                   '🟢 You may rely on it.',
                   '🟢 As I see it, yes.',
                   '🟢 Most likely.',
                   '🟢 Outlook good.',
                   '🟢 Yes.',
                   '🟢 Signs point to yes.',
                   '🟡 Reply hazy, try again.',
                   '🟡 Ask again later.',
                   '🟡 Better not tell you now.',
                   '🟡 Cannot predict now.',
                   '🟡 Concentrate and ask again.',
                   "🔴 Don't count on it.",
                   '🔴 My reply is no.',
                   '🔴 My sources say no.',
                   '🔴 Outlook not so good.',
                   '🔴 Very doubtful.']

        return random.choice(choices)

    async def meme(self):
        req = await self.request_url("https://memes.blademaker.tv/api")
        try:
            return await req.json()
        except Exception:
            raise FetchError('FetchError')

    async def advice(self):
        req = await self.request_url("https://api.adviceslip.com/advice")

        try:
            return await req.json()
        except:
            raise FetchError('FetchError')

    async def ascii(self, text):
        req = await self.request_url(f"http://artii.herokuapp.com/make?text={text}")

        try:
            return await req.text()
        except:
            raise FetchError('FetchError')

    async def joke(self):
        req = await self.request_url(
            "https://official-joke-api.appspot.com/random_joke")

        try:
            return await req.json()
        except:
            raise FetchError('FetchError')

    async def password(self, length: int = 12, type="medium"):
        lower_case = 'abcdefghijklmnopqrstuvwxyz'
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '123456789'
        punctuation = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

        password = ""
        if type == "easy":

            for c in range(length):
                password += (random.choice(lower_case + digits))

            return password

        if type == "medium":
            for c in range(length):
                password += (random.choice(lower_case + upper_case + digits))

            return password

        if type == "hard":
            for c in range(length):
                password += (random.choice(lower_case +
                                           upper_case + digits + punctuation))

            return password

    async def changemymind(self, text):
        req = await self.request_url(
            f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}")

        try:
            return await req.json()
        except:
            raise FetchError('FetchError')

    async def fact(self, type="dog"):
        url = "https://some-random-api.ml/facts/"

        if type == "dog":
            url += "dog"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "cat":
            url += "cat"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "panda":
            url += "panda"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "fox":
            url += "fox"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "Koala":
            url += "Koala"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "bird":
            url += "bird"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

    async def image(self, type="dog"):
        url = "https://some-random-api.ml/img/"

        if type == "dog":
            url += "dog"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "cat":
            url += "cat"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "bird":
            url += "bird"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "fox":
            url += "fox"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "koala":
            url += "koala"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "panda":
            url += "panda"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

        if type == "red_panda":
            url += "red_panda"
            req = await self.request_url(url)
            try:
                return await req.json()
            except:
                raise FetchError('FetchError')

    async def wink(self):
        req = await self.request_url("https://some-random-api.ml/animu/wink")

        try:
            return await req.json()
        except:
            raise FetchError('FetchError')

    async def pat(self):
        req = await self.request_url("https://some-random-api.ml/animu/pat")

        try:
            return await req.json()
        except:
            raise FetchError('FetchError')

    async def hug(self):
        req = await self.request_url("https://some-random-api.ml/animu/hug")

        try:
            return await req.json()
        except:
            raise FetchError('FetchError')

    async def gay(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/gay?avatar={avatar_url}"
        return url

    async def glass(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/glass?avatar={avatar_url}"
        return url

    async def wasted(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/wasted?avatar={avatar_url}"
        return url

    async def triggered(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/triggered?avatar={avatar_url}"
        return url

    async def greyscale(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/greyscale?avatar={avatar_url}"
        return url

    async def invert(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/invert?avatar={avatar_url}"
        return url

    async def invertgreyscale(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={avatar_url}"
        return url

    async def brightness(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/brightness?avatar={avatar_url}"
        return url

    async def threshold(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/threshold?avatar={avatar_url}"
        return url

    async def greyscale(self, avatar_url):
        url = f"https://some-random-api.ml/canvas/greyscale?avatar={avatar_url}"
        return url
