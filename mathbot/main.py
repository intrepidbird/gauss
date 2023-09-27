import discord
from discord import Intents
from discord.ext import commands, tasks
import math
from itertools import cycle
from threading import Thread
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask
import cmath
import statistics
import numpy as np
from asteval import Interpreter
import wolframalpha
import cmath
from sympy import symbols, lambdify
from sympy.parsing.sympy_parser import parse_expr

client = wolframalpha.Client('id')
aeval = Interpreter()
app = Flask('')

@app.route('/')

# 'Keep Alive' Stuff
def main(): return "[+] Ready"

def run(): app.run(host="0.0.0.0", port=8000)

def keep_alive(): 
    server = Thread(target=run) 
    server.start()

intents = Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)
status = cycle(['!help, !ask'])

@bot.event
async def on_ready(): change_status.start() 
print("[+] Ready")

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

# Commands

@bot.command(name='flag')
async def flag(ctx):
    await ctx.send("intrepidbird{m47h3mag1c14n}")

@bot.command(name='calculate')
async def calculate(ctx, expr):
    try:
        x = aeval(expr)
        await ctx.send(x)
    except:
        await ctx.send('Please enter a valid mathematical expression.')

@bot.command(name='graph')
async def graph(ctx, *, expression: str):
    x = symbols('x')
    y_expr = parse_expr(expression)
    y_func = lambdify(x, y_expr, "numpy")

    x_vals = np.linspace(-10, 10, 1000)
    y_vals = y_func(x_vals)

    plt.plot(x_vals, y_vals)
    plt.savefig('graph.png')
    await ctx.send(file=discord.File('graph.png'))

@bot.command(name='factorial')
async def factorial(ctx, number: int):
    result = math.factorial(number)
    if len(str(result)) > 2000:
        with open('factorial_result.txt', 'w') as f:
            f.write(f"The factorial of {number} is: {result}")
        await ctx.send("The result is over 2000 digits. It has been written to 'factorial_result.txt'.")
        await ctx.send(file=discord.File('factorial_result.txt'))
        os.remove('factorial_result.txt')  # remove the file after sending it
    else:
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

@bot.command(name='pow')
async def pow(ctx, base: float, exponent: float):
    result = math.pow(base, exponent)
    await ctx.send(f"{base} raised to the power of {exponent} is: {result}")

@bot.command(name='mod')
async def mod(ctx, number1: float, number2: float):
    result = number1 % number2
    await ctx.send(f"The remainder of the division of {number1} by {number2} is: {result}")

@bot.command(name='hypot')
async def hypot(ctx, side1: float, side2: float):
    result = math.hypot(side1, side2)
    await ctx.send(f"The length of the hypotenuse for a right triangle with sides {side1} and {side2} is: {result}")

@bot.command(name='solve_quad')
async def solve_quad(ctx, a: float, b: float, c: float):
    d = (b**2) - (4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    await ctx.send(f"The solutions are {sol1} and {sol2}")

@bot.command(name='std_dev')
async def std_dev(ctx, *args: float):
    data = list(args)
    result = statistics.stdev(data)
    await ctx.send(f"The standard deviation is {result}")

@bot.command(name='fibonacci')
async def fibonacci(ctx, n: int):
    a, b = 0, 1
    fib_sequence = []
    while a < n:
        fib_sequence.append(a)
        a, b = b, a+b
    await ctx.send(f"The Fibonacci sequence up to {n} is: {fib_sequence}")

@bot.command(name='inverse_matrix')
async def inverse_matrix(ctx, *args: float):
    matrix = np.array(args).reshape((int(np.sqrt(len(args))), -1))
    try:
        inverse = np.linalg.inv(matrix)
        await ctx.send(f"The inverse of the matrix is: {inverse}")
    except np.linalg.LinAlgError:
        await ctx.send("The matrix is not invertible.")

@bot.command(name='goat')
async def goat(ctx):
    await ctx.send("Gauss is the Greatest of all Time in Mathematics")

@bot.command(name='determinant')
async def determinant(ctx, *args: float):
    matrix = np.array(args).reshape((int(np.sqrt(len(args))), -1))
    det = np.linalg.det(matrix)
    await ctx.send(f"The determinant of the matrix is: {det}")

@bot.command(name='ask')
async def ask(ctx, *, question: str):
    try:
        res = client.query(question)
        if res['@success'] == 'false':
            await ctx.send('I could not find an answer to your question.')
        else:
            answer = next(res.results).text
            await ctx.send(f'The answer to your question is: {answer}')
    except Exception as e:
        await ctx.send(f'An error occurred {str(e)}')


@bot.command(name='solve')
async def solve(ctx, a: float, b: float, c: float):
    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    await ctx.send("The solutions are {0} and {1}".format(sol1,sol2))

@bot.command(name='eigen')
async def eigen(ctx, *args: float):
    matrix = np.array(args).reshape((int(np.sqrt(len(args))), -1))
    try:
        eigenvalues, eigenvectors = np.linalg.eig(matrix)
        await ctx.send(f"The eigenvalues of the matrix are: {eigenvalues}, and the corresponding eigenvectors are: {eigenvectors}")
    except np.linalg.LinAlgError:
        await ctx.send("The eigenvalues and eigenvectors could not be calculated.")

bot.run('token')
