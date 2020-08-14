import asyncio
import random


import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix='>')


@client.event
async def on_ready() :
    print('Bot is ready.')
    print('MC Weekly')
    change_status.start()

def check_if_it_is_me(ctx) :
    return ctx.message.author.id == 470261090798796800

@tasks.loop(seconds=25)
async def change_status() :
    await client.change_presence(activity=discord.Game(name="MC Weekly!"))
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Game(name="Coded By Tic#0001"))
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Game(name="play.titaniumgames.ga:8989"))
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Game(name="alecdev.cf"))
    await asyncio.sleep(10)

@client.command()
async def invite(ctx) :
    await ctx.send('Here\'s your invite!\nhttps://discord.com/api/oauth2/authorize?client_id=735205103879061534&permissions=8&scope=bot')
   

@client.command(aliases=['nexttournament','nt','next.tournament','next_Tournament','NEXT_TOURNAMENT'])
#
async def next_tournament(ctx) :
  
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title='Next Tournament',
        description='___________',
        timestamp=ctx.message.created_at
    )

    embed.set_author(name="Minecraft Weekly", icon_url="https://3dwarehouse.sketchup.com/warehouse/v1.0/publiccontent/8ae1e915-94ec-4c0b-b8c7-1f18095e814e")
    embed.add_field(name="Extreme Camoflage Hide And Seek ", value="Friday 14th of August, 6:15 BST", inline=False)
    embed.add_field(name="Wool Shuffle", value="Monday 17th of August, 6:15 BST", inline=False)
    embed.set_footer(text=f"Made by Tic. | {client.user.name} | alecdev.cf")

    await ctx.send(embed=embed)


@client.command(aliases=['win','winne','winner','WINNERS'])
#
async def winners(ctx) :
  
    embed = discord.Embed(
        colour=discord.Colour.blue(),
        title='Winners',
        description='___________',
        timestamp=ctx.message.created_at
    )

    embed.set_author(name="Minecraft Weekly", icon_url="https://3dwarehouse.sketchup.com/warehouse/v1.0/publiccontent/8ae1e915-94ec-4c0b-b8c7-1f18095e814e")
    embed.add_field(name="Floor is lava ", value="Lightning Hero", inline=False)
    embed.add_field(name="Bedwars Tourney - Retake", value="Tillage & MegaGardevoir", inline=False)
    embed.set_footer(text=f"Made by Tic. | {client.user.name} | alecdev.cf")

    await ctx.send(embed=embed)


@client.command(pass_context=True)
@commands.has_any_role('Owners','Developer','CommandTesterPerms')
async def echo(ctx, *, message: str):
    await ctx.channel.purge(limit=1)
    await ctx.send(message)



@client.command()
@commands.check(check_if_it_is_me)
async def logout(ctx) :
    await ctx.send(':arrows_counterclockwise: Logging bot off.')
    await client.close()




client.run('token')
