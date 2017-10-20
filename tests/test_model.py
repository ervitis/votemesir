# -*- coding: utf-8 -*-

import unittest

from datetime import datetime
from models.user import (ModelUser, generate_data)


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

    def test_auto_generate_data(self):
        models = generate_data(5)
        self.assertEqual(len(models), 5)
        self.assertTrue(any([model.get('email') for model in models]))
        self.assertTrue(any([model.get('password') for model in models]))
        self.assertTrue(any([model.get('name') for model in models]))
        self.assertTrue(any([model.get('surname') for model in models]))

    def test_auto_generate_data_url_and_date_are_empty(self):
        models = generate_data(2)
        self.assertFalse(any([model.get('url_email_validation') for model in models]))
        self.assertFalse(any([model.get('date_last_vote') for model in models]))

    def test_all_generated_data_are_not_equal(self):
        models = generate_data(1000)
        i = 0
        for m in models[i:]:
            j = i + 1
            for n in models[j:]:
                if n == m:
                    self.fail('{n} and {m} are equal in iteration {i}, {j}'.format(n=n, m=m, i=i, j=j))
                j += i
            i += 1

    def test_parameter_generate_data_int(self):
        self.assertRaises(AssertionError, generate_data, '2')
        self.assertRaises(AssertionError, generate_data, 4.5)

    def test_parameter_generate_data_between_1_and_1000(self):
        self.assertRaises(AssertionError, generate_data, 0)
        self.assertRaises(AssertionError, generate_data, 1001)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestModel)
    unittest.TextTestRunner(verbosity=2).run(suite)
