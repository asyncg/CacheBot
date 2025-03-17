# CacheBot

Discord Bot for Brother's Discord Server.\
Comes with Clash API Integration and two very lazy devs

## Installation

- For the first step, you need Python and Poetry installed on your system

```bash
    git clone https://github.com/asyncg/CacheBot.git
    cd CacheBot
    poetry install
```

- Now create your `secrets.toml` file and place it in the root directory
```toml
[discord]
token = "YOUR_DISCORD_BOT_TOKEN_HERE"

[clash]
email = "CLASH_API_EMAIL"
password = "CLASH_API_PASSWORD"
```

## Run Locally

- Simple, just make sure you are in the root directory of the project

```bash
    poetry run python cachebot/main.py
```


