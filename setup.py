from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='discord_utils',
      author='Ashish Yadav',
      author_email='ashishyadav1400@gmail.com',
      version='1.0',
      packages=['discord_utils'],
      license='MIT',
      description='A simple API wrapper for discord bot commands',
      long_description=readme,
      )
