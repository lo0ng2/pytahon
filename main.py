import numpy as np
a = np.random.randint(1,10, size=(3,3))
b = np.random.randint(1,10, size=(3,3))
print(a)
print(b)
# cong
print(a+b)
# tru
print(a-b)
# nhan
print(a*b)
# tim nghich dao
print(np.linalg.inv(a))
print(np.linalg.inv(b))
# tim dinh thuc
print(np.linalg.det(a))
print(np.linalg.det(b))
# mu
print(a**2)
#rank
print(np.linalg.matrix_rank(a));
print(np.linalg.matrix_rank(b));
# tim ma tran chuyen vi
print(np.transpose(a))
print(np.transpose(b))
