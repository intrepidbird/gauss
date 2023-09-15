from discord_slash import SlashCommand, SlashContext

slash = SlashCommand(bot, sync_commands=True)

# Slash Command 🤔
@slash.slash(name="add",
             description="Add two numbers",
             options=[
               {
                 "name": "first",
                 "description": "The first number",
                 "type": 4,
                 "required": True
               },
               {
                 "name": "second",
                 "description": "The second number",
                 "type": 4,
                 "required": True
               }
             ])
async def _add(ctx: SlashContext, first: int, second: int):
    await ctx.send(f"The sum of {first} and {second} is {first + second}")
