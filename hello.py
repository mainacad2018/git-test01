# hello %username%
import sys

who = "word" if len(sys.argv) < 2 else sys.argv[1]
print("hello, %s" % who)
