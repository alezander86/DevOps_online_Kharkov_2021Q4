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