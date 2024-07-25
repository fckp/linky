from fastapi import Request, status
from fastapi.responses import HTMLResponse, RedirectResponse

from fastapi.templating import Jinja2Templates

from valkey import Valkey

templates = Jinja2Templates("frontend/templates", auto_reload=True)


def empty_response():
    return HTMLResponse("")

def index(request: Request):
    return templates.TemplateResponse(request, "index.html")

async def manage(request: Request):
    async with request.form() as form:
        access_pw = form.get("password")
        if access_pw is None:
            return templates.TemplateResponse(request, "manage_auth.html")
        if access_pw != request.app.db.get("________________________________ACCESSPW"):
            return RedirectResponse("/", status.HTTP_403_FORBIDDEN)
    db: Valkey = request.app.db
    def get_info_from_key(key):
        return {
            "id": key.replace('url_', '', 1),
            "url": db.get(key)
        }
    urls = db.keys("url_*")
    urls = list(map(get_info_from_key, urls))
    print(urls)
    return templates.TemplateResponse(request, "manage.html", {
        "links": urls
    })