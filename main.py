#!/usr/bin/env python
from re import sub
import subprocess
from starlette import applications, responses
from starlette import routing
import datetime

async def home(request):
    return responses.FileResponse('index.html')

async def websocketEndpoint(websocket):
    await websocket.accept()
    myprocess = subprocess.Popen('./sub.py', stdout=subprocess.PIPE, text=True)
    i = 0
    while i < 25:
        time = datetime.datetime.now().strftime("%H:%M:%S:%f")
        line = f"[{time}] {myprocess.stdout.readline()}"
        print(line)
        await websocket.send_text(line)
        i += 1
    myprocess.stdout.close()
    await websocket.close()

routes = [
    routing.Route('/', home),
    routing.WebSocketRoute('/ws', websocketEndpoint)
]

app = applications.Starlette(True, routes=routes)
