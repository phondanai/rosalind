def gen_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return gen_fib(n-1) + gen_fib(n-2)

if __name__ == '__main__':
    with open('rosalind_fibo.txt', 'r') as f:
        num = int(f.read().strip())

        print(gen_fib(num))

