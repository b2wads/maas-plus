import json

from aioresponses import CallbackResult


def plus_service_callback(url, **kwargs):
    data = kwargs["json"]
    return CallbackResult(
        status=200, body=json.dumps({"result": data["left"] + data["right"]})
    )


def minus_service_callback(url, **kwargs):
    data = kwargs["json"]
    return CallbackResult(
        status=200, body=json.dumps({"result": data["left"] - data["right"]})
    )


def multiply_service_callback(url, **kwargs):
    data = kwargs["json"]
    return CallbackResult(
        status=200, body=json.dumps({"result": data["left"] * data["right"]})
    )


def divide_service_callback(url, **kwargs):
    data = kwargs["json"]
    return CallbackResult(
        status=200, body=json.dumps({"result": data["left"] / data["right"]})
    )


def power_service_callback(url, **kwargs):
    data = kwargs["json"]
    return CallbackResult(
        status=200, body=json.dumps({"result": data["left"] ** data["right"]})
    )
