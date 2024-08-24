import numpy as np

num = input("ENTER YOUR BODY COUNT: ")

umm = []

for _ in range(len(num),0, -1):
    umm.append(num[_])

final = np.array(umm)

print(final)

