"""
A python program that implements a simple
compression and decompression algorithm.

           Sandeep Jadoonanan
                2/11/2014
"""

import re

def overkillValidate(inputStr):
    """
    A very inefficient, but working validation function for
    a decompression string...

    NOTE: The default ReDecompression regex pattern doesn't
          work quite well yet. Falling back to this for now.
    """

    if len(inputStr) > 2:

        strNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
         
        i = 0
        el = ""
        done = False
        while not done:
            el = inputStr[i]
            if i < len(inputStr) - 2:
                if ((inputStr[i] == inputStr[i + 1]) and (inputStr[i + 2] in strNumbers) ) \
                or (inputStr[i] != inputStr[i + 1]):
                   if ((inputStr[i] == inputStr[i + 1]) and (inputStr[i + 2] in strNumbers) ):
                      i += 2
                   else:
                      i += 1
                else:
                    return False
            else:
                if (inputStr[i] != inputStr[i + 1]):
                    i += 1
                else:
                    return False

            if i == len(inputStr) - 1:
                done = True

        return True
     
    else:
      return True

