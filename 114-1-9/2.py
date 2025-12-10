def apply_ops(n_str: str, ops: str) -> str:
    s = n_str
    for op in ops:
        if op == '+':
            x = int(s) + 1
            s = str(x)
            s = s[-1] + s[:-1]
        elif op == '-':
            x = int(s) - 1
            s = str(x)
            s = s[1:] + s[0]
        else:
            continue
    return s

if __name__ == "__main__":
    n = input().strip()
    ops = input().strip()
    result = apply_ops(n, ops)
    print(int(result))