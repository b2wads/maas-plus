import os

import asyncworker
from aiohttp import web
from aiohttp.test_utils import TestServer, TestClient
from asynctest import TestCase


class BaseApiTestCase(TestCase):
    async def aiohttp_client(self, app: asyncworker.App) -> TestClient:
        routes = app.routes_registry.http_routes
        http_app = web.Application()
        for route in routes:
            http_app.router.add_route(**route)
        self.server = TestServer(
            http_app, port=os.environ["TEST_ASYNCWORKER_HTTP_PORT"]
        )
        client = TestClient(self.server)
        await self.server.start_server()

        return client

    async def tearDown(self):
        if hasattr(self, "server"):
            await self.server.close()
