import sys

def calculator():
    op = sys.argv[2]
    result = eval(op)
    print(f"The result of the operation is: {result}")