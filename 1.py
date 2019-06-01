import numpy as np 
T=[[0,1],[2,3]]
U=[[4,5],[6,7]]
T=np.array(T)
U=np.array(U)
print(T+U)
print(2*T)
T=np.array([[0,1],[2,3],[4,5]])
print(T[1])
print(T[1][0])
T[2][0]=10
print(T)