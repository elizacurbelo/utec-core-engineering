#!/usr/bin/env python3
print("{0}".format("".join(chr(i) for i in range(97, 123) if chr(i) not in "qe")), end="")
