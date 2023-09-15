import discord
from discord.ext import commands
import math
import matplotlib.pyplot as plt
import numpy as np
from discord import Intents
from flask import Flask
from threading import Thread app = Flask('') @app.route('/')
def main(): return "Your Bot Is Ready" def run(): app.run(host="0.0.0.0", port=8000) def keep_alive(): server = Thread(target=run) server.start()
intents = Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)
status = cycle(['with Python','JetHub']) @bot.event
async def on_ready(): change_status.start() print("Your bot is ready") @tasks.loop(seconds=10)
async def change_status(): await bot.change_presence(activity=discord.Game(next(status)))

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

@bot.command(name='sqrt')
async def sqrt(ctx, number: float):
    if number < 0:
        await ctx.send("Cannot calculate the square root of a negative number")
    else:
        result = math.sqrt(number)
        await ctx.send(f"The square root of {number} is: {result}")

@bot.command(name='log')
async def log(ctx, number: float, base: float):
    if number <= 0 or base <= 0:
        await ctx.send("Cannot calculate the logarithm of a non-positive number or with a non-positive base")
    else:
        result = math.log(number, base)
        await ctx.send(f"The logarithm base {base} of {number} is: {result}")
        
bot.run('[redacted]')
