import unittest
from unittest import TestCase
from LocatingRestrictionSites import complement_, reverse_string_, is_dna


class TestLocatingRestrictionSite(TestCase):
    def setUp(self):
        self.string = "GCATGC"

    def test_complement_1(self):
        self.assertEqual(complement_(self.string), "CGTACG")

    def test_complement_2(self):
        self.assertEqual(complement_("CGTACG"), self.string)

    def test_reverse_string(self):
        self.assertEqual(reverse_string_(self.string), "CGTACG")

    def test_correct_dna(self):
        self.assertTrue(is_dna(self.string))

if __name__ == "__main__":
    unittest.main()
