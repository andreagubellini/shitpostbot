# Discord shitposter

this discord bot scrapes random images out of N 4chan boards & N threads then dumps either an img, webm or gif to your server.

## Installation
Your python env must satisfy the dependencies in `requirements.txt`, if you're using anaconda you can automatically create an env with all the correct deps using the included yml env configurator.   

`conda create env -f shitpostbot_env.yml`

this will automatically create a `shitpost_bot` environment, which you can activate with   

`conda activate shitpost_bot`

## Configuration
First you have to create your bot using Discord's developer applet, just follow this guide:  [really nice guide ](https://realpython.com/how-to-make-a-discord-bot-python/)
You have to compile a `.yml` configuration file like the included `config_ex.yml`
```
bot:
    channelid: my_channel_id
    token: token
chan:
    boards:
        - a
        - b
        - c
        - vg
        - c
        - r9k
        - mlp
        - wsg
```
You have to fill in your channel's ID and your token.
**warning**: do not share your token with anyone or commit it to your repo: bot tokens are powerful tools.

## Usage
To start your shitposting bot just type

`python bot.py -f myconfig.yml`

If you ever get confused about the arguments just type

`python bot.py -h`

Have a nice shitposting day and don't forget your oats.
