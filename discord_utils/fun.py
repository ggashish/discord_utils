import requests
import random
import json

from discord_utils.exceptions import MissingArgumentError, FetchError


def request_url(url, headers=None, params=None):
    if not headers and params:
        r = requests.get(url)
        return r
    if headers and params:
        r = requests.get(url, headers=headers, params=params)
        return r
    if headers and not params:
        r = requests.get(url, headers=headers)
        return r
    if params and not headers:
        r = requests.get(url, params=params)
        return r


def eight_ball(question):
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


def meme():
    req = request_url("https://memes.blademaker.tv/api")

    try:
        return req.json()
    except:
        raise FetchError('FetchError')


def advice():
    req = request_url("https://api.adviceslip.com/advice")

    try:
        return req.json()
    except:
        raise FetchError('FetchError')


def ascii(text):
    req = request_url(f"http://artii.herokuapp.com/make?text={text}")

    try:
        return req.text
    except:
        raise FetchError('FetchError')


def joke():
    req = request_url("https://official-joke-api.appspot.com/random_joke")

    try:
        return req.json()
    except:
        raise FetchError('FetchError')


def password(length: int = 12, type="medium"):
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


def changemymind(text):
    req = request_url(
        f"https://nekobot.xyz/api/imagegen?type=changemymind&text={text}")

    try:
        return req.json()
    except:
        raise FetchError('FetchError')


def fact(type="dog"):
    url = "https://some-random-api.ml/facts/"

    if type == "dog":
        url += "dog"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "cat":
        url += "cat"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "panda":
        url += "panda"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "fox":
        url += "fox"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "Koala":
        url += "Koala"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "bird":
        url += "bird"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')


def image(type="dog"):
    url = "https://some-random-api.ml/img/"

    if type == "dog":
        url += "dog"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "cat":
        url += "cat"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "bird":
        url += "bird"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "fox":
        url += "fox"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "koala":
        url += "koala"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "panda":
        url += "panda"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')

    if type == "red_panda":
        url += "red_panda"
        req = request_url(url)
        try:
            return req.json()
        except:
            raise FetchError('FetchError')


def wink():
    req = request_url("https://some-random-api.ml/animu/wink")

    try:
        return req.json()
    except:
        raise FetchError('FetchError')


def pat():
    req = request_url("https://some-random-api.ml/animu/pat")

    try:
        return req.json()
    except:
        raise FetchError('FetchError')


def hug():
    req = request_url("https://some-random-api.ml/animu/hug")

    try:
        return req.json()
    except:
        raise FetchError('FetchError')


def hug():
    req = request_url("https://some-random-api.ml/animu/hug")

    try:
        return req.json()
    except:
        raise FetchError('FetchError')


def gay(avatar_url):
    url = f"https://some-random-api.ml/canvas/gay?avatar={avatar_url}"
    return url


def glass(avatar_url):
    url = f"https://some-random-api.ml/canvas/glass?avatar={avatar_url}"
    return url


def wasted(avatar_url):
    url = f"https://some-random-api.ml/canvas/wasted?avatar={avatar_url}"
    return url


def triggered(avatar_url):
    url = f"https://some-random-api.ml/canvas/triggered?avatar={avatar_url}"
    return url


def greyscale(avatar_url):
    url = f"https://some-random-api.ml/canvas/greyscale?avatar={avatar_url}"
    return url


def invert(avatar_url):
    url = f"https://some-random-api.ml/canvas/invert?avatar={avatar_url}"
    return url


def invertgreyscale(avatar_url):
    url = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={avatar_url}"
    return url


def brightness(avatar_url):
    url = f"https://some-random-api.ml/canvas/brightness?avatar={avatar_url}"
    return url


def threshold(avatar_url):
    url = f"https://some-random-api.ml/canvas/threshold?avatar={avatar_url}"
    return url


def greyscale(avatar_url):
    url = f"https://some-random-api.ml/canvas/greyscale?avatar={avatar_url}"
    return url
