# write a code in which user can write more than 1 arguments in command line and output should be "My Name is {arg}". But it should not take 0th index argument.

import sys

if len(sys.argv) > 2:
    sys.exit("More than 1 arguments must be given.")

for arg in sys.argv[1:]:
    print(arg)