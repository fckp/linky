from fastapi import Request, status
from fastapi.responses import RedirectResponse

def handle_redirect(request: Request, id):
    db = request.app.db
    url = db.get("url_"+id)
    if url is None:
        return 404
    else:
        return RedirectResponse(url)