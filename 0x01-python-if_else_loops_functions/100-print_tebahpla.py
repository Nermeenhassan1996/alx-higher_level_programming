!/usr/bin/python3
upper = False
for i in range(90, 64, -1):
    if not upper:
        i += 32
        upper = True
    else:
        upper = False
    print("{:c}".format(i), end="")
