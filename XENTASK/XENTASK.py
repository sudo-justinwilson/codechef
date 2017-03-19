#!/usr/bin/python3

# URL for challenge:
#       https://www.codechef.com/problems/XENTASK

def get_num_of_test_cases():
    num_of_test_cases = input()
    return int(num_of_test_cases)

def test_case():
    N = input()
    Xi = str(input())
    Yi = str(input())
    X = [int(i) for i in Xi.split()]
    Y = [int(i) for i in Yi.split()]
    Xl = [X[i] for i in range(len(X)) if i%2 == 0]
    Yl = [X[i] for i in range(len(X)) if i%2 == 1]
    Xl += [Y[i] for i in range(len(X)) if i%2 == 1]
    Yl += [Y[i] for i in range(len(X)) if i%2 == 0]
    totalX, totalY = sum(Xl), sum(Yl)
    print(min(totalX, totalY))

def main():
    T = get_num_of_test_cases()
    while T != 0:
        test_case()
        T -= 1

if __name__ == '__main__':
    main()
