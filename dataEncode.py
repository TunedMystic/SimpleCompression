
"""
A python program that implements a simple
compression and decompression algorithm.

           Sandeep Jadoonanan
                2/11/2014
"""

import abc
import re

class DataString(object):
    def __init__(self, inputStr = ""):
        self.inputString = inputStr
        self.outputString = ""

    def __unicode__(self):
        s = ""
        s += "Input : " + self.inputString[:10] + "\n"
        s += "Output: " + self.outputString[:10] if self.outputString else "..."
        return s

    @abc.abstractmethod
    def crunch(self):
        pass


class Compressor(DataString):
    def __init__(self, inputStr = ""):
        super(Compressor, self).__init__(inputStr)

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
               ...
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

        #for i, ch in enumerate(self.inputString):
        while done == False:
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




if __name__ == "__main__":
    print Compressor("AABBBBBBBBBBBBBBBB").crunch()
