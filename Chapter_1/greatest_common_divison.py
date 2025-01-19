def cal_gcd_recursive(a: int, b: int) -> int:
    # TC: log(max(a, b))
    if  a % b == 0:
        return b
    else:
        return cal_gcd_recursive(b, a%b)


def cal_gcd_iterative(a: int, b: int) -> int:
    # 輾轉相除法
    while b != 0:
        a, b = b, a % b

    return a

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(f"GCD recursive: {a}, {b} -> {cal_gcd_recursive(a, b)}")
    print(f"GCD iterative: {a}, {b} -> {cal_gcd_iterative(a, b)}")
