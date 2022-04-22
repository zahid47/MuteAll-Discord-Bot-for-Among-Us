async def show_common_error(ctx, e):
    await ctx.send(f"Something went wrong ({e})", value="[Join support server](https://discord.gg/8hrhffR6aX) for help.")


async def show_permission_error(ctx):
    await ctx.send("Make sure I have the necessary permissions. If unsure, try giving me the 'administrator' permission or [Join support server](https://discord.gg/8hrhffR6aX)")
