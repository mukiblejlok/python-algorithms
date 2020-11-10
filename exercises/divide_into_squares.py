
def divide_into_squares(x: float, y: float, e: float = 0.1):
    if x == 0 or y == 0:
        return x
    l = max(x, y)
    w = min(x, y)
    r = l // w
    new_l = l - r * w
    return divide_into_squares(x=w, y=new_l)


if __name__ == '__main__':

    test_cases = (
        (1680, 640, 80),
        (250, 50, 50),
        (40, 40, 40),
        (1601, 203, 50)
    )
    for case in test_cases:
        assert case[2] == divide_into_squares(x=case[0], y=case[1]), case
    print("ALL TESTS OK")
