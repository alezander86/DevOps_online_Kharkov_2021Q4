# Task 8.1

** Implement a script that solves a quadratic equation of the form 𝑎𝑥ଶ + 𝑏𝑥 + 𝑐 = 0:

<details>
	<summary>solv_square_equation.py</summary>

  ```
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
  ```
</details>


<details>
	<summary>unit_test.py</summary>

  ```
import unittest
import solv_square_equation


class MyTestCase(unittest.TestCase):
    def test_discriminant(self):
        self.assertEqual(solv_square_equation.discriminant(-29, -365, 18), 135313)
        self.assertEqual(solv_square_equation.discriminant(1, 1, 1), (-3))
        self.assertEqual(solv_square_equation.discriminant(1, -4, 4), 0)

    def test_roots(self):
        self.assertEqual(solv_square_equation.roots(-8, 1, 2, 3), (None, None))
        self.assertEqual(solv_square_equation.roots(300, -7, 0, 15), (-1.237179148263484, 1.237179148263484))
        self.assertEqual(solv_square_equation.roots(0, -1, 0, 0), (0.00, None))

    def test_solv_square(self):
        self.assertEqual(solv_square_equation.solv_square(1, 2, 3), (None, None))
        self.assertEqual(solv_square_equation.solv_square(-7, 0, 15), (-1.4638501094227998, 1.4638501094227998))
        self.assertEqual(solv_square_equation.solv_square(1, 4, -4), (0.8284271247461903, -4.82842712474619))

if __name__ == '__main__':
    unittest.main()
  ```
</details>