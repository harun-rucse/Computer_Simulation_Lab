def main():
    with open('./lcm_input.txt') as file:
        for line in file.readlines():
            multiplier, increment, seed, modulus, n = [int(x) for x in line.rstrip().rsplit(',')]

            X = LCM(seed, multiplier, increment, modulus, n)
            print(X)

def LCM(X0, A, C, M, N):
    X = [0] * N
    X[0] = X0

    for i in range(N-1):
        X[i+1] = (A * X[i] + C) % M

    return X

if __name__ == '__main__':
    main()