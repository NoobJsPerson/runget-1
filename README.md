# RunGet Bot
RunGet is a discord bot that posts recent verified runs from Speedrun.com 
# How to setup the bot
#### ⚠️ Warning: You need to have python and git installed
If you don't have them you can install them using the commands/links right here ￬
#### Linux:
- Debian and Debian based distros (Ubuntu, Kubuntu, Pop_!OS...):
`apt install python git`
- Arch and Arch based distros (like Manjaro)
`pacman install python git`
#### Windows:
- Red Hat Enterprise Linux and centOS
`rpm install python git`
- [Git for Windows](https://gitforwindows.org/)
- [Python Installer 64-bit (Recommended)](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe)
- [Python Installer 32-bit](https://www.python.org/ftp/python/3.9.6/python-3.9.6.exe)
#### macOS:
[Git Installer](https://git-scm.com/download/mac)
[Python 64-bit Intel installer](https://www.python.org/ftp/python/3.9.6/python-3.9.6-macosx10.9.pkg)
[Python 64-bit universal2 installer](https://www.python.org/ftp/python/3.9.6/python-3.9.6-macos11.pkg)
1. run this on terminal to clone the repository and install dependencies `git clone https://github.com/Skycloudd/runget && cd runget && pip install -r requirements.txt`
2. add your bots token to the `config.json` and the prefix that you want the bot to have between quotes in the bracket in front of prefixes like this
```
{
  "prefixes":["!"]
}
```
3. run the bot using `python main.py`
