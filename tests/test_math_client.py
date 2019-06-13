from aioresponses import aioresponses
from asynctest import TestCase
from yarl import URL

from maas.client import MathClient, default_http_client_timeout
from tests.util import (
    minus_service_callback,
    plus_service_callback,
    multiply_service_callback,
    divide_service_callback,
    power_service_callback,
)


class MathClientTest(TestCase):
    async def setUp(self):
        self.client = MathClient()

    async def test_session_has_default_timeout(self):
        client = MathClient()
        self.assertEqual(client.session._timeout, default_http_client_timeout)

    async def test_plus_calls_right_service_address(self):
        """
            Confere que para valores simples o serviço é chamado com o payload correto
        """
        with aioresponses() as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await self.client.plus(5, 5)
            request_plus = rsps.requests[("POST", URL("http://plus.service"))][
                0
            ]
            self.assertEqual(result, {"result": 10})
            self.assertEqual(
                request_plus.kwargs["json"], {"left": 5, "right": 5}
            )

    async def test_minus_calls_right_service_address(self):
        """
            Confere que para valores simples o serviço é chamado com o payload correto
        """
        with aioresponses() as rsps:
            rsps.post("http://minus.service", callback=minus_service_callback)
            result = await self.client.minus(5, 5)
            request_plus = rsps.requests[("POST", URL("http://minus.service"))][
                0
            ]
            self.assertEqual(result, {"result": 0})
            self.assertEqual(
                request_plus.kwargs["json"], {"left": 5, "right": 5}
            )

    async def test_multiply_calls_right_service_address(self):
        """
            Confere que para valores simples o serviço é chamado com o payload correto
        """
        with aioresponses() as rsps:
            rsps.post(
                "http://multiply.service", callback=multiply_service_callback
            )
            result = await self.client.multiply(5, 5)
            request_plus = rsps.requests[
                ("POST", URL("http://multiply.service"))
            ][0]
            self.assertEqual(result, {"result": 25})
            self.assertEqual(
                request_plus.kwargs["json"], {"left": 5, "right": 5}
            )

    async def test_divide_calls_right_service_address(self):
        """
            Confere que para valores simples o serviço é chamado com o payload correto
        """
        with aioresponses() as rsps:
            rsps.post("http://divide.service", callback=divide_service_callback)
            result = await self.client.divide(21, 3)
            request_plus = rsps.requests[
                ("POST", URL("http://divide.service"))
            ][0]
            self.assertEqual(result, {"result": 7})
            self.assertEqual(
                request_plus.kwargs["json"], {"left": 21, "right": 3}
            )

    async def test_power_calls_right_service_address(self):
        """
            Confere que para valores simples o serviço é chamado com o payload correto
        """
        with aioresponses() as rsps:
            rsps.post("http://power.service", callback=power_service_callback)
            result = await self.client.power(5, -2)
            request_plus = rsps.requests[("POST", URL("http://power.service"))][
                0
            ]
            self.assertEqual(result, {"result": 0.04})
            self.assertEqual(
                request_plus.kwargs["json"], {"left": 5, "right": -2}
            )
