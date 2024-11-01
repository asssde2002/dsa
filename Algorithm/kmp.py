def kmp(s: str) -> int:
    # string matching algorithm
    # TC: O(n), SC: O(n)
    next_list = [0] * len(s)
    i = 1
    prefix_len = 0
    while i < len(s):
        if s[i] == s[prefix_len]:
            prefix_len += 1
            next_list[i] = prefix_len
            i += 1
        else:
            if prefix_len > 0:
                prefix_len = next_list[prefix_len-1]
            else:
                next_list[i] = 0
                i += 1
    
    return next_list


if __name__ == "__main__":
    string = "abcde#abbabcde"
    next_list = kmp(string)
    print(f"string ({string}):", next_list)
    # [0, 0, 0, 0, 0, 0, 1, 2, 0, 1, 2, 3, 4, 5]
