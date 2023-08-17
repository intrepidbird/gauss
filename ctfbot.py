import discord
from sympy import mod_inverse
import random

intents = discord.Intents.default()
client = discord.Client(intents=intents)
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!rsa'):
        args = message.content.split()[1:]
        if len(args) == 3:
            n, e, phi = map(int, args)
            d = mod_inverse(e, phi)
            await message.channel.send(f'd: {d}')
        elif len(args) == 2:
            n, d = map(int, args)
            await message.channel.send('Not enough information to solve RSA')
        elif len(args) == 3:
            p, q, d = map(int, args)
            n = p * q
            phi = (p - 1) * (q - 1)
            e = mod_inverse(d, phi)
            await message.channel.send(f'n: {n}, e: {e}')
        elif len(args) == 4:
            p, q, e, phi = map(int, args)
            n = p * q
            d = mod_inverse(e, phi)
            await message.channel.send(f'n: {n}, d: {d}')
        elif len(args) == 1:
            n = int(args[0])
            e = 65537
            # factorize n to find p and q
            # calculate phi using p and q
            # calculate d using e and phi
            await message.channel.send('Not implemented yet')

    if message.content.startswith('!caesar'):
        method = message.content.split()[1:]
        text = message.content.split()[2:]
        key = message.content.split()[3:]
        translation = ''

        for symbol in text:
            if symbol in symbols:
                symbolIndex = symbols.find(symbol)
                if method == 'encrypt':
                    translateIndex = symbolIndex + key
                elif method == 'decrypt':
                    translateIndex = symbolIndex - key

                if translateIndex >= len(symbols):
                    translateIndex = translateIndex - len(symbols)
                elif translateIndex < 0:
                    translateIndex = translateIndex + len(symbols)

                translation = translation + symbols[translateIndex]
            else:
                translation = translation + symbol



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!iq'):
        name = message.author.name
        if name[0].lower() in ['a', 't']:
            iq = random.randint(300, 500)
        else:
            iq = 100
        await message.channel.send(f'Your IQ is: {iq}')

client.run('[redacted token]')
