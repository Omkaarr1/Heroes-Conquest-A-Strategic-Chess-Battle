# Filename: server/main.py

from .websocket_server import WebSocketServer

if __name__ == "__main__":
    server = WebSocketServer()
    server.start()
