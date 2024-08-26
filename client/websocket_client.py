# Filename: client/websocket_client.py

# Filename: server/websocket_server.py



import asyncio
import websockets
import json

async def send_move():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        move = input("Enter your move: ")
        data = json.dumps({
            "player": "A",
            "move": move
        })
        await websocket.send(data)
        response = await websocket.recv()
        print(response)

asyncio.get_event_loop().run_until_complete(send_move())
