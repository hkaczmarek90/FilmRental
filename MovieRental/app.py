from typing import Tuple


class User:
    def __init__(self, ID, First, Last, Email, Is_active=True):
        self._ID = ID
        self._First = First
        self._Last = Last
        self._Email = Email
        self._Is_active = Is_active

    def get_ID(self) -> int:
        return self._ID

    def get_name(self) -> str:
        return self._First

    def get_last(self) -> str:
        return self._Last

    def get_email(self) -> str:
        return self._Email

    def is_active(self) -> bool:
        return self._Is_active


class Movie:
    def __init__(self, ID, Title, Year, Rating):
        self._ID = ID
        self._Title = Title
        self._Year = Year
        self._Rating = Rating

    def get_ID(self) -> int:
        return self._ID

    def get_title(self) -> str:
        return self._Title

    def get_Year(self) -> int:
        return self._Year

    def get_Ratio(self) -> float:
        return self._Rating

    def __str__(self):
        return f'{self._ID}|{self._Title}|{self._Year}|{self._Rating}\n'

    def __repr__(self):
        return self.get_title() + ' ' + self.get_Ratio()


class MovieRentalSystem:
    def add_movie(self, movie: Movie):
        with open('movie_db.txt', 'a+') as f:
            f.write(str(movie))

    def get(self, id) -> Movie:
        with open('movie_db.txt', 'r+') as u:
            for line in u:
                splitted = line.split('|')
                if id == int(splitted[0]):
                    return Movie(*splitted)
        raise ValueError("Movie doesn't exist")

    def show(self) -> Tuple[Movie]:
        with open('movie_db.txt', 'r+') as read_handler:
            library = []
            for line in read_handler:
                library.append(Movie(*line.split('|')))
            return tuple(library)


def what_do():
    while True:
        entrypoint = str(input('Welcome, what do you want to do in Rental system ?'))
        if entrypoint.lower() == 'show':
            print(f'Avaliable movies :\n')
            for move in system.show():
                print(move)


system = MovieRentalSystem()
what_do()
