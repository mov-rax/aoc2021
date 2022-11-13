import utils
import numpy as np

data = np.array([int(x) for x in utils.get_input('d7').strip().split(",")])
data.sort()
median = data[len(data) // 2]
triangle = lambda n: n * (n + 1) // 2
resiter = (triangle(abs(data - x)).sum() for x in range(data.max()))
last = next(resiter)
for v in resiter:
    if v < last:
        last = v
    else:
        break
print(f"part 1: {abs(data - median).sum()}") 
print(f"part 2: {last}")