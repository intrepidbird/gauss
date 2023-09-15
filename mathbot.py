import discord
from discord import Intents
from discord.ext import commands, tasks
import math
from itertools import cycle
from threading import Thread
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask

app = Flask('')
@app.route('/')

# 'Keep Alive' Stuff
def main(): return "Your Bot Is Ready"

def run(): app.run(host="0.0.0.0", port=8000)

def keep_alive(): 
    server = Thread(target=run) 
    server.start()

intents = Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

status = cycle(['!help'])

@bot.event
async def on_ready(): change_status.start() 
print("Your bot is ready")

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

# Commands

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

@bot.command(name='cube')
async def cube(ctx, number: float):
    result = number ** 3
    await ctx.send(f"The cube of {number} is: {result}")

@bot.command(name='sin')
async def sin(ctx, number: float):
    result = math.sin(math.radians(number))
    await ctx.send(f"The sine of {number} is: {result}")

@bot.command(name='cos')
async def cos(ctx, number: float):
    result = math.cos(math.radians(number))
    await ctx.send(f"The cosine of {number} is: {result}")

@bot.command(name='tan')
async def tan(ctx, number: float):
    result = math.tan(math.radians(number))
    await ctx.send(f"The tangent of {number} is: {result}")

@bot.command(name='ln')
async def ln(ctx, number: float):
    if number <= 0:
        await ctx.send("Cannot calculate the natural logarithm of a non-positive number")
    else:
        result = math.log(number)
        await ctx.send(f"The natural logarithm of {number} is: {result}")

@bot.command(name='exp')
async def exp(ctx, number: float):
    result = math.exp(number)
    await ctx.send(f"The exponential of {number} is: {result}")

@bot.command(name='is_prime')
async def is_prime(ctx, number: int):
    if number <= 1:
        await ctx.send(f"{number} is not a prime number.")
    elif number == 2:
        await ctx.send(f"{number} is a prime number.")
    else:
        for i in range(2, number):
            if (number % i) == 0:
                await ctx.send(f"{number} is not a prime number.")
                break
        else:
            await ctx.send(f"{number} is a prime number.")

@bot.command(name='abs')
async def abs(ctx, number: float):
    result = math.fabs(number)
    await ctx.send(f"The absolute value of {number} is: {result}")

bot.run('[redacted]')
