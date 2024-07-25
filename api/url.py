from fastapi import Request, status
from fastapi.responses import JSONResponse
from valkey import Valkey


from utils import gen_str

async def handle_new_url(request: Request):
    async with request.form() as form:
        id, redir_to = form.get("id"), form.get("redir_to")
        if redir_to is None:
            return JSONResponse("redir_to is nonexistent", status.HTTP_400_BAD_REQUEST)
        redir_to = redir_to.lstrip().rstrip()
        if id is None or len(id) <= 0:
            id = gen_str(8)
        if request.app.db.exists("url_"+id) > 0:
            return JSONResponse("this id already exists", status.HTTP_400_BAD_REQUEST)
        if request.app.db.set("url_"+id, redir_to):
            result = {
                'id': id,
                'url': redir_to
            }
    return result

async def handle_delete_url(request: Request, id):
    db: Valkey = request.app.db
    if db.exists("url_"+id) > 0:
        db.delete("url_"+id)
    return 200