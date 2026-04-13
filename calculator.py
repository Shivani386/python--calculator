while True:
    print("\n1.Add 2.Sub 3.Mul 4.Div 5.Exit")
    ch = input("Choice: ")

    if ch == '5':
        break

    a , b = float(input("A: ")), float(input("B: "))

    if ch == '1': print("Result =", a + b)
    elif ch == '2': print("Result =", a - b)
    elif ch == '3': print("Result =", a * b)
    elif ch == '4': print("Result =", "Error" if b == 0 else a / b)
    else: print("Invalid choice")
