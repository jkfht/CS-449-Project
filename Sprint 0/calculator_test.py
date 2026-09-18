""" Test module for calculator.py """

import unittest
import calculator
from PySide6.QtWidgets import QApplication
import sys

APP = QApplication(sys.argv)
CALC = calculator.CalculatorApp()

class CalcTest(unittest.TestCase):
    def test_number_press(self):
        for i in range(10):
            with self.subTest(i):
                existing_text = CALC.display.text()
                CALC.autoButton(i)
                self.assertEqual(CALC.display.text(), existing_text + str(i))

    def test_clear_text(self):
        CALC.autoButton(4)
        CALC.autoButton('C')
        self.assertEqual(CALC.display.text(), '')

    def test_clear_empty(self):
        CALC.autoButton('C')
        self.assertEqual(CALC.display.text(), '')

    def test_add(self):
        CALC.autoButton(3)
        CALC.autoButton('+')
        CALC.autoButton(9)
        CALC.autoButton('=')
        self.assertEqual(CALC.display.text(), '12')

    def test_div_zero(self):
        CALC.autoButton('C')
        CALC.autoButton('3')
        CALC.autoButton('/')
        CALC.autoButton('0')
        CALC.autoButton('=')
        self.assertEqual(CALC.display.text(),"Error")

if __name__ == '__main__':
    unittest.main()
