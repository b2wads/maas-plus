import os

os.environ["ENV"] = "TEST"

os.environ["TEST_PLUS_SERVICE_ADDRESS"] = os.getenv(
    "TEST_PLUS_SERVICE_ADDRESS", "http://plus.service"
)
os.environ["TEST_MINUS_SERVICE_ADDRESS"] = os.getenv(
    "TEST_MINUS_SERVICE_ADDRESS", "http://minus.service"
)
os.environ["TEST_DIVIDE_SERVICE_ADDRESS"] = os.getenv(
    "TEST_DIVIDE_SERVICE_ADDRESS", "http://divide.service"
)
os.environ["TEST_MULTIPLY_SERVICE_ADDRESS"] = os.getenv(
    "TEST_MULTIPLY_SERVICE_ADDRESS", "http://multiply.service"
)
os.environ["TEST_POWER_SERVICE_ADDRESS"] = os.getenv(
    "TEST_POWER_SERVICE_ADDRESS", "http://power.service"
)

os.environ["TEST_ASYNCWORKER_HTTP_PORT"] = os.getenv(
    "TEST_ASYNCWORKER_HTTP_PORT", "9999"
)


assert os.environ["ENV"] == "TEST"
