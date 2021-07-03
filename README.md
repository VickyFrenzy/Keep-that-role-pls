# Keep that role pls

This is a troll Discord bot with the only specific purpose of making sure that a role stays on one specific user.

## Setup

Dependencies are [discord.py](https://pypi.org/project/discord.py/) and [discord-py-slash-command](https://pypi.org/project/discord-py-slash-command/).

```sh
pip install -U discord.py
pip install -U discord-py-slash-command
```

This bot needs the [Server Members Intent](https://discord.com/developers/docs/topics/gateway#privileged-intents) to be enabled.
It also uses [Discord slash commands](https://discord.com/developers/docs/interactions/slash-commands).
And it will obviously require the permission to manage roles on the Discord server.

Create your `config.json` based on `config-example.json` and fill in the details.

Invite the bot on your server of choice with that invite link for example:
`https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID_HERE&permissions=2617557056&scope=bot%20applications.commands`

Start the bot with `python main.py` or whatever.
