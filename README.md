## RunGet Bot
RunGet is a discord bot that posts recent verified runs from Speedrun.com 
## How to setup the bot
1. first install git and python if you having already.
for Ubuntu:
`apt install python git`
for others just replace apt with your package manager
2. then run this to clone the repository and install dependencies `git clone https://github.com/Skycloudd/runget && cd runget && pip install -r requirements.txt`
3. add your bots token to the `config.json` and the prefix that you want the bot to have between quotes in the bracket in front of prefixes like this
```
{
  "prefixes":["!"]
}
```
4. run the bot using `python main.py`
