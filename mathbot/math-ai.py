import wolframalpha

client = wolframalpha.Client('client-id')

@bot.command(name='ask')
async def ask(ctx, *, question: str):
    res = client.query(question)
    if res['@success'] == 'false':
        await ctx.send('I could not find an answer to your question.')
    else:
        answer = next(res.results).text
        await ctx.send(f'The answer to your question is: {answer}')

# Wolfram Alpha API
