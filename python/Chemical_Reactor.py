import matplotlib.pyplot as plt
import numpy as np

dt = 0.1
k1 = 0.008
k2 = 0.002
N = 100

A = [0] * N
B = [0] * N
C = [0] * N

A[0] = 100
B[0] = 50
C[0] = 0

for i in range(N-1):
    d_a = ( (k2 * C[i]) - (k1 * A[i] * B[i]) ) * dt
    d_b = ( (k2 * C[i]) - (k1 * A[i] * B[i]) ) * dt
    d_c = 2 * ( (k1 * A[i] * B[i]) - (k2 * C[i]) ) * dt

    A[i+1] = A[i] + d_a
    B[i+1] = B[i] + d_b
    C[i+1] = C[i] + d_c

T = 0
print('Time     A[i]        B[i]        C[i]')
print('--------------------------')

for i in range(N):
    print('{:.2f}       {:.2f}      {:.2f}      {:.2f}'.format(T, A[i], B[i], C[i]))
    T += dt

x = np.arange(0, dt*N, dt)
plt.plot(x, A, label='reactant A', color='red')
plt.plot(x, B, label='reactant B', color='green')
plt.plot(x, C, label='reactant C', color='blue')
plt.legend()
plt.show()