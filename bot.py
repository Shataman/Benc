import os
import discord
from discord.ext import commands
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get configuration from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')  # Optional: restrict to specific channel
MODEL = os.getenv('AI_MODEL', 'llama-3.3-70b-versatile')  # Default Groq model

# Validate required environment variables
if not DISCORD_TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN not found in environment variables. Please check your .env file.")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")

# Initialize Groq client
ai_client = Groq(api_key=GROQ_API_KEY)

# Set up Discord bot intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content
intents.members = True  # Optional: for member-related features

# Initialize Discord bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Store conversation history per channel (optional: can be enhanced with database)
conversation_history = {}

def get_conversation_key(channel_id, user_id):
    """Generate a unique key for conversation history"""
    return f"{channel_id}_{user_id}"

async def get_ai_response(prompt, conversation_key):
    """Get response from Groq AI API"""
    try:
        # Get conversation history for this user/channel
        messages = conversation_history.get(conversation_key, [])
        
        # Add the new user message
        messages.append({"role": "user", "content": prompt})
        
        # Keep only last 20 messages to avoid token limits
        if len(messages) > 20:
            messages = messages[-20:]
        
        # Call Groq API
        response = ai_client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        
        # Extract the assistant's response
        assistant_message = response.choices[0].message.content
        
        # Update conversation history
        messages.append({"role": "assistant", "content": assistant_message})
        conversation_history[conversation_key] = messages
        
        return assistant_message
    
    except Exception as e:
        return f"Error getting AI response: {str(e)}"

@bot.event
async def on_ready():
    """Called when the bot is ready"""
    print(f'{bot.user} has logged in to Discord!')
    print(f'Bot is connected to {len(bot.guilds)} server(s)')
    # Set bot status
    await bot.change_presence(activity=discord.Game(name="AI Chat | !help"))

@bot.event
async def on_message(message):
    """Handle incoming messages"""
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    
    # Check if message is in the specified channel (if CHANNEL_ID is set)
    if CHANNEL_ID and str(message.channel.id) != CHANNEL_ID:
        return
    
    # Check if message mentions the bot or is in a DM
    bot_mentioned = bot.user in message.mentions
    is_dm = isinstance(message.channel, discord.DMChannel)
    
    # Only respond to mentions or DMs (you can change this logic)
    if not bot_mentioned and not is_dm:
        # Optional: respond to all messages in the channel if you want
        # Remove this return to make the bot respond to all messages
        return
    
    # Remove bot mention from message content
    content = message.content
    if bot_mentioned:
        content = content.replace(f'<@{bot.user.id}>', '').strip()
    
    # Ignore empty messages
    if not content:
        await message.channel.send("Hi! I'm your AI bot. Mention me or DM me to chat!")
        return
    
    # Show typing indicator
    async with message.channel.typing():
        # Get conversation key
        conversation_key = get_conversation_key(message.channel.id, message.author.id)
        
        # Get AI response
        response = await get_ai_response(content, conversation_key)
        
        # Split response if it's too long (Discord has a 2000 character limit)
        if len(response) <= 2000:
            await message.reply(response)
        else:
            # Split into chunks
            chunks = [response[i:i+2000] for i in range(0, len(response), 2000)]
            for chunk in chunks:
                await message.channel.send(chunk)

@bot.command(name='clear')
async def clear_history(ctx):
    """Clear conversation history for the current user/channel"""
    conversation_key = get_conversation_key(ctx.channel.id, ctx.author.id)
    if conversation_key in conversation_history:
        del conversation_history[conversation_key]
        await ctx.send("Conversation history cleared!")
    else:
        await ctx.send("No conversation history to clear.")

@bot.command(name='model')
async def change_model(ctx, model_name=None):
    """View or change the AI model"""
    global MODEL
    if model_name:
        MODEL = model_name
        await ctx.send(f"Model changed to: {MODEL}")
    else:
        await ctx.send(f"Current model: {MODEL}")

@bot.command(name='ping')
async def ping(ctx):
    """Check if the bot is responsive"""
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

# Run the bot
if __name__ == "__main__":
    try:
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        print(f"Error starting bot: {e}")

