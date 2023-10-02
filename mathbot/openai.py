import openai

@bot.command()
async def ai(ctx, *, prompt):
    openai.api_key = 'openai_key'
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
    await ctx.send(response.choices[0].text.strip())
