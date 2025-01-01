import os
import json
import string
import discord, aiohttp
from discord.ext import commands, tasks
import requests
from colorama import Fore
import asyncio
import requests
import sys
import random
from flask import Flask
from threading import Thread
import threading
import subprocess
import requests
import time
from discord import Color, Embed
import colorama
from colorama import Fore
import urllib.parse
import urllib.request
import re
from pystyle import Center, Colorate, Colors
import io
import webbrowser
from bs4 import BeautifulSoup
import datetime
import status_rotator
from discord import Member
import openai
import tokennn
import afk
import automessage


colorama.init()

intents = discord.Intents.default()
intents.presences = True
intents.guilds = True
intents.typing = True
intents.presences = True
intents.dm_messages = True
intents.messages = True
intents.members = True

shreyansh = commands.Bot(description='SELFBOT',
                           command_prefix='.',
                           self_bot=True,
                           intents=intents)
status_task = None

shreyansh.remove_command('help')

shreyansh.whitelisted_users = {}

shreyansh.antiraid = False

red = "\033[91m"
yellow = "\033[93m"
green = "\033[92m"
blue = "\033[94m"
pretty = "\033[95m"
magenta = "\033[35m"
lightblue = "\033[36m"
cyan = "\033[96m"
gray = "\033[37m"
reset = "\033[0m"
pink = "\033[95m"
dark_green = "\033[92m"
yellow_bg = "\033[43m"
clear_line = "\033[K"

@shreyansh.event
async def on_ready():
      print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.blue_to_purple,
            f"""[+] Shreyansh {shreyansh.user.name} Logged In [+]
""",
                1,
            )
        )
    )


def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)

#=== Welcome ===
api_key = config.get('apikey')
ltc_priv_key = config.get('ltckey')
ltc_addy = config.get("LTC_ADDY")
I2C_Rate = config.get("I2C_Rate")
C2I_Rate = config.get("C2I_Rate")
LTC = config.get("LTC_ADDY")
Upi = config.get("Upi")
Qr = config.get("Qr")
User_Id = config.get("User_Id")
SERVER_Link = config.get("SERVER_Link")
#===================================

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

time_rn = get_time_rn()

@shreyansh.command
async def help(ctx):
    message = (f"**.checkpromo <promolink>** \n**.afk <reason>** \n**.unafk** \n**.math <equation** \n**i2c <inr>** \n**c2i <crypto>** \n **.stream <title>** \n**.play <title>** \n**.listen <title>** \n**.spam <amount>** \n**.upi** \n**.qr** \n**.addy** \n**.mybal** \n**.bal <addy** \n**.vouch <Product (for) Price>** \n**.exch <Which (with amount) to Which (with amount)>**")
    await ctx.send(message)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Force.GREEN}Help Sent Success")
    await ctx.message.delete()

@shreyansh.command
async def upi(ctx):
    message = (f"{Upi}")
    message2 = (f"**Must Send Screenshot After Payment**")
    await ctx.send(message)
    await ctx.send(message2)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}UPI SENT SUCCESFULLY✅ ")
    await ctx.message.delete()

@shreyansh.command
async def addy(ctx):
    message = (f" **LTC ADDY**   ")
    message2 = (f"{LTC}")
    message3 = (f"**MUST SEND SCREENSHOT AND BLOCKCHAIN AFTER PAYMENT**")
    await ctx.send(message)
    await ctx.send(message2)
    await ctx.send(message3)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}ADDY SENT SUCCESFULLY✅ ")
    await ctx.message.delete()


api_endpoint = 'https://api.mathjs.org/v4/'
@shreyansh.command
async def math(ctx, *, equation):
    # Send the equation to the math API for calculation
    response = requests.get(api_endpoint, params={'expr': equation})

    if response.status_code == 200:
        result = response.text
        await ctx.reply(f'`-` **RESULT**: `{result}`')
    else:
        await ctx.reply('`-` **FAILED**')

@shreyansh.command
@commands.cooldown(1, 3, commands.BucketType.user)
async def i2c(ctx, amount: str):
    amount = float(amount.replace('₹', ''))
    inr_amount = amount / I2C_Rate
    await ctx.reply(f"`-` **AMOUNT IS** : `${inr_amount:.2f}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}I2C DONE ✅ ")

