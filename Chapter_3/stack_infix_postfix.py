SYMBOL_PRIORITY_MAP = {"+": 2, "-": 2, "*": 3, "/": 3, "(": 1, ")": 1}


def transform_infix_to_postfix(infix_string: str) -> str:
    postfix_string = ""
    stack = []
    for s in infix_string:
        if s.isalpha():
            postfix_string += s
        elif s == "(":
            stack.append(s)
        elif s == ")":
            while stack and stack[-1] != "(":
                postfix_string += stack.pop()
            stack.pop()
        else:
            while stack and SYMBOL_PRIORITY_MAP[stack[-1]] >= SYMBOL_PRIORITY_MAP[s]:
                postfix_string += stack.pop()
            stack.append(s)

    while stack:
        postfix_string += stack.pop()
    
    return postfix_string


def transform_postfix_to_infix(postfix_string: str) -> str:
    stack = []
    for s in postfix_string:
        if s.isalpha():
            stack.append(s)
        else:
            operator_2 = stack.pop()
            operator_1 = stack.pop()
            stack.append(f"({operator_1}{s}{operator_2})")
    
    return stack[0]


if __name__ == "__main__":
    infix_string = "A/(B-C*D)"
    postfix_string = transform_infix_to_postfix(infix_string)   # ABCD*-/
    print(f"infix string: {infix_string} -> postfix string: {postfix_string}")

    infix_string = transform_postfix_to_infix(postfix_string)   # (A/(B-(C*D)))
    print(f"postfix string: {postfix_string} -> infix string: {infix_string}")

    infix_string = "(A+(B-C)/D)-E/(F*G)"
    postfix_string = transform_infix_to_postfix(infix_string)   # ABC-D/+EFG*/-
    print(f"infix string: {infix_string} -> postfix string: {postfix_string}")

    infix_string = transform_postfix_to_infix(postfix_string)   # ((A+((B-C)/D))-(E/(F*G)))
    print(f"postfix string: {postfix_string} -> infix string: {infix_string}")
