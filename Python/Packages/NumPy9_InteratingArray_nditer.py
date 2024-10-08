import numpy as np
arr=np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,8,7]]])
for x in np.nditer(arr):
    print(x)


