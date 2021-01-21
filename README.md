# discord_utils.py | Docs

An easy to use Python Wrapper for the [Our upcoming API](https://google.com)\
For any questions and support, you can join the [Support Server](https://discord.gg/aBM5xz6)

To begin with, you'll have to install the package by doing one of the following commands:

- `pip install git+https://github.com/ggashish/discord_utils`

After that, you will have to create the client:
```py
import discord_utils

client = discord_utils.Client()
```

## Using the wrapper:
All available endpoints you can use.

### await client.eight_ball(text)

Returns 8ball answer to your text.

**Parameters**:

- text `string` | Text for the 8ball.

**Return type**: `str`

---

### await client.meme()

Generates an random meme.

**Parameters**:

- None

**Return type:** `dict`

---

### await client.advice()

Generates an random advice.

**Return type:** `dict`

---

### await client.ascii(text)

Get a calling meme image with your text.

**Parameters**:

- text `string` | Your text that you want to convert into ascii.

**Return type:** `str`

---

### await client.joke()
Generates an random joke.

**Parameters**:

 - None

**Return Type:** `dict`

---

### await client.password(length=12, type="medium")

Generates an random password according to your parameters.

**Parameters**:

- lenght `integer` | The length of the password you want.
- type `string` | Type of the password you want (easy, medium, hard). 
 
**Return type:** `str`

---

### await client.changemymind(text)

Get a calling meme image with your text.

**Parameters**:

- text `string` | Your text that you want to convert into ascii.

**Return type:** `str`

---

