# A simple Compression Algorithm
### Written in Python

Two algorithms are implemented here:

* Compression
* Decompression

### Compression:
Two or more occurences of the same character should
be converted to '__two characters + the number of times
the character repeats after that__'

Note: Valid input requires the string to be
      UpperCase letters A-Z only.
      
##### Test Cases:
Input | Output
--- | ---
"__A__",      |  "__A__"
"__AA__",     |  "__AA0__"
"__AAAA__",   |  "__AA2__"
"__AAABCC__", |  "__AAA1BCC0__"


### Decompression:
This is a simple reversal process from __Compression__. It takes a compressed
string and expands it.
      
##### Test Cases:
Input | Output
--- | ---
"__BB0__",      |  "__BB__"
"__ABB3AA1__",     |  "__ABBBBBAAA__"
"__ABCDD2EFG__",   |  "__ABCDDDDEFG__"
"__AA0BB1CC2__", |  "__AABBBCCCC__"

### Important!
The compression would only suppor a single digit. What this means is that
if the Compression input was "__AAAAAAAAAAA__" (11 A's), the output would be: "__AA9__".

What if I wanted to add 12 A's now? Then the output would be: "__AA9A__"

13 A's? Output: "__AA9AA0__"
14 A's? Output: "__AA9AA1__"

*You get the idea :)*

### Command Line
Arguments:
* __-c__ : Compress a string
* __-d__ : Decompress a string

<br />
__Example Usage__:
### `python compress.py -c AAABBCDD` <br />
Output: <br />
##### __`Compression AA1BB0CDD0`__

<br /> <br />

### `python compress.py -d AA4BCC3` <br />
Output: <br />
##### __`Decompression AAAAAABCCCCC`__

<br /> <br />

You can use both arguments at once. Like this:
### `python compress.py -c BBBBBBAACCDC -d AA2BB4CC0` <br />
Output: <br />
##### __`Compression BB4AA0CC0DC`__ <br />
##### __`Compression AAAABBBBBBCC`__ <br />
