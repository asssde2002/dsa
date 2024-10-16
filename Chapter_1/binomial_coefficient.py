def cal_binomial_coefficient_recursive(n: int, m: int) -> int:
    if m == 0 or n == m:
        return 1
    else:
        return cal_binomial_coefficient_recursive(n-1, m) + cal_binomial_coefficient_recursive(n-1, m-1)
    

def cal_binomial_coefficient_iterative(n: int, m: int) -> int:
    k = max(n-m, m)
    numerator = 1
    denominator = 1
    for i in range(k+1, n+1):
        numerator *= i
    
    for i in range(1, n-k+1):
        denominator *= i

    return numerator//denominator


if __name__ == "__main__":
    n, m = map(int, input().split(" "))
    print(f"Binomial Coefficient recursive: {n}, {m} -> {cal_binomial_coefficient_recursive(n, m)}")
    print(f"Binomial Coefficient iterative: {n}, {m} -> {cal_binomial_coefficient_iterative(n, m)}")