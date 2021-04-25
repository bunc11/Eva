import unittest

from main import Eva
from main import Environment

class Test_Eva(unittest.TestCase):

    def setUp(self):
        self.e = Eva(Environment({
        'null': None,
        'true': True,
        'false': False,
        'VERSION': 0.1
    }))

    def test_numbers(self):

        self.assertEqual(self.e.eval(1), 1)

    def test_strings(self):

        self.assertEqual(self.e.eval('"string"'), '"string"')
        self.assertNotEqual(self.e.eval('"string"'), '"string1"')

    def test_addition(self):

        self.assertEqual(self.e.eval(['+', 1, 5]), 6)
        self.assertEqual(self.e.eval(['+', ['+', 3, 2], 5]), 10)
        self.assertEqual(self.e.eval(['+', ['+', 3, 2], ['+', 11 ,22]]), 38) 
        self.assertEqual(self.e.eval(['+', ['+', 3, 2], ['+', ['+', 11, 21], 22]]), 59) # same sa below, written in another form
        self.assertEqual(self.e.eval(['+', ['+', ['+', 11, 21], 22], ['+', 3, 2]]), 59) # same as above, written in another form

    def test_complex_expression(self):

        self.assertEqual(self.e.eval(['+', 2, ['*', 2, 2]]), 6)
        
        self.assertEqual(self.e.eval(['+', 2, ['*', 3, ['*', 8, ['-', 8, ['/', 16, 4]]]]]), 98) #2+3*8*8-16/4 # ovo treba popravit

        # 2 + 3 * 8 * 8 - 4 -> 8-4 -> 4 -> 8*4 -> 32 -> 3*32 -> 96 -> +2 -> 98

    def test_var_declaration_retrival(self):

        self.assertEqual(self.e.eval(['var', 'x', 10]), 10)
        self.assertEqual(self.e.eval('x'), 10)

        with self.assertRaises(ValueError):
            self.e.eval('y')

        self.assertEqual(self.e.eval(['var', 'y', 100]), 100)
        self.assertEqual(self.e.eval('y'), 100)

        self.assertEqual(self.e.eval(['var', 'x', ['*', 2, 3]]), 6)

    def test_globalEnv(self):

        self.assertEqual(self.e.eval('VERSION'), 0.1)
        self.assertEqual(self.e.eval(['var', 'user', 'true']), True)

    
unittest.main()
