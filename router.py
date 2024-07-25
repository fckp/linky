from fastapi.routing import APIRouter

from api import handle_new_url, handle_delete_url
from redirect import handle_redirect
from frontend import index, manage

router = APIRouter()

router.add_api_route("/api/url/{id}", handle_delete_url, methods=["DELETE"])
router.add_api_route("/api/url", handle_new_url, methods=["POST"])
router.add_api_route("/manage", manage, methods=["GET", "POST"], include_in_schema=False)
router.add_api_route("/{id}", handle_redirect, include_in_schema=False)
router.add_api_route("/", index, include_in_schema=False)

if __name__ == "__main__":
    raise Exception("this module was never meant to be executed outside of dependency")