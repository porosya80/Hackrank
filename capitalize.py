import re
# Complete the solve function below.
def solve(s):
    return re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), s)




print(solve("1 w 2 r 3g"))