import discord
from discord import app_commands
from discord.ext import commands
import os

# ---- INTENTS ----
intents = discord.Intents.default()
intents.members = True
intents.message_content = False  # Not needed yet

# ---- BOT ----
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def setup_hook(self):
        # Sync slash commands globally
        await self.tree.sync()
        print("Slash commands synced")

bot = MyBot()

# ---- EVENTS ----
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# ---- BASIC COMMAND ----
@bot.tree.command(name="ping", description="Check bot latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Pong! 🏓 `{round(bot.latency * 1000)}ms`"
    )

# ---- RUN BOT ----
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN environment variable not set")

bot.run(TOKEN)
