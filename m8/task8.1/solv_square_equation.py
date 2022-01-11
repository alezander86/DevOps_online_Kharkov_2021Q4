import math

def validate_param():
    attepmts = 3
    while attepmts > 0:
        try:
            print(f'you have {attepmts} attepmts')
            a = int(input("Enter value for a: "))
            b = int(input("Enter value for b: "))
            c = int(input("Enter value for c: "))
        except ValueError:
            print(f"Value is not integer, try again.")
            attepmts -= 1
            validate_param(a, b, c)
            continue
        else:
            return a, b, c

def discriminant( a, b, c):
    return b ** 2 - 4 * a * c

def roots(discr, a, b, с):
    if a == 0:
        print("cannot be multiplied by 0")
    elif discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return x1, x2
    elif discr == 0:
        x1 = -b / (2 * a)
        return x1, None
    else:
        return (None, None)

def solv_square(a, b, c) -> roots:
    discr = discriminant(a, b, c)
    return roots(discr, a, b, c)

def square_print(a, b, c, roots, discriminant):
    x1, x2 = roots
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print(f"discriminant = {discriminant}")
    if x2 == (None):
        print(f"x1 = {x1}")
    elif x1 != (None) and x2 != (None):
        print(f"x1 = {x1} and x2 ={x2}")
    else:
        print(f"Square have no roots")


def main():
    print("Please enter values for equation:")
    valid_params = validate_param()
    a = valid_params[0]
    b = valid_params[1]
    c = valid_params[2]
    square_print(a, b, c, roots (discriminant(a, b, c), a, b, c), discriminant(a, b, c))

if __name__ == "__main__":
    main()