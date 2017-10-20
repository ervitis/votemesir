# -*- coding: utf-8 -*-

import unittest

from datetime import datetime
from google.appengine.ext import testbed
from models.user import ModelUser

from models.user import generate_data


class TestDatastoreOperations(unittest.TestCase):
    _test_parameters = {
        'email': 'example@examplebot.com',
        'url_email_validation': 'http://validate.me/12345678910',
        'date_last_vote': datetime.now(),
        'password': '123456',
        'name': 'foo',
        'surname': 'bar'
    }

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_save_model_into_datastore(self):
        ModelUser(**self._test_parameters).put()
        entities = ModelUser().all().fetch(1)
        self.assertEqual(1, len(entities))
        for k, v in self._test_parameters.items():
            self.assertEqual(getattr(entities[0], k), v)

    def test_save_multiple_models_into_datastore(self):
        data = generate_data(3)
        for d in data:
            ModelUser(**d).put()
        entities = ModelUser().all().fetch(3)
        self.assertEqual(3, len(entities))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDatastoreOperations)
    unittest.TextTestRunner(verbosity=2).run(suite)
