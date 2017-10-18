# -*- coding: utf-8 -*-

from __future__ import absolute_import
import unittest

import main


class TestEmails(unittest.TestCase):

    def setUp(self):
        self.app = main.create_app(__name__)

    def tearDown(self):
        self.app = None

    def test_app_not_none(self):
        self.assertIsNotNone(self.app)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmails)
    unittest.TextTestRunner(verbosity=2).run(suite)
