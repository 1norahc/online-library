from dataclasses import dataclass

class Utils:
    class ReleaseDate:
        def __init__(self, year: int, month: int, day: int):
            self.year = year
            self.month = month
            self.day = day

        @classmethod
        def from_string(cls, date_str: str):
            year, month, day = map(int, date_str.split('-'))
            return cls(year, month, day)

        def is_valid(self):
            try:
                self.to_datetime()
                return True
            except ValueError:
                return False

        def to_datetime(self):
            from datetime import datetime
            return datetime(self.year, self.month, self.day)

        def __str__(self):
            return f"{self.year}-{self.month:02d}-{self.day:02d}"


        


"""# Użycie:

release_date = Utils().ReleaseDate(2024, 4, 25)
print("Release date:", release_date)  # Wyświetli: Release date: 2024-04-25

release_date_str = "2024-04-25"
release_date_from_str = release_date.from_string(release_date_str)
print("Release date from string:", release_date_from_str)  # Wyświetli: Release date from string: 2024-04-25

print("Is valid?", release_date.is_valid())  # Wyświetli: Is valid? True

print(Utils().ReleaseDate(20232, 23, 20).__str__())
"""