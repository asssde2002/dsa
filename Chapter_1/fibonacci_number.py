
def cal_fibonacci_number_recursive(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return cal_fibonacci_number_recursive(num-1) + cal_fibonacci_number_recursive(num-2)


def cal_fibonacci_number_iterative(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        prev_prev_val = 0
        prev_val = 1
        res = 1
        for _ in range(2, num+1):
            res = prev_prev_val + prev_val
            prev_prev_val = prev_val
            prev_val = res
        
        return res


if __name__ == "__main__":
    num = int(input())
    print(f"Fibonacci number recursive: {num} -> {cal_fibonacci_number_recursive(num)}")
    print(f"Fibonacci number iterative: {num} -> {cal_fibonacci_number_iterative(num)}")
