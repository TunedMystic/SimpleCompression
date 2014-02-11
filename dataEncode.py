"""
A python program that implements a simple
compression and decompression algorithm.

           Sandeep Jadoonanan
                2/11/2014
"""

import abc
import re
import customValidate as cv

class DataString(object):
    # Regex patterns to check for valid strings
    ReCompression = r"^[A-Z]+$"
    ReDecompression = r"^((([A-Z])\3[0-9])|[A-Z])+$"

    def __init__(self, inputStr = ""):
        self.inputString = inputStr
        self.outputString = ""

    def __repr__(self):
        s = ""
        s += "Input : " + self.inputString[:10] + "\n"
        s += "Output: " + (self.outputString[:10] if self.outputString else "...")
        return s

    def alreadyComputed(f):
        """
        Simple decorator to check if the output
        string has already been computed
        """
        def computed(self):
           if not self.outputString:
              #print "S: first time"
              return f(self)
           else:
              #print "S: already computed"
              return self.outputString
        return computed

    @abc.abstractmethod
    @alreadyComputed
    def crunch(self):
        pass

    alreadyComputed = staticmethod(alreadyComputed)


class Compressor(DataString):
    def __init__(self, inputStr = ""):
        if re.match(Compressor.ReCompression, inputStr):
           super(Compressor, self).__init__(inputStr)
        else:
            raise Exception("Invalid string for Compressor")

    @DataString.alreadyComputed
    def crunch(self):

        def gatherElements(el, i):
            """
            Gather consecutive elements 'el' from a list
            beginning at index 'i'
            """
            counter = 0
            for ic in self.inputString[i:]:
                if ic == el:
                    counter += 1
                else:
                    break
            return counter
        # ------------------------------------------------

        def compressThis(el, elCount):
            """
            Compresses a large string (of same elements):
            'A' -> 'A'
            'AA' -> 'AA0'
            'AAA' -> 'AA1'
            'AAAA' -> 'AA2'
               ...
            'AAAAAAAAAAA' -> AA9
            'AAAAAAAAAAAA' -> AA9A
            'AAAAAAAAAAAAA' -> AA9AA0
            """
            output = ""
            remainder = elCount
             
            if remainder > 11:
                iterations, remainder = divmod(elCount, 11)
                output += (el * 2 + str(9) ) * iterations 
            if remainder >= 2:
                output += el * 2 + str(remainder - 2)   
            else:
                output += el * remainder

            return output
        # ------------------------------------------------

        i = 0
        ch = ""
        chCount = 0
        chEncode = ""
        done = False

        while not done:
            ch = self.inputString[i]
            # Returns the count of the element 'ch'
            chCount = gatherElements(ch, i)
            if chCount > 1:
                # Compress the substring
                chEncode = compressThis(ch, chCount)
            else:
                chEncode = ch
            # Update the output
            self.outputString += chEncode

            # Increment counter or finish the algorithm
            i += chCount
            if i == len(self.inputString):
                done = True

        return self.outputString


class Decompressor(DataString):
    def __init__(self, inputStr = ""):
        if re.match(Decompressor.ReDecompression, inputStr):
            if cv.overkillValidate(inputStr):
               super(Decompressor, self).__init__(inputStr)
            else:
               raise Exception("Invalid string for Decompressor")
        else:
            raise Exception("Invalid string for Decompressor")

    @DataString.alreadyComputed
    def crunch(self):

        def nextIsSame(ch, i):
            """
            Returns True if the next element (from index 'i')
            is the same as ch.

            Returns False otherwise.
            """
            if i == len(self.inputString) - 1:
                return False
            else:
                return ch == self.inputString[i + 1]
        # ------------------------------------------------

        def expandChunk(chunkStr):
            """
            Takes a string excerpt of the form:
                         AA# 
            ( where "A" is a character, where "#" is a number )
            and expands it. So:

            AA1 -> AAA
            AA3 -> AAAAA
            AA0 -> AA
               ...
            """
            return (chunkStr[0] * 2) + (chunkStr[0] * int(chunkStr[2]) )
        # ------------------------------------------------

        i = 0
        done = False
        ch = ""
        chDecode = ""

        while not done:
            ch = self.inputString[i]
            # Is the next character the same?
            if nextIsSame(ch, i):
                chDecode = expandChunk(self.inputString[i: i + 3])
                i += 3
            else:
                chDecode = ch
                i += 1
            # Update the output
            self.outputString += chDecode
            
            # Increment counter or finish the algorithm
            if i == len(self.inputString):
                done = True

        return self.outputString

