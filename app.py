"""
Application definition
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
async def home():
    return HTMLResponse("Hello world!")


@app.post("/callback_test")
async def callback_test(request: Request):
    body = await request.body()
    return {
        'success': True,
        'requestBody': body
    }
