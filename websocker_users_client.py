import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Здравствуйте, сервер!"
        await websocket.send(message)  # Отправляем сообщение

        for _ in range(5):
            message = await websocket.recv()
            print(message)


asyncio.run(client())
