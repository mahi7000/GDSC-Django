try:
    def basic_operations(a, b):
        add = int(a + b)
        subtract = int(a - b)
        multiply = int(a * b)

        try:
            divide = int(a / b)
        except ZeroDivisionError:
            print("Divisor can't be Zero")


        oper_dict = {"Addition": add, "Subtraction": subtract, "Multiplication": multiply, "Division": divide}

        return (oper_dict)

    def power_operation(base, exponent, **kwargs):
        power = base ** exponent

        try:
            if "modulo" in kwargs:
                power %= kwargs["modulo"]
        except ZeroDivisionError:
            print("Divisor can't be Zero")

        return (power)

except ValueError:
    print("Please input only numbers")

def apply_operations(operation_list):
    results = list(map(lambda x: x[0](*x[1]), operation_list))
    
    return results