import discord
from discord.ext import commands
import math
import matplotlib.pyplot as plt
import numpy as np

bot = commands.Bot(command_prefix='!')

@bot.command(name='calculate')
async def calculate(ctx, *, expression: str):
    try:
        result = eval(expression)
        await ctx.send(f"The result is: {result}")
    except:
        await ctx.send("Invalid expression")

@bot.command(name='graph')
async def graph(ctx, *, expression: str):
    x = np.linspace(-10, 10, 1000)
    y = eval(expression)
    plt.plot(x, y)
    plt.savefig('graph.png')
    await ctx.send(file=discord.File('graph.png'))

@bot.command(name='factorial')
async def factorial(ctx, number: int):
    result = math.factorial(number)
    await ctx.send(f"The factorial of {number} is: {result}")

@bot.command(name='square')
async def square(ctx, number: float):
    result = number ** 2
    await ctx.send(f"The square of {number} is: {result}")

@bot.command(name='factor')
async def factor(ctx, number: int):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    await ctx.send(f"The factors of {number} are: {factors}")

bot.run('[redacted]')
