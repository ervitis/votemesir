# -*- coding: utf-8 -*-

import unittest

from datetime import datetime
from models.user import ModelUser


class TestModel(unittest.TestCase):
    _test_parameters = {
        'email': 'example@examplebot.com',
        'url_email_validation': 'http://validate.me/12345678910',
        'date_last_vote': datetime.now(),
        'password': '123456',
        'name': 'foo',
        'surname': 'bar'
    }

    def setUp(self):
        self.model = ModelUser(**self._test_parameters)

    def tearDown(self):
        self.model = None

    def test_model_not_none(self):
        self.assertIsNotNone(self.model)

    def test_model_properties(self):
        for attr, value in self._test_parameters.items():
            self.assertEqual(getattr(self.model, attr), value)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestModel)
    unittest.TextTestRunner(verbosity=2).run(suite)
