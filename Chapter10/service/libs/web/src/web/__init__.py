from sanic import Sanic
from sanic.exceptions import NotFound

from .view import View

app = Sanic("delivery_status")


def register_route(view_object, route):
    app.add_route(view_object.as_view(), route)


__all__ = ["View", "app", "register_route"]
