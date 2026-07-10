#!/usr/bin/env python3


from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.staticfiles import StaticFiles


async def homepage(request):
    with open("index.html") as f:
        html_content = f.read()
    html_response = HTMLResponse(content=html_content, status_code=200)
    return html_response

async def websocket_endpoint(websocket):
    await websocket.accept()
    while True:
        message = await websocket.receive_text()
        return_message = f"{message}"
        await websocket.send_text(return_message)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
app.mount("/static", StaticFiles(directory="static"), name="static")