"""
A python program that implements a simple
compression and decompression algorithm.

           Sandeep Jadoonanan
                2/11/2014
"""

import unittest
from dataEncode import Compressor, Decompressor

class encodingTest(unittest.TestCase):
   def setUp(self):
      pass

   def test_Compression(self):
      # Simple compression encoding
      self.assertEqual(Compressor("AAAA").crunch(),              "AA2")
      self.assertEqual(Compressor("A").crunch(),                   "A")
      self.assertEqual(Compressor("AAAABABBB").crunch(),    "AA2BABB1")
      self.assertEqual(Compressor("ABCDEF").crunch(),         "ABCDEF")
      self.assertEqual(Compressor("AAAAAAAAAAAAAA").crunch(), "AA9AA1")
      self.assertEqual(Compressor("AAACBBC").crunch(),      "AA1CBB0C")

      # Make sure that the object isn't constructed with an invalid string
      self.assertRaises(Exception, Compressor,       "A9")
      self.assertRaises(Exception, Compressor,     "ABBa")
      self.assertRaises(Exception, Compressor,     "BaBB")
      self.assertRaises(Exception, Compressor, "ABB0BB10")


   def test_Decompression(self):
      # Simple Decompression encoding
      self.assertEqual(Decompressor("A").crunch(),                                "A")
      self.assertEqual(Decompressor("AA8BCC0KK2").crunch(),       "AAAAAAAAAABCCKKKK")
      self.assertEqual(Decompressor("AA9A").crunch(),                  "AAAAAAAAAAAA")
      self.assertEqual(Decompressor("BB0ABCDEFGHH3").crunch(),       "BBABCDEFGHHHHH")
      self.assertEqual(Decompressor("AA0BB0CDD0EE1FF0GG0").crunch(), "AABBCDDEEEFFGG")
      self.assertEqual(Decompressor("BB9BB0").crunch(),               "BBBBBBBBBBBBB")

      # Make sure that the object isn't constructed with an invalid string
      self.assertRaises(Exception, Decompressor,   "AAA")
      self.assertRaises(Exception, Decompressor,  "BB83")
      self.assertRaises(Exception, Decompressor, "BGG7b")
      self.assertRaises(Exception, Decompressor,  "AA01")

if __name__ == '__main__':
    unittest.main(verbosity = 2)

"""
from dataEncode import Decompressor as d, Compressor as c
d1 = d("BB9")
c1 = c("AAABBAABA")
"""