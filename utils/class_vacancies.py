
class Vacancies:


    def __init__(self, name, area, salary_from, salary_to, url):
        self.__name = name
        self.__area = area
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__url = url



    @property
    def name(self):
        return self.__name

    @property
    def area(self):
        return self.__area

    @property
    def url(self):
        return self.__url

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    def __str__(self):
        return f'{self.__name}\n{self.__area}\n{self.__salary_from}\n{self.__url}\n'


    def __eq__(self, other):
        if not isinstance(other, Vacancies):
            print('нет данных для сравнения')
        else:
            return self.__salary_to == other.__salary_to

    def __lt__(self, other):
        if not isinstance(other, Vacancies):
            print('нет данных для сравнения')
        else:
            return self.__salary_to < other.__salary_to

    def __le__(self, other):
        if not isinstance(other, Vacancies):
             print('нет данных для сравнения')
        else:
            return self.__salary_to <= other.__salary_to

    def __ge__(self, other):
        if not isinstance(other, Vacancies):
            print('нет данных для сравнения')
        else:
            return self.__salary_to >= other.__salary_to






