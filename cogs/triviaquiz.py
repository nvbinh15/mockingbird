import random
import asyncio
import requests
import json
from discord.ext import commands
import discord

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

class Quiz(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def on_message(self, message):
    #     # we do not want the bot to reply to itself
    #     if message.author.id == self.user.id:
    #         return

    #     if message.content.startswith('$task'):
    #         await message.channel.send('Answer True or False to turn off annoying sound:')
    #         response = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")
    #         jprint(response.json())
    #         result = response.json()['results']
    #         print(result)
    #         question = result[0]['question']
    #         question = question.replace("&quot;", "'")
    #         answer = result[0]['correct_answer']
    #         print(question)
    #         await message.channel.send(question)

    #         def is_correct(m):
    #             return m.author == message.author

    #         try:
    #             guess = await self.wait_for('message', check=is_correct, timeout=10.0)
    #         except asyncio.TimeoutError:
    #             return await message.channel.send('Sorry, you took too long it was {}.'.format(answer))

    #         if guess.content.lower() == answer.lower():
    #             await message.channel.send('You are right!')
    #         else:
    #             await message.channel.send('Oops. It is actually {}.'.format(answer))

    @commands.command()
    async def quiz(self, ctx):
        await ctx.send('Answer True or False:')
        response = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")
        jprint(response.json())
        result = response.json()['results']
        print(result)
        question = result[0]['question']
        question = question.replace("&quot;", "'")
        question = question.replace("&#039;", "'")
        answer = result[0]['correct_answer']
        print(question)
        await ctx.send(question)

        try:
            guess = await self.bot.wait_for('message', timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send('Sorry, you took too long it was {}.'.format(answer))

        if guess.content.lower() == answer.lower():
            await ctx.send('You are right!')
        else:
            await ctx.send('Oops. It is actually {}.'.format(answer))

##ADD MORE FEATURES TO THE ANSWERS