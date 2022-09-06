import asyncio
import websockets
import json

orangeScore = {}
blueScore = {}

players = {'Ron, your worst nightmare_1': {}, 'Tommy_6': {}, 'Yurizan_5': {}, '✪ loftzu_2': {}}
async def sosLogger():
	async with websockets.connect("ws://localhost:49122", ping_timeout = 9999) as websocket:
		#await websocket.send("Hello world!")
		frame = 0
		while frame < 9328:
			rawChunk = json.loads(await websocket.recv())["data"]
			if "players" in rawChunk:
				#print("Valid Chunk")
				rawPlayers = rawChunk["players"]
				rawGame = rawChunk["game"]
				time = rawGame["elapsed"]
				frame = rawGame["frame"]

				rOrangeScore = rawGame["teams"][0]["score"]
				if rOrangeScore not in orangeScore:
					print(f"{rOrangeScore} : {[time, frame]}")
					orangeScore[rOrangeScore] = [time, frame]
				rBlueScore = rawGame["teams"][1]["score"]
				if rBlueScore not in blueScore:
					print(f"{rBlueScore} : {[time, frame]}")
					blueScore[rBlueScore] = [time, frame]

				for player in rawPlayers:
					players[player][frame] = [time, rawPlayers[player]["score"], rawPlayers[player]["goals"], rawPlayers[player]["saves"], rawPlayers[player]["shots"], rawPlayers[player]["boost"]]
					print(f'{player} {frame} : {[time, rawPlayers[player]["score"], rawPlayers[player]["goals"], rawPlayers[player]["saves"], rawPlayers[player]["shots"], rawPlayers[player]["boost"]]}')
			#await asyncio.sleep(0.2)
asyncio.run(sosLogger())

with open("outputFile.txt", "w") as outputFile:
	outputFile.write(str(orangeScore))
	outputFile.write("\n")
	outputFile.write(str(blueScore))
	outputFile.write("\n")
	outputFile.write(str(players).replace("✪", ""))
















"""import asyncio
import websockets

async def hello(websocket, path):
	print("anything")
	name = await websocket.recv()
	print("< {}".format(name))

	greeting = "Hello {}!".format(name)
	#await websocket.send(greeting)
	print("> {}".format(greeting))

start_server = websockets.serve(hello, '', 49322)
print("anything 1")
asyncio.get_event_loop().run_until_complete(start_server)
print("anything 2")
asyncio.get_event_loop().run_forever()"""
"""import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)

PORT = 49122        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

	s.bind((HOST, PORT))

	s.listen()

	conn, addr = s.accept()

	with conn:
		print('Connected by', addr)

while True:
	data = conn.recv(1024)
	if not data:
		break
	conn.sendall(data)"""
