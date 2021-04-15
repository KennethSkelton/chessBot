# chessBot.py 
import os

import discord
import urllib.request

import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message): 
    
    if message.author == client.user:
        return

    print("Seen")
    if '!fen' in message.content.lower():
        print("Respond")
        rawMessage = message.content
        fen = rawMessage[rawMessage.find("(")+1 : rawMessage.find(")")]

        if "w" in fen:
            urlAddon = fen[:(fen.find(" w"))]
        else:
            
            urlAddon = fen[:(fen.find(" b"))]

        url = "https://chessboardimage.com/"+urlAddon+".png"

        imageFilename = urlAddon.replace("/","")

        urllib.request.urlretrieve(url, "/Users/kenneth/Desktop/Homework Stevens/Personal Projects/chessBot/fens/"+imageFilename+".png")
        await message.channel.send(file=discord.File('/Users/kenneth/Desktop/Homework Stevens/Personal Projects/chessBot/fens/'+imageFilename+'.png'))
            
        board = chess.Board(fen)
        
        info = engine.analyse(board, chess.engine.Limit(depth=18))



        centipawnScore = str(info["score"].white().score())
        
        centipawnScore = centipawnScore[:-2] + "."+centipawnScore[-2:]
        scoreInfo = "Stockfish 12 evaluates this position as: " + centipawnScore

        await message.channel.send(scoreInfo)

        await message.channel.send(fen)
        
client.run("ODA4ODE3MjEyMjMxOTA5Mzc2.YCMDug.fZB49Vjs2caM4kSlDN2EjobFngc")