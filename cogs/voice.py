from discord.ext import commands
import discord

class Voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel):
        """Joins a voice channel"""

        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)

        await channel.connect()

    @commands.command()
    async def play(self, ctx, *, query):
        """Plays a file from the local filesystem"""

        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(query))
        ctx.voice_client.play(source, after=lambda e: print(f"Player error: {e}") if e else None)

        await ctx.send(f"Now playing: {query}")
    
    @commands.command()
    async def disconnect(self, ctx):
        """Disconnects the bot from voice channel"""
        await ctx.voice_client.disconnect()

    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send('You are not connected to a voice channel.')
                raise commands.CommandError('Author not connected to a voice channel')
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()
