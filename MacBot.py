import discord
import time
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from random import randint

mods = ["400055843787243531"]
rando = randint(1,9)
bypass_list = [""]
chat_filter = ["OOGIEPOOGIENIGGERNOGGER"]
#startup_extensions = ["Music"]
bot = commands.Bot(".")

#459871164974628886 - living room
#436290304606339073 - inkopolis plaza
#474093768774254595 - Mac's server

@bot.event
async def on_ready():
    rando
    print("Bot Online")
    await bot.change_presence(game=discord.Game(name="with Rob"))
    me = await bot.get_user_info('400055843787243531')
    await bot.send_message(me, "The bot has restarted.")#.format(ctx.message))
    #await bot.send_message(discord.Object(id='459871164974628886'), "Version 1.3.0")
   
#class Main_Commands():
    #def __init__(self, bot):
        #self.bot = bot


@bot.event
async def on_message(message):

#@bot.event
#async def on_message(message):
    #if message.content.upper().startswith('.SHUTDOWN'):
        #if message.author.id == "400055843787243531":
            #await bot.send_message(message.channel,"Goodbye Saucefam!")
        #else:
            #await bot.send_message(message.channel,"You are not Robert Jefferson.")
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await bot.delete_message(message)
                    await bot.send_message(message.channel, "Please {0.author.mention}, don't use racial slur!".format(message))
                except discord.errors.NotFound:
                    return
    
    #if message.content.upper().startswith('.REPORT'):
        #if message.author == bot.user:
            #return
        #rob = await bot.get_user_info('400055843787243531')
        #await bot.send_message(rob, "The user {0.author.mention} has reported someone".format(message))
        #henry = await bot.get_user_info('258675615194939392')
        #await bot.send_message(henry, "The user {0.author.mention} has reported someone".format(message))
        #rehan = await bot.get_user_info('310045671094747136')
        #await bot.send_message(rehan, "The user {0.author.mention} has reported someone".format(message))
        #tester = await bot.get_user_info('Tester ID')
        #await bot.send_message(tester, "The user {0.author.mention} has reported someone".format(message))
        
    if message.content.upper().startswith('.HELLO'):
        await bot.send_message(message.channel,"Hello {0.author.mention}! :wave:".format(message))
        
    if message.content.upper().startswith('.HI'):
        await bot.send_message(message.channel,"Hello {0.author.mention}! :wave:".format(message))        
        
    if message.content.upper().startswith('.BYE'):
        await bot.send_message(message.channel,"Hope to see you again soon {0.author.mention}! ;o;".format(message))
        
    if message.content.upper().startswith('.GOODBYE'):
        await bot.send_message(message.channel,"Hope to see you again soon {0.author.mention}! ;o;".format(message))

    if message.content.upper().startswith('.PING'):
        await bot.send_message(message.channel,"PONG {0.author.mention}".format(message))
        
    #if message.content.upper().startswith('.COMMANDS'):
        await bot.send_message(message.channel," .help: Shows this \n .rules : Displays the rules \n .rules(number of rule): Displays specific rules \n .yt: Link to Eddie's channel! \n .info: Shows info about the bot")
        
    if message.content.upper().startswith('.SPAM'):
        await bot.send_message(message.channel,"Initializing spam...")
        time.sleep(5)
        await bot.send_message(message.channel,"JK {0.author.mention}, please don't spam in the server!".format(message))
        
    #if message.content.upper().startswith(''):
        #await bot.send_message(message.channel,"")
#( ͡° ͜ʖ ͡°)

    await bot.process_commands(message)
    
@bot.command(pass_context=True)
async def info(ctx):
    """Information about the bot"""
    embed=discord.Embed(title="A bot based on the world's best girlfriend.", description="Functions: Loving Rob.", color=0x00FF00)
    embed.set_author(name="MacBot")
    embed.set_footer(text="Created by Robert Jefferson")
    await bot.say(embed=embed)
    print("Information accesed")
    
@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

@bot.command(pass_context = True)
async def report(ctx, *args):
    """Usage: .report (@name and cause)"""
    mesg = ' '.join(args)
    
    me = await bot.get_user_info('400055843787243531')
    await bot.send_message(me, "The user {0.author.mention} has reported: {1}".format(ctx.message, mesg))
    
    mac = await bot.get_user_info('414484144115154945')
    await bot.send_message(mac, "The user {0.author.mention} has reported: {1}".format(ctx.message, mesg))
    
    #await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def hello(ctx):
    """Salute the bot!"""

@bot.command(pass_context=True)
async def bye(ctx):
    """Say your goodbyes to the bot..."""

@bot.command(pass_context=True)
async def spam(ctx):
    """A naughty command."""
    
@bot.command(pass_context=True)
async def ping(ctx):
    """PONG"""
    
@bot.command(pass_context=True)
async def rape(ctx, *args):
    """Rape someone"""
    mesg = ' '.join(args)
    #return await bot.say(mesg)"The user {0.author.mention} has reported: {1}".format(ctx.message, mesg)
    return await bot.say("{0.author.mention} has raped: {1}".format(ctx.message, mesg))
    



#if __name__ == "__main__":
        #for extension in startup_extensions:
            #try:
                #bot.load_extension(extension)
            #except Exception as e:
                #exc = '(): ()'.format(type(e).__name__, e)
#print('Failed to load extension ()\n()'.format(extension, exc))

bot.run("NDg4MjIyNzIwMTgyNDUyMjcy.DnZFvQ.oFV6Xq_Nl3QLD13tncwgu_zw8Lg")
#code ends here
