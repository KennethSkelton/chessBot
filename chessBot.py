''' chess_bot.py '''
import os
import urllib.request
from dotenv import load_dotenv

import discord

import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    '''executes when the client first starts up'''
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    '''executes when someone sends a message in chat'''
    if message.author == client.user:
        return

    print("Seen")
    if '!fen' in message.content.lower():
        print("Respond")
        raw_message = message.content
        fen = raw_message[raw_message.find("(")+1: raw_message.find(")")]

        if "w" in fen:
            url_addon = fen[:(fen.find(" w"))]
        else:
            url_addon = fen[:(fen.find(" b"))]

        url = "https://chessboardimage.com/"+url_addon+".png"

        image_filename = url_addon.replace("/", "")

        temp = "/Users/kenneth/Desktop/Homework Stevens"
        path = temp+"/Personal Projects/chessBot/fens/"
        urllib.request.urlretrieve(url, path+image_filename+".png")

        await message.channel.send(
            file=discord.File(path+image_filename+'.png'))

        board = chess.Board(fen)

        info = engine.analyse(board, chess.engine.Limit(depth=18))

        centipawn_score = str(info["score"].white().score())

        centipawn_score = centipawn_score[:-2] + "."+centipawn_score[-2:]
        msg = "Stockfish 12 evaluates this position as: "
        score_info = msg + centipawn_score

        await message.channel.send(score_info)

        await message.channel.send(fen)

client.run("ODA4ODE3MjEyMjMxOTA5Mzc2.YCMDug.fZB49Vjs2caM4kSlDN2EjobFngc")
