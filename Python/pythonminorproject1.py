print("=== CLI Calculator ===")
print("Supports multiple operations: +, -, *, /")
print("Type 'exit' to quit\n")

while True:
    expr = input("Enter expression: ").strip()

    if expr.lower() == "exit":
        print("Goodbye!")
        break

        
    expr = expr.replace(" ", "")

    allowed_chars = "0123456789+-*/."
    if not all(c in allowed_chars for c in expr):
        print("Invalid characters! Use only numbers and + - * /")
        continue
    
    try:
        
        result = eval(expr)
        print(f"Result: {result}")
    except ZeroDivisionError:
            print("Division by zero is not allowed!")
    except Exception:
            print("❌ Invalid expression! Try again.")
