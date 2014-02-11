"""
A python program that implements a simple
compression and decompression algorithm.

           Sandeep Jadoonanan
                2/11/2014
"""

import argparse
from dataEncode import Compressor, Decompressor

def showCompression(inputStr):
    print "\nCompression:\n"
    try:
       c = Compressor(inputStr)
       c.crunch()
       print c
    except Exception as e:
        print e

def showDecompression(inputStr):
    print "\nDecompression:\n"
    try:
       d = Decompressor(inputStr)
       d.crunch()
       print d
    except Exception as e:
        print e


commandLine = argparse.ArgumentParser()
commandLine.add_argument("-c", "--compress", type = str, help = "Compress a string")
commandLine.add_argument("-d", "--decompress", type = str, help = "Decompress a string")

args = commandLine.parse_args()

if args.compress:
   showCompression(args.compress)
if args.decompress:
    showDecompression(args.decompress)

if not args.compress and not args.decompress:
    print "\nCompress.py > No input values\n"

