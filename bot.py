import sys
import yaml
from argparse import ArgumentParser
from pathlib import Path
#import pdb

from discord.ext import commands
from scraper import scraper


def main():
    parser = ArgumentParser()
    # token as path to file
    parser.add_argument(
        "-f",
        "--config",
        action="store",
        type=str,
        dest="cfg_fpath",
        help="Path to config file"
        )
    
    args = parser.parse_args()
    
    # print help and exit if no arguments are passed
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    cfg_fpath = Path(args.cfg_fpath)
    
    with cfg_fpath.open(mode="r") as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)
        
    token = cfg["bot"]["token"]
    ch_id = cfg["bot"]["channelid"]
    boards = cfg["chan"]["boards"]
    
    client = commands.Bot(command_prefix='.')
    @client.event
    async def on_ready():
        print('bot is ready.')
        
    @client.event
    async def on_message(message):
        if message.content.startswith('!shitpost'):
            #pdb.set_trace()
            channel = client.get_channel(int(ch_id))
            img = scraper.scrape(boards)
            await channel.send("Ecco la tua daily dose di shitpost: \n"+img)
    
    client.run(token)

if __name__ == "__main__":
    main()