#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample01 (self):
            for _ in range(100):
                self.assertEqual (1, calc(1, 1))

        def test_sample02 (self):
            for _ in range(100):
                self.assertEqual (998001, calc(999, 999))

        def test_sample03 (self):
            for _ in range(100):
                self.assertEqual (999, calc(1, 999))

        def test_sample04 (self):
            for _ in range(100):
                self.assertEqual (999, calc(999, 1))

        def test_sample05 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1, 0))

        def test_sample06 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(0, 1))

        def test_sample07 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(999, 1000))

        def test_sample08 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1000, 999))

        def test_sample09 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(0, 0))

        def test_sample10 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1000, 1000))

        def test_sample11 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(0, 1000))

        def test_sample12 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1000, 0))

        def test_sample13 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(float('inf'), float('inf')))

        def test_sample14 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(float('inf'), -float('inf')))

        def test_sample15 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(0.1, 0.1))

        def test_sample16 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1, 0.1))

        def test_sample17 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(0.1, 1))

        def test_sample18 (self):
            for _ in range(100):
                self.assertEqual (-1, calc("a", "10"))

        def test_sample19 (self):
            for _ in range(100):
                self.assertEqual (-1, calc("1", "999"))

        def test_sample20 (self):
            for _ in range(100):
                self.assertEqual (-1, calc("1a", "999"))

        def test_sample21 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1, "a"))

        def test_sample22 (self):
            for _ in range(100):
                self.assertEqual (-1, calc("a", 1))
        
        def test_sample23 (self):
            for _ in range(100):
                self.assertEqual (-1, calc([1], [1]))

        def test_sample24 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1, [1]))

        def test_sample25 (self):
            for _ in range(100):
                self.assertEqual (-1, calc([1], 1))

        def test_sample26 (self):
            for _ in range(100):
                self.assertEqual (-1, calc({"a":1}, {"a":1}))

        def test_sample27 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1, {"a":1}))

        def test_sample28 (self):
            for _ in range(100):
                self.assertEqual (-1, calc({"a":1}, 1))

        def test_sample29 (self):
            for _ in range(100):
                self.assertEqual (-1, calc((1,1), (1,1)))

        def test_sample30 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1, (1,1)))

        def test_sample31 (self):
            for _ in range(100):
                self.assertEqual (-1, calc((1,1), 1))

        def test_sample32 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(None, None))

        def test_sample33 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1, None))

        def test_sample34 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(None, 1))

        def test_sample35 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(True, False))

        def test_sample36 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(1, True))

        def test_sample37 (self):
            for _ in range(100):
                self.assertEqual (-1, calc(True, 1))
