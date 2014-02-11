import unittest
from dataEncode import Compressor, Decompressor

class encodingTest(unittest.TestCase):
   def setUp(self):
      pass

   def test_Compressor(self):
      self.assertEqual(Compressor("AAAA").crunch(), "AA2")
      self.assertEqual(Compressor("A").crunch(), "A")
      self.assertEqual(Compressor("AAAABABBB").crunch(), "AA2BABB1")
      self.assertEqual(Compressor("ABCDEF").crunch(), "ABCDEF")

      self.assertRaises(Exception, Compressor, "A9")

if __name__ == '__main__':
	unittest.main()