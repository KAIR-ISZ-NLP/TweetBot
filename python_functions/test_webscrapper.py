#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import webscrapper


class MyTestCase(unittest.TestCase):
    def test_extract_desc_for_app(self):
        result = webscrapper.extract_desc_for_app('https://www.gry-online.pl/gry/agatha-christie-hercule-poirot-the-first-cases/zf6018#pc')
        result2 = webscrapper.extract_desc_for_app('agashdhf')
        self.assertEqual(type(result), str)
        self.assertEqual(result2, "Invalid url")


if __name__ == '__main__':
    unittest.main()
