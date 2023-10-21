import discord
import io
import random
import matplotlib.pyplot as plt
import numpy as np
from discord.ext import commands
from matplotlib.figure import Figure
from io import *
from math import *

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def gcd(ctx, a: int, b: int):
    result = int(gcd(a, b))
    await ctx.send(f'The GCD of {a} and {b} is {result}')


@bot.command()
async def graph(ctx, *, expression: str):
    try:
        x = np.linspace(-10, 10, 1000)
        y = ast.literal_eval(expression, {'x': x, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan, 'exp': np.exp, 'log': np.log})
        fig = Figure()
        ax = fig.subplots()
        ax.plot(x, y)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.grid()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        await ctx.send(file=discord.File(buf, 'graph.png'))
    except:
        await ctx.send("Sorry, I couldn't understand that expression. Please make sure it's a valid mathematical expression.")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="/helper"))

@bot.command()
async def hi(ctx):
    await ctx.send("Hey there! I'm IntrepidBot, your personal discord robot programmed to assist in what you want. Try out my commands!")

@bot.command()
async def formulas(ctx):
    formulas = ["https://cdn.artofproblemsolving.com/attachments/9/0/0e7904bb539cd6056457058f60d7a1c7864bb8.pdf"]
    response = "Here are some AIME level mathematical formulas you might find useful:\n"
    response += '\n'.join(formulas)
    await ctx.send(response)

@bot.command()
async def helper(ctx):
    commands = ["/hi", "**/formulas**", "/game", "/hangman", "**/calc**", "**/graph**", "**/factorial**", "/trivia", "**/graph2**"]
    response = "Here is a list of available commands:\n"
    response += '\n'.join(commands)
    await ctx.send(response)

@bot.command()
async def calc(ctx, *, expression: str):
    try:
        result = ast.literal_eval(expression)
        await ctx.send(f"The result is: {result}")
    except:
        await ctx.send("Sorry, I couldn't understand that expression. Please make sure it's a valid arithmetic expression.")

@bot.command()
async def game(ctx):
    await ctx.send("Let's play Rock, Paper, Scissors! To make a move, type 'rock', 'paper', or 'scissors'.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['rock', 'paper', 'scissors']

    try:
        player_move = await bot.wait_for('message', check=check, timeout=10.0)
    except asyncio.TimeoutError:
        return await ctx.send('Sorry, you took too long to respond.')

    moves = ['rock', 'paper', 'scissors']
    bot_move = random.choice(moves)

    winner = None
    if player_move.content.lower() == bot_move:
        winner = 'Tie'
    elif (player_move.content.lower() == 'rock' and bot_move == 'scissors') or \
         (player_move.content.lower() == 'paper' and bot_move == 'rock') or \
         (player_move.content.lower() == 'scissors' and bot_move == 'paper'):
        winner = 'Player'
    else:
        winner = 'Bot'

    if winner == 'Tie':
        await ctx.send(f"It's a tie! We both chose {bot_move}.")
    else:
        await ctx.send(f"{winner} wins! You chose {player_move.content.lower()} and I chose {bot_move}.")

words = ['apple', 'banana', 'orange', 'strawberry', 'grapefruit']

@bot.command()
async def hangman(ctx):
    word = random.choice(words)
    word_display = ['\\_' for _ in range(len(word))]
    guessed_letters = []
    attempts_remaining = 6

    await ctx.send(f"Let's play Hangman! Here's your word: {' '.join(word_display)}")

    while attempts_remaining > 0:
        await ctx.send(f"Enter a letter to guess. You have {attempts_remaining} attempts remaining.")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel and m.content.isalpha() and len(m.content) == 1

        try:
            guess = await bot.wait_for('message', check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send('Sorry, you took too long to respond.')

        if guess.content.lower() in guessed_letters:
            await ctx.send(f"You already guessed the letter {guess.content.lower()}. Try a different letter.")
            continue

        guessed_letters.append(guess.content.lower())

        if guess.content.lower() in word:
            word_display = [x if x == guess.content.lower() else y for x, y in zip(word, word_display)]
            await ctx.send(f"Correct! Here's your word: {' '.join(word_display)}")
        else:
            attempts_remaining -= 1
            await ctx.send(f"Incorrect. Here's your word: {' '.join(word_display)}")

        if '\\_' not in word_display:
            await ctx.send(f"Congratulations, you won! The word was {word}.")
            return

    await ctx.send(f"Sorry, you lost. The word was {word}.")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@bot.command(name='factorial')
async def factorial_command(ctx, n: int):
    result = factorial(n)
    await ctx.send(f'The factorial of {n} is {result}')

questions = [
    {'question': 'What is the formula for calculating force?', 'answer': 'F=ma'},
    {'question': 'What is the speed of light?', 'answer': '299792458 m/s'},
    {'question': 'What is the formula for calculating work?', 'answer': 'W=Fd'},
    {'question': 'What is the first law of thermodynamics?', 'answer': 'Energy cannot be created or destroyed'},
    {'question': 'What is the second law of thermodynamics?', 'answer': 'Heat flows from hot to cold'},
    {'question': 'What are the three types of rock?', 'answer': 'Igneous, sedimentary, metamorphic'},
    {'question': 'What is the most abundant gas in Earth’s atmosphere?', 'answer': 'Nitrogen'},
    {'question': 'What is the largest ocean on Earth?', 'answer': 'Pacific Ocean'},
    {'question': 'What is the highest mountain on Earth?', 'answer': 'Mount Everest'},
    {'question': 'What is the largest desert on Earth?', 'answer': 'Antarctica'}
]

@bot.command(name='trivia')
async def trivia_command(ctx):
    question = random.choice(questions)
    await ctx.send(question['question'])

@bot.command(name='answer')
async def answer_command(ctx, answer: str):
    for question in questions:
        if answer.lower() == question['answer'].lower():
            await ctx.send('Correct!')
            return
    await ctx.send('Incorrect!')

@bot.command(name='graph2')
async def graph2_command(ctx, equation: str):
    try:
        x = np.linspace(-10, 10, 100)
        y = ast.literal_eval(equation)
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Graph of {equation}')
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        await ctx.send(file=discord.File(buf, 'graph.png'))
    except:
        await ctx.send("Sorry, I couldn't understand that expression. Please make sure it's a valid mathematical expression.")

bot.run('[redacted token]')
