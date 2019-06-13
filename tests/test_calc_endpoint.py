import json

from aioresponses import aioresponses, CallbackResult
from asynctest import mock

from maas.calc.app import app
from tests.base import BaseApiTestCase
from tests.util import (
    plus_service_callback,
    minus_service_callback,
    multiply_service_callback,
    divide_service_callback,
    power_service_callback,
)


class CalcEndpointTest(BaseApiTestCase):
    async def setUp(self):
        self.client = await self.aiohttp_client(app)

    async def tearDown(self):
        await super(CalcEndpointTest, self).tearDown()

    async def test_invalid_expression(self):
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            result = await self.client.post(
                "/eval", json={"expr": "1 + 1 --+="}
            )
            self.assertEqual(result.status, 400)
            data = await result.json()
            self.assertEqual(
                data,
                {
                    "result": None,
                    "error": {"exc": mock.ANY, "reason": "Invalid Expression"},
                },
            )

    async def test_error_on_async_eval(self):
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            result = await self.client.post("/eval", json={"expr": "1 + 1"})
            self.assertEqual(result.status, 500)
            data = await result.json()
            self.assertEqual(
                data,
                {
                    "result": None,
                    "error": {
                        "exc": "Connection refused: POST http://plus.service",
                        "reason": "Error evaluating expression",
                    },
                },
            )

    async def test_plus_simple_expression(self):
        """
        Confere que conseguimos avaliar uma expressão simples: a + b
        """
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await self.client.post("/eval", json={"expr": "1 + 1"})
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 2})

    async def test_plus_simple_expression_more_than_one_value(self):
        """
        Confere que conseguimos avaliar uma expressão simples: a + b + c
        """
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await self.client.post("/eval", json={"expr": "4 + 1 + 3"})
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 8})

    async def test_plus_simple_expression_with_negative_numbers(self):
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await self.client.post(
                "/eval", json={"expr": "4 + 1 + -3"}
            )
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 2})

    async def test_plus_simple_expression_with_parenthesis(self):
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await self.client.post(
                "/eval", json={"expr": "8 + (1 + -3)"}
            )
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 6})

    async def test_complex_expression_multiple_operations(self):
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post(
                "http://multiply.service", callback=multiply_service_callback
            )
            result = await self.client.post("/eval", json={"expr": "8 + 2 * 3"})
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 14})

    async def test_complex_expression_multiple_repeated_operations(self):
        with aioresponses(passthrough=["http://127.0.0.1"]) as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post("http://plus.service", callback=plus_service_callback)
            rsps.post("http://power.service", callback=power_service_callback)
            rsps.post(
                "http://multiply.service", callback=multiply_service_callback
            )
            result = await self.client.post(
                "/eval", json={"expr": "5 + 5 + (2 * 3) + (5^2)"}
            )
            self.assertEqual(result.status, 200)
            data = await result.json()
            self.assertEqual(data, {"result": 41})
