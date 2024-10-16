SYMBOL_PRIORITY_MAP = {"+": 2, "-": 2, "*": 3, "/": 3, "(": 1, ")": 1}


def transform_infix_to_prefix(infix_string: str) -> str:
    prefix_string = ""
    stack = []
    for s in infix_string[::-1]:
        if s.isalpha():
            prefix_string += s
        elif s == ")":
            stack.append(s)
        elif s == "(":
            while stack and stack[-1] != ")":
                prefix_string += stack.pop()
            stack.pop()
        else:
            while stack and SYMBOL_PRIORITY_MAP[stack[-1]] >= SYMBOL_PRIORITY_MAP[s]:
                prefix_string += stack.pop()
            stack.append(s)

    while stack:
        prefix_string += stack.pop()
    
    return prefix_string[::-1]


def transform_prefix_to_infix(prefix_string: str) -> str:
    stack = []
    for s in prefix_string[::-1]:
        if s.isalpha():
            stack.append(s)
        else:
            operator_1 = stack.pop()
            operator_2 = stack.pop()
            stack.append(f"({operator_1}{s}{operator_2})")
    
    return stack[0]


if __name__ == "__main__":
    infix_string = "A/(B-C*D)"
    prefix_string = transform_infix_to_prefix(infix_string)   # /A-B*CD
    print(f"infix string: {infix_string} -> prefix string: {prefix_string}")

    infix_string = transform_prefix_to_infix(prefix_string)   # (A/(B-(C*D)))
    print(f"postfix string: {prefix_string} -> infix string: {infix_string}")

    infix_string = "(A+(B-C)/D)-E/(F*G)"
    prefix_string = transform_infix_to_prefix(infix_string)   # -+A/-BCD/E*FG
    print(f"infix string: {infix_string} -> prefix string: {prefix_string}")

    infix_string = transform_prefix_to_infix(prefix_string)   # ((A+((B-C)/D))-(E/(F*G)))
    print(f"postfix string: {prefix_string} -> infix string: {infix_string}")
