import discord
from discord.ext import commands
import matplotlib.pyplot as plt
import numpy as np

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def graph(ctx, *, equation: str):
    x = np.linspace(-10, 10, 1000)
    y = eval(equation)
    plt.plot(x, y)
    plt.savefig('graph.png')
    await ctx.send(file=discord.File('graph.png'))

bot.run('[redacted]')
