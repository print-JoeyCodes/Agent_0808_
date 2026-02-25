import discord
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.reactions = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    channel = bot.get_channel(YOUR_CHANNEL_ID)  # Add your channel ID
    await channel.send("Bot is online!")

@bot.event
async def on_raw_reaction_add(payload):
    # Your reaction code
    YOUR_MESSAGE_ID = 1234567890
    YOUR_ROLE_NAME = "Testing Role"
    
    if payload.message_id == YOUR_MESSAGE_ID:
        guild = bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name=YOUR_ROLE_NAME)
        member = guild.get_member(payload.user_id)
        await member.add_roles(role)

bot.run(os.environ['TOKEN'])
