from aiohttp import ClientSession
from aiohttp.client import ClientTimeout

from maas.conf import settings

default_http_client_timeout = ClientTimeout(total=5, connect=5)


class MathClient:
    def __init__(self):
        self.session = ClientSession(timeout=default_http_client_timeout)

    async def _call_service(self, url, left, right):
        resp = await self.session.post(url, json={"left": left, "right": right})
        return await resp.json()

    async def plus(self, left, right):
        return await self._call_service(
            settings.PLUS_SERVICE_ADDRESS, left, right
        )

    async def minus(self, left, right):
        return await self._call_service(
            settings.MINUS_SERVICE_ADDRESS, left, right
        )

    async def multiply(self, left, right):
        return await self._call_service(
            settings.MULTIPLY_SERVICE_ADDRESS, left, right
        )

    async def divide(self, left, right):
        return await self._call_service(
            settings.DIVIDE_SERVICE_ADDRESS, left, right
        )

    async def power(self, left, right):
        return await self._call_service(
            settings.POWER_SERVICE_ADDRESS, left, right
        )
