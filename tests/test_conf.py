import os
from importlib import reload

from asynctest import TestCase, mock

import maas.conf


class ConfTest(TestCase):
    async def setUp(self):
        pass

    async def test_load_service_addrs_from_env(self):
        with mock.patch.dict(
            os.environ,
            ENV="MAAS",
            MAAS_PLUS_SERVICE_ADDRESS="http://plus.pe.hmg.asgard.b2w.io",
            MAAS_MINUS_SERVICE_ADDRESS="http://minus.pe.hmg.asgard.b2w.io",
            MAAS_DIVIDE_SERVICE_ADDRESS="http://divide.pe.hmg.asgard.b2w.io",
            MAAS_MULTIPLY_SERVICE_ADDRESS="http://multiply.pe.hmg.asgard.b2w.io",
            MAAS_POWER_SERVICE_ADDRESS="http://power.pe.hmg.asgard.b2w.io",
        ):
            reload(maas.conf)
            self.assertEqual(
                maas.conf.settings.PLUS_SERVICE_ADDRESS,
                "http://plus.pe.hmg.asgard.b2w.io",
            )
            self.assertEqual(
                maas.conf.settings.MINUS_SERVICE_ADDRESS,
                "http://minus.pe.hmg.asgard.b2w.io",
            )
            self.assertEqual(
                maas.conf.settings.DIVIDE_SERVICE_ADDRESS,
                "http://divide.pe.hmg.asgard.b2w.io",
            )
            self.assertEqual(
                maas.conf.settings.MULTIPLY_SERVICE_ADDRESS,
                "http://multiply.pe.hmg.asgard.b2w.io",
            )
            self.assertEqual(
                maas.conf.settings.POWER_SERVICE_ADDRESS,
                "http://power.pe.hmg.asgard.b2w.io",
            )
