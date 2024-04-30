import unittest
from datetime import date
from dataclasses import dataclass, asdict, field

@dataclass
class DType:
    
    @dataclass
    class _date():
        year: int
        month: int
        day: int
    
    @dataclass
    class Date(_date):
        month: int
        day: int
        
        
        

class TestDType(unittest.TestCase):
    def test_date(self):
        # Tworzymy obiekt klasy DType
        dtype_instance = DType()

        # Tworzymy obiekt daty i przypisujemy go do obiektu DType
        test_date = DType.Date([2024, 4, 25])
        dtype_instance.date = test_date

        # Sprawdzamy, czy przypisana data jest instancją klasy DType.Date
        self.assertIsInstance(dtype_instance.date, DType.Date)

        # Sprawdzamy, czy wartości daty są poprawne
        self.assertEqual(dtype_instance.date.date, [2024, 4, 25])

if __name__ == '__main__':
    unittest.main()
