"""View helper Objects"""
from sanic.response import json
from sanic.views import HTTPMethodView


class View(HTTPMethodView):
    """Extend with the logic of the application"""

    async def get(self, request, *args, **kwargs):
        response = await self._get(request, *args, **kwargs)
        return json(response)