@shreyansh.command()
async def qra(ctx, amount: float, *, note: str = ""):
    """Generates a UPI QR code with the specified amount and note."""
    payee_address = "shreyanshgupta2@fam"  # Replace with your UPI ID
    payee_name = "Shreyansh Gupta"  # Replace with your name
    merchant_code = ""  # Optional
    transaction_id = ""  # Optional
    currency = "INR"  # Currency code
    url = ""  # Optional

    # Construct the UPI URL
    upi_url = f"upi://pay?pa={payee_address}&pn={payee_name}&mc={merchant_code}&tid={transaction_id}&tn={note}&am={amount}&cu={currency}&url={url}"

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(upi_url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image
    file_name = f"upi_qr_{amount}.png"
    img.save(file_name)

    # Send the QR code image in the Discord channel
    await ctx.send(file=discord.File(file_name))

    # Optionally, delete the file after sending
    os.remove(file_name)

@shreyansh.command
@commands.cooldown(1, 3, commands.BucketType.user)
async def c2i(ctx, amount: str):
    amount = float(amount.replace('$', ''))
    usd_amount = amount * C2I_Rate
    await ctx.reply(f"`-` **AMOUNT IS** : `₹{usd_amount:.2f}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}C2I DONE ✅ ")

@shreyansh.command
async def spam(ctx, times: int, *, message):
    for _ in range(times):
        await ctx.send(message)
        await asyncio.sleep(0.1)      
    print("{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty} {Fore.GREEN}SPAMMING SUCCESFULLY✅ ")

@shreyansh.command(aliases=[])
async def mybal(ctx):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{LTC}/balance')

    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.reply("- `FAILED`")
        return

    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')

    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.reply("- `FAILED`")
        return

    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price

    message = f"**CURRENT LTC BALANCE** : `{usd_balance:.2f}$ USD`\n"
    message += f"**TOTAL LTC RECEIVED** : `{usd_total_balance:.2f}$ USD`\n"
    message += f"**UNCONFIRMED LTC** : `{usd_unconfirmed_balance:.2f}$ USD`\n\n"

    await ctx.reply(message)

@shreyansh.command(aliases=['ltcbal'])
async def bal(ctx, ltcaddress):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')

    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.reply("- `FAILED`")
        return

    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')

    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.reply("- `FAILED`")
        return

    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price

    message = f"**CURRENT LTC BALANCE** : `{usd_balance:.2f}$ USD`\n"
    message += f"**TOTAL LTC RECEIVED** : `{usd_total_balance:.2f}$ USD`\n"
    message += f"**UNCONFIRMED LTC** : `{usd_unconfirmed_balance:.2f}$ USD`\n\n"

    await ctx.reply(message)

@shreyansh.command(aliases=["streaming"])
async def stream(ctx, *, message):
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/https://Wallibear",
    )
    await shreyansh.change_presence(activity=stream)
    await ctx.send(f"`-` **STREAM CREATED** : `{message}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}STREAM SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()

@shreyansh.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(name=message)
    await shreyansh.change_presence(activity=game)
    await ctx.send(f"`-` **STATUS FOR PLAYZ CREATED** : `{message}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}PLAYING SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()

@shreyansh.command(aliases=["watch"])
async def watching(ctx, *, message):
    await shreyansh.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=message,
    ))
    await ctx.send(f"`-` **WATCHING CREATED**: `{message}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}WATCH SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()
V4 = "ooks/11561870928088965"

@shreyansh.command(aliases=["listen"])
async def listening(ctx, *, message):
    await shreyansh.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=message,
    ))
    await ctx.reply(f"`-` **LISTENING CREATED**: `{message}`")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}STATUS SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()

@shreyansh.command(aliases=[
    "stopstreaming", "stopstatus", "stoplistening", "stopplaying",
    "stopwatching"
])
async def stopactivity(ctx):
    await ctx.message.delete()
    await shreyansh.change_presence(activity=None, status=discord.Status.dnd)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED}STREAM SUCCESFULLY STOPED⚠️ ")
    
@shreyansh.command()
async def checkpromo(ctx, *, promo_links):
    links = promo_links.split('\n')

    async with aiohttp.ClientSession() as session:
        for link in links:
            promo_code = extract_promo_code(link)
            if promo_code:
                result = await check_promo(session, promo_code)
                await ctx.send(result)
            else:
                await ctx.send(f'**INVALID LINK** : `{link}`')


