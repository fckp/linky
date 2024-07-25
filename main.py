from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from router import router

from valkey import Valkey

import os

vk_host = os.environ.get("VK_HOST", "localhost")
vk_port = os.environ.get("VK_PORT", 6379)
vk_db = os.environ.get("VK_DB", 0)

access_password = os.environ.get("ACCESS_PASSWORD", "links.pnlt.pw")

app = FastAPI()
app.db = Valkey(vk_host, vk_port, vk_db, decode_responses=True)

app.db.set("________________________________ACCESSPW", access_password)

app.include_router(router)

static_files = StaticFiles(directory="frontend/static")
app.mount("/static", static_files, name="static")