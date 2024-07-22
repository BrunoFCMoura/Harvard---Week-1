def main():
    expression = (input('Expression: ')).strip()

    x, y, z = expression.split()

    x = int(x)
    z = int(z)

    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z
    else:
        raise ValueError("Unknown operator")

    print(f"{result:.1f}")

main()


