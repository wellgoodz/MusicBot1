from discord.ext import commands

client = commands.Bot(command_prefix="!")
player_dict = dict()


@client.event
async def on_ready():
    print("Bot is ready")


@client.command(pass_context=True)
async def play(ctx, url):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice = client.voice_client_in(server)
    player = await voice.create_ytdl_player(url)
    player_dict[server.id] = player
    player.start()

@client.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.stop()
    del player_dict[server.id]
client.run("NTYzNDUyMzQxODU3MTU3MTMw.XKZiRg.5SEWc5NFgxqHAt9HD2tRkHiewvU")
