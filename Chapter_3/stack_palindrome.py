def is_palindrome(string: str) -> bool:
    length = len(string)
    for i in range(length//2):
        if string[i] != string[length-i-1]:
            return False
        
    return True


if __name__ == "__main__":
    input_string = "abcab"
    print(f"Is '{input_string}' palindrome -> {is_palindrome(input_string)}")

    input_string = "abcba"
    print(f"Is '{input_string}' palindrome -> {is_palindrome(input_string)}")

    input_string = "abba"
    print(f"Is '{input_string}' palindrome -> {is_palindrome(input_string)}")

    input_string = "abca"
    print(f"Is '{input_string}' palindrome -> {is_palindrome(input_string)}")
