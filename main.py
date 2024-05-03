import os
from discord.ext import commands
import discord
import requests
import shutil
from dotenv import load_dotenv

load_dotenv()
from pprint import pprint


token = os.getenv("TOKEN")

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="T ", intents=intents)


@client.event
async def on_ready():
    print("ready")


@client.command()
async def helpp(ctx):

    await ctx.channel.send(
        "Use the command 'T add <Origin city> <Destination city> <Number of People> <Number of days>' enter theneeded values without the symbol '<>'"
    )


# T add <Origin city> <Destination city> <Number of People> <Number of days>
# http://127.0.0.1:8080
@client.command()
async def add(ctx):
    await ctx.message.channel.send("Hold on our AI is generating an itineray for you.")
    use = ctx.message.content.split()
    print(use)
    """    origin = request.form.get("origin")
    desti = request.form.get("desti")
    num_peo = request.form.get("num_peo")
    num_days = request.form.get("num_days")"""
    info = {"origin": use[2], "desti": use[3], "num_peo": use[4], "num_days": use[5]}

    res = requests.post("http://127.0.0.1:8080/plan", data=info)
    print(res.json()["message"])
    await ctx.channel.send(res.json()["message"])
    pl = {"place": res.json()["places"]}
    pprint(res.json()["places"])
    imgg = requests.post("http://127.0.0.1:8080/places", data=pl)
    pprint(imgg.json()["images"])

    for linkk in imgg.json()["images"]:
        await ctx.channel.send(linkk)


client.run(token)
