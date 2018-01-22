#!/usr/bin/env python3
# vim:set ff=unix expandtab ts=4 sw=4:

from unittest import TestCase
from toxTest.Sym2Num import sym2num
class Test_Sym2Num(TestCase):
    def test_sym2num(self):
        res=sym2num()
        self.assertEqual(res,42)

