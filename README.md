# Discord AI Chat Bot

A Discord bot that allows you to interact with AI (powered by Groq) directly from Discord chat. **100% FREE!**

## Features

- 🎯 Chat with AI by mentioning the bot or sending DMs
- 💬 Conversation history maintained per user/channel
- 🔧 Configurable AI model (default: llama-3.3-70b-versatile)
- 🎨 Typing indicators for better UX
- 📝 Commands to manage conversation history and settings
- 💰 Completely FREE - uses Groq's free tier

## Prerequisites

- Python 3.8 or higher
- A Discord Bot Token (see setup instructions below)
- A Groq API Key (FREE - see setup instructions below)

## Setup Instructions

### 1. Create a Discord Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section
4. Click "Add Bot" and confirm
5. Under "Token", click "Reset Token" and copy the token (you'll need this)
6. Enable the following Privileged Gateway Intents:
   - MESSAGE CONTENT INTENT (Required)
   - SERVER MEMBERS INTENT (Optional, for member features)
7. Go to the "OAuth2" > "URL Generator" section
8. Select scopes: `bot` and `applications.commands`
9. Select bot permissions: `Send Messages`, `Read Message History`, `Use External Emojis`
10. Copy the generated URL and open it in your browser to invite the bot to your server

### 2. Get Groq API Key (FREE!)

1. Go to [Groq Console](https://console.groq.com/)
2. Sign up or log in (no credit card required!)
3. Go to [API Keys](https://console.groq.com/keys)
4. Click "Create API Key"
5. Copy the key (you'll need this)

### 3. Install Dependencies

1. **Verify Python is installed:**
   - Open a terminal/command prompt (PowerShell on Windows, Terminal on Mac/Linux)
   - Run: `python --version` or `python3 --version`
   - You should see something like `Python 3.8.x` or higher
   - If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

2. **Navigate to the project directory:**
   ```bash
   cd "C:\Users\Daniel.Boras\Desktop\Cursor\Discord Bot"
   ```
   (Or navigate to wherever you saved the bot files)

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
   
   **If `pip` doesn't work, try:**
   - `python -m pip install -r requirements.txt`
   - `python3 -m pip install -r requirements.txt`
   - `py -m pip install -r requirements.txt` (Windows)

4. **Verify installation:**
   - You should see packages being downloaded and installed
   - Look for "Successfully installed" messages
   - If you see any errors, make sure you have an internet connection and try again

### 4. Configure Environment Variables

1. Copy `env.example` to `.env`:
   ```bash
   copy env.example .env
   ```
   (On Linux/Mac, use: `cp env.example .env`)

2. Edit `.env` and add your tokens:
   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Optional settings:
   - `DISCORD_CHANNEL_ID`: Restrict bot to a specific channel (leave empty for all channels)
   - `AI_MODEL`: AI model to use (default: llama-3.3-70b-versatile)
     - Available models: `llama-3.3-70b-versatile`, `mixtral-8x7b-32768`, `gemma2-9b-it`

### 5. Run the Bot

```bash
python bot.py
```

You should see a message confirming the bot has logged in to Discord!

## Usage

### Chatting with AI

1. **Mention the bot** in any channel (if channel restriction is not set):
   ```
   @YourBotName What is Python?
   ```

2. **Send a DM** directly to the bot:
   ```
   What is Python?
   ```

The bot will respond with AI-generated answers. Conversation history is maintained per user/channel, so the bot can remember context from previous messages.

### Commands

- `!ping` - Check if the bot is responsive
- `!clear` - Clear your conversation history for the current channel
- `!model [model_name]` - View or change the AI model (e.g., `llama-3.3-70b-versatile`, `mixtral-8x7b-32768`)

## Configuration Options

You can customize the bot behavior by modifying environment variables in `.env`:

- `DISCORD_BOT_TOKEN`: Your Discord bot token (required)
- `GROQ_API_KEY`: Your Groq API key (required, FREE!)
- `DISCORD_CHANNEL_ID`: Restrict bot to specific channel (optional)
- `AI_MODEL`: AI model to use (default: llama-3.3-70b-versatile)

## Notes

- The bot maintains conversation history in memory (last 20 messages per user/channel)
- Responses longer than 2000 characters are split into multiple messages
- Make sure to keep your `.env` file secure and never commit it to version control
- The `.env` file is already included in `.gitignore` for your safety

## Troubleshooting

**Bot doesn't respond:**
- Check that the bot has the "MESSAGE CONTENT INTENT" enabled in Discord Developer Portal
- Verify your tokens are correct in the `.env` file
- Make sure the bot has permission to read and send messages in the channel

**Groq API errors:**
- Verify your Groq API key is valid
- Check that you're within Groq's free tier limits
- Ensure the model name is correct (if you changed it)
- Popular models: `llama-3.3-70b-versatile`, `mixtral-8x7b-32768`, `gemma2-9b-it`

## Free 24/7 Hosting Options

To keep your bot online 24/7 for free, here are the best options:

### Option 1: Railway (Recommended - Easiest) 🚂

**Railway** offers $5 free credit per month, which is more than enough for a Discord bot.

1. **Sign up:**
   - Go to [railway.app](https://railway.app/)
   - Sign up with GitHub (recommended) or email

2. **Create a new project:**
   - Click "New Project"
   - Select "Deploy from GitHub repo" (if you have your code on GitHub)
   - OR select "Empty Project" and upload files manually

3. **Set up your bot:**
   - If using GitHub: Connect your repository
   - If using Empty Project: Upload your bot files (`bot.py`, `requirements.txt`)
   - Railway will auto-detect Python

4. **Configure environment variables:**
   - Go to "Variables" tab
   - Add:
     - `DISCORD_BOT_TOKEN` = your Discord bot token
     - `GROQ_API_KEY` = your Groq API key
     - (Optional) `DISCORD_CHANNEL_ID` = your channel ID
     - (Optional) `AI_MODEL` = llama-3.3-70b-versatile

5. **Deploy:**
   - Railway will automatically start your bot
   - Check the "Deployments" tab to see logs
   - Your bot should now be online 24/7!

**Note:** Railway's free tier gives $5 credit/month. A Discord bot typically uses $0.50-1.00/month, so it's effectively free.

---

### Option 2: Render (Free but spins down) ☁️

**Render** offers a free tier, but services spin down after 15 minutes of inactivity.

1. Go to [render.com](https://render.com/)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name:** your-bot-name
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
6. Add environment variables (same as Railway above)
7. Click "Create Web Service"

**Note:** Free services on Render spin down after inactivity. For a Discord bot, this isn't ideal as it needs to stay connected. Consider Railway instead.

---

### Option 3: Replit (Free with Keep-Alive) 🔧

**Replit** can host bots 24/7, but requires some setup to prevent sleeping.

1. Go to [replit.com](https://replit.com/)
2. Create a new Repl → "Python"
3. Upload your bot files (`bot.py`, `requirements.txt`)
4. Install dependencies in the Shell: `pip install -r requirements.txt`
5. Set environment variables:
   - Click the lock icon (Secrets)
   - Add: `DISCORD_BOT_TOKEN`, `GROQ_API_KEY`
6. To keep it online 24/7:
   - Use [UptimeRobot](https://uptimerobot.com/) (free) to ping your Repl every 5 minutes
   - OR use a keep-alive script (search "Replit keep alive" for examples)

---

### Option 4: Specialized Discord Bot Hosting 🎮

These services specialize in hosting Discord bots:

- **KataBump** - [katabump.com](https://katabump.com/) - Free plan with 1512 MB RAM
- **LemonHost** - [lemonhost.me](https://lemonhost.me/) - 1GB RAM, 99.9% uptime
- **Bot-Hosting.net** - [bot-hosting.net](https://bot-hosting.net/) - Free Discord bot hosting

**Setup is similar:**
1. Sign up on the platform
2. Upload your bot files
3. Set environment variables
4. Start the bot

---

### Quick Comparison

| Service | Free Tier | 24/7 Uptime | Ease of Use | Best For |
|---------|-----------|-------------|-------------|----------|
| **Railway** | $5 credit/month | ✅ Yes | ⭐⭐⭐⭐⭐ | Recommended |
| **Render** | Yes | ❌ Spins down | ⭐⭐⭐⭐ | Not ideal for bots |
| **Replit** | Yes | ⚠️ Needs keep-alive | ⭐⭐⭐ | Learning/testing |
| **KataBump** | Yes | ✅ Yes | ⭐⭐⭐⭐ | Discord bots only |

**Recommendation:** Use **Railway** - it's the easiest and most reliable free option for keeping your bot online 24/7.

---

## License

This project is open source and available for personal use.

