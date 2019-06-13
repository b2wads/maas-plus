from asynctest import skip

from maas.app import app
from tests.base import BaseApiTestCase


class OperationTest(BaseApiTestCase):
    async def setUp(self):
        self.client = await self.aiohttp_client(app)

    async def tearDown(self):
        await super(OperationTest, self).tearDown()

    async def test_operation_endpoint(self):
        result = await self.client.post("/", json={"left": 10, "right": 10})
        self.assertEqual(200, result.status)
        data = await result.json()
        self.assertEqual({}, data)
