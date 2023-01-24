import sys

from calculator.calculator import calculator
from fs.fs import fs

fuctionality = sys.argv[1]

if fuctionality == "cal": calculator()
elif fuctionality == "fs": fs()