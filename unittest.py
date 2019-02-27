import calculator
import unittest

class testStringMethods(testunittest.TestCase):

    def testAddTest(self): 
        self.assertEqual(calculator.add(3,9), 12)
        self.assertEqual(calculator.add(4,2), 6)
        self.assertEqual(calculator.add (7,8), 15)

    def testSubtractTest(self):
        self.assertEqual(calculator.subtract (7,5), 2)
        self.assertEqual(calculator.subtract (4,2), 2)
        self.assertEqual(calculator.subtract (8,3), 11)


    def testMultiplyTest(self):
        self.assertEqual(calculator.multiply(5,3), 15)
        self.assertEqual(calculator.multiply(2,8), 16)
        self.assertEqual(calculator.multiply(7,6), 42)

    def testDivideTest(self):
        self.assertEqual(calculator.divide(100,2), 50)
        self.assertEqual(calculator.divide (8 ,2), 4)
        self.assertEqual(calculator.divide(25,5), 5)
    


if_name_== '_main_':
unittest.main()