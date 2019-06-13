from aioresponses import aioresponses
from asynctest import TestCase
from yarl import URL

from contrib.parser import Plus, Value, Minus, Divide, Times, Exponent
from tests.util import (
    plus_service_callback,
    minus_service_callback,
    divide_service_callback,
    multiply_service_callback,
    power_service_callback,
)


class ParserValueTest(TestCase):
    async def test_value_has_async_eval(self):
        v1 = Value("10")
        self.assertEqual(10.0, await v1.eval())


class ParserTest(TestCase):
    async def setUp(self):
        pass

    async def test_plus_calls_service(self):
        plus = Plus()
        plus.addChild(Value("4"))
        plus.addChild(Value("10"))
        with aioresponses() as rsps:
            rsps.post("http://plus.service", callback=plus_service_callback)
            result = await plus.eval()
            plus_service_call = rsps.requests[
                ("POST", URL("http://plus.service"))
            ][0].kwargs["json"]
            self.assertEqual(plus_service_call, {"left": 4, "right": 10})
            self.assertEqual(14.0, result)

    async def test_minus_calls_service(self):
        plus = Minus()
        plus.addChild(Value("4"))
        plus.addChild(Value("10"))
        with aioresponses() as rsps:
            rsps.post("http://minus.service", callback=minus_service_callback)
            result = await plus.eval()
            plus_service_call = rsps.requests[
                ("POST", URL("http://minus.service"))
            ][0].kwargs["json"]
            self.assertEqual(plus_service_call, {"left": 4, "right": 10})
            self.assertEqual(-6.0, result)

    async def test_divide_calls_service(self):
        plus = Divide()
        plus.addChild(Value("15"))
        plus.addChild(Value("5"))
        with aioresponses() as rsps:
            rsps.post("http://divide.service", callback=divide_service_callback)
            result = await plus.eval()
            plus_service_call = rsps.requests[
                ("POST", URL("http://divide.service"))
            ][0].kwargs["json"]
            self.assertEqual(plus_service_call, {"left": 15, "right": 5})
            self.assertEqual(3.0, result)

    async def test_multiply_calls_service(self):
        plus = Times()
        plus.addChild(Value("15"))
        plus.addChild(Value("5"))
        with aioresponses() as rsps:
            rsps.post(
                "http://multiply.service", callback=multiply_service_callback
            )
            result = await plus.eval()
            plus_service_call = rsps.requests[
                ("POST", URL("http://multiply.service"))
            ][0].kwargs["json"]
            self.assertEqual(plus_service_call, {"left": 15, "right": 5})
            self.assertEqual(75.0, result)

    async def test_power_calls_service(self):
        plus = Exponent()
        plus.addChild(Value("15"))
        plus.addChild(Value("5"))
        with aioresponses() as rsps:
            rsps.post("http://power.service", callback=power_service_callback)
            result = await plus.eval()
            plus_service_call = rsps.requests[
                ("POST", URL("http://power.service"))
            ][0].kwargs["json"]
            self.assertEqual(plus_service_call, {"left": 15, "right": 5})
            self.assertEqual(759_375, result)
