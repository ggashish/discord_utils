# discord_utils | Docs

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

Generates an changemymind image

**Parameters**:

- text `string` | Your text that you want in your changemymind image.

**Return type:** `dict`

---

### await client.fact(type="dog")

Generates random facts.

**Parameters**:

- type `string` | The type of fact you want (dog, cat, fox, bird, panda, koala)

**Return type:** `dict`

---

### await client.image(type="dog")

Generates random images.

**Parameters**:

- type `string` | The type of image you want (dog, cat, fox, bird, panda, koala, red_panda)

**Return type:** `dict`

---

### await client.image(type="dog")

Generates random images.

**Parameters**:

- type `string` | The type of image you want (dog, cat, fox, bird, panda, koala, red_panda)

**Return type:** `dict`

---

### await client.wink()

Generates an random wink images.

**Parameters**:

- None

  **Return type:** `dict`

---

### await client.pat()

Generates an random pat images.

**Parameters**:

- None

  **Return type:** `dict`

---

### await client.hug()

Generates an random hug images.

**Parameters**:

- None

  **Return type:** `dict`

  ***

### await client.gay(avatar_url)

Converts the avatar into an gay image.

**Parameters**:

- avatar_url `string` | Link of avatar you want to convert.

  **Return type:** `dict`

  ***

### await client.glass(avatar_url)

Converts the avatar into an glass image.

**Parameters**:

- avatar_url `string` | Link of avatar you want to convert.

  **Return type:** `dict`

---

### await client.wasted(avatar_url)

Converts the avatar into an wasted image

**Parameters**:

- avatar_url `string` | Link of avatar you want to convert.

  **Return type:** `dict`

---

### await client.triggered(avatar_url)

Converts the avatar into an triggered image

**Parameters**:

- avatar_url `string` | Link of avatar you want to convert.

  **Return type:** `dict`

---

### await client.greyscale(avatar_url)

Converts the avatar into an greyscale image

**Parameters**:

- avatar_url `string` | Link of avatar you want to convert.

  **Return type:** `dict`

---

### await client.invert(avatar_url)

Converts the avatar into an invert image

**Parameters**:

- avatar_url `string` | Link of avatar you want to convert.

  **Return type:** `dict`

---

### await client.invertgreyscale(avatar_url)

Converts the avatar into an invertgreyscale image

**Parameters**:

- avatar_url `string` | Link of avatar you want to convert.

  **Return type:** `dict`

---

### await client.brightness(avatar_url)

Increases brightness of the image.

**Parameters**:

- avatar_url `string` | Link of avatar you want to convert.

  **Return type:** `dict`

---

### await client.threshold(avatar_url)

Converts the avatar into an threshold image

**Parameters**:

- avatar_url `string` | Link of avatar you want to convert.

  **Return type:** `dict`

---