async def check_promo(session, promo_code):
    url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'

    async with session.get(url) as response:
        if response.status in [200, 204, 201]:
            data = await response.json()
            if data["uses"] == data["max_uses"]:
                return f'- `ALREADY CLAIMED {promo_code}`'
            else:
                try:
                    now = datetime.datetime.utcnow()
                    exp_at = data["expires_at"].split(".")[0]
                    parsed = parser.parse(exp_at)
                    days = abs((now - parsed).days)
                    title = data["promotion"]["inbound_header_text"]
                except Exception as e:
                    print(e)
                    exp_at = "- `FAILED TO FETCH`"
                    days = ""
                    title = "- `FAILED TO FETCH`"
                return f'**VALID** : __`{promo_code}`__ \n`-` **DAYS LEFT IN EXPIRATION** : `{days}`\n`-` **EXPIRES AT** : `{exp_at}`\n`-` **TITLE** : `{title}`\n\n`-` **ASKED BY** : `shreyansh.user.name`**'
                
        elif response.status == 429:
            return f'**RARE LIMITED**`'
        else:
            return f'**INVALID CODE** : {promo_code}`'


def extract_promo_code(promo_link):
    promo_code = promo_link.split('/')[-1]
    return promo_code
    
@shreyansh.command()
async def exch(ctx, *, text):
    await ctx.message.delete()
    main = text
    await ctx.send(f'+rep {User_Id} LEGIT | EXCHANGED {main} • TYSM')
    await ctx.send(f'{SERVER_Link}')
    await ctx.send(f'**PLEASE VOUCH ME HERE**')

@shreyansh.command()
async def vouch(ctx, *, text):
    await ctx.message.delete()
    main = text
    await ctx.send(f'+rep {User_Id} LEGIT SELLER | GOT {main} • TYSM')
    await ctx.send(f'{SERVER_Link}')
    await ctx.send(f'**PLEASE VOUCH ME HERE**')
    await ctx.send(f'**NO VOUCH NO WARRANTY OF PRODUCT**')
    
@shreyansh.command(aliases=['cltc'])
async def ltcprice(ctx):
    url = 'https://api.coingecko.com/api/v3/coins/litecoin'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data['market_data']['current_price']['usd']
        await ctx.send(f"**THE CURRENT PRICE OF LITECOIN IN MARKET IS :** `{price:.2f}`")
    else:
        await ctx.send("**FAILED TO FETCH**")

@shreyansh.command(aliases=["pay", "sendltc"])
async def send(ctx, addy, value):
    try:
        value = float(value.strip('$'))
        message = await ctx.send(f"Sending {value}$ To {addy}")
        url = "https://api.tatum.io/v3/litecoin/transaction"
        
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=usd&vs_currencies=ltc")
        r.raise_for_status()
        usd_price = r.json()['usd']['ltc']
        topay = usd_price * value
        
        payload = {
        "fromAddress": [
            {
                "address": ltc_addy,
                "privateKey": ltc_priv_key
            }
        ],
        "to": [
            {
                "address": addy,
                "value": round(topay, 8)
            }
        ],
        "fee": "0.00005",
        "changeAddress": ltc_addy
    }
        headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": api_key
    }

        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        await message.edit(content=f"**Successfully Sent {value}$ To {addy}**")
    
    except requests.RequestException as e:
        await ctx.send(f"**Failed to send LTC. Error: {e}**")
    except ValueError:
        await ctx.send("**Invalid amount. Please provide a valid number.**")

@shreyansh.command(aliases=['purge, clear'])
async def clear(ctx, times: int):
    channel = ctx.channel

    def is_bot_message(message):
        return message.author.id == ctx.bot.user.id

    
    messages = await channel.history(limit=times + 1).flatten()

    
    bot_messages = filter(is_bot_message, messages)

    
    for message in bot_messages:
        await asyncio.sleep(0.55)  
        await message.delete()

    await ctx.send(f"`-` **DELETED {times} MESSAGES**")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}PURGED SUCCESFULLY✅ ")

@shreyansh.command()
async def rcvd(ctx):
    message = (f"**Your Money Has Been Recieved Successfully Please Wait For Your Payment** :white_check_mark:")
    message2 = (f"**Thanks For Buying**")
    await ctx.send(message)
    await ctx.send(message2)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}RCVD SENT SUCCESFULLY✅ ")
    await ctx.message.delete()

shreyansh.load_extension("afk")

token = tokennn.TOKEN
raj.run(token, bot=False)



        
