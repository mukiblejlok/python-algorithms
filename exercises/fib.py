import time


def fib(n: int) -> int:
    f_2, f_1 = 0, 1

    for k in range(1, n + 1):
        f = f_2 + f_1
        f_2, f_1 = f_1, f
    return f


if __name__ == '__main__':
    for i in range(7):
        t0 = time.perf_counter()
        r = fib(10**i)
        t1 = time.perf_counter()
        dt = t1 - t0
        print(f"10^{i} ({dt:4g})")
        """
        10^0 (1.57e-05)
        10^1 (6.3e-06)
        10^2 (2.19e-05)
        10^3 (0.0001437)
        10^4 (0.0052997)
        10^5 (0.222287)
        10^6 (10.4707)
        10^7 (1628.11)
        """
