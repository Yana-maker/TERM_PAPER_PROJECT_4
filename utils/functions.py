from utils.api_classes import HeadHunterAPI, SuperJobAPI
from utils.class_vacancies import Vacancies
import pandas as pd



def get_hh_vacancies_list(text):

    '''создание списка экземпляров клссса Vacancies'''

    data = HeadHunterAPI(text)
    data.json_file_saver()
    raw_json = data.read_json_file()
    list_vacancies = []
    for vacancy in raw_json['items']:
        name = vacancy["name"]
        area = vacancy["area"]["name"]
        try:
            salary_from = vacancy["salary"]["from"]
            salary_to = vacancy["salary"]["to"]
            if not salary_from:
                salary_from = salary_to
            if not salary_to:
                salary_to = salary_from
        except TypeError:
            salary_from = 0
            salary_to = 0

        url = vacancy["alternate_url"]
        class_vacancy = Vacancies(name, area, salary_from, salary_to, url)
        list_vacancies.append(class_vacancy)

    return list_vacancies


def get_sb_vacancies_list(text):

    '''создание списка экземпляров клссса Vacancies'''

    data = SuperJobAPI(text)
    data.json_file_saver()
    raw_json = data.read_json_file()
    list_vacancies = []
    for vacancy in raw_json['objects']:
        name = vacancy["profession"]
        area = vacancy["town"]["title"]
        try:
            salary_from = vacancy["payment_from"]
            salary_to = vacancy["payment_to"]
            if not salary_from:
                salary_from = salary_to
            if not salary_to:
                salary_to = salary_from
        except TypeError:
            salary_from = 0
            salary_to = 0

        url = vacancy["link"]
        class_vacancy = Vacancies(name, area, salary_from, salary_to, url)
        list_vacancies.append(class_vacancy)

    return list_vacancies


def user_interaction():
    """Получение вакансий по критериям пользователя с платформы"""

    search_query = input("""Введите:
1 - для поиска по платформе HeadHunter "
2 - для поиска по платформе SuperJob "
3 - для поиска по платформам HeadHunter и SuperJob\n""")

    vacancies_list = []
    if search_query == "1":
        filter_words = input("Введите ключевое слово для фильтрации вакансий: ").split()
        vacancies_list = get_hh_vacancies_list(filter_words)


    elif search_query == "2":
        filter_words = input("Введите ключевое слово для фильтрации вакансий: ").split()
        vacancies_list = get_sb_vacancies_list(filter_words)

    elif search_query == "3":
        filter_words = input("Введите ключевое слово для фильтрации вакансий: ").split()
        vacancies_list = get_sb_vacancies_list(filter_words) + get_hh_vacancies_list(filter_words)

    else:
        print('По данной платформе поиск не осуществляется')



    user_choice = input('''Введите: 
1 - для сортировки вакансий по ЗП: 
2 - для вывода топ 10 вакансий:
3 - для сортировки вакансий по городу:
''')

    if user_choice == '1':
        all_name = []
        all_city = []
        all_salary_from = []
        all_salary_to = []
        all_url = []

        for vacancies in sorted(vacancies_list, reverse=True):

            all_name.append(vacancies.name)
            all_city.append(vacancies.area)
            all_url.append(vacancies.url)
            all_salary_from.append(vacancies.salary_from)
            all_salary_to.append(vacancies.salary_to)

            df = pd.DataFrame(
                dict(специальность=all_name, город=all_city, ссылка=all_url, ЗП_от=all_salary_from, ЗП_до=all_salary_to)
            )
            df.to_excel('../src/file.xlsx')
            print(vacancies)



    elif user_choice == '2':
        all_name = []
        all_city = []
        all_salary_from = []
        all_salary_to = []
        all_url = []

        for vacancies in sorted(vacancies_list, reverse=True)[:10]:
            all_name.append(vacancies.name)
            all_city.append(vacancies.area)
            all_url.append(vacancies.url)
            all_salary_from.append(vacancies.salary_from)
            all_salary_to.append(vacancies.salary_to)

            df = pd.DataFrame(
                dict(специальность=all_name, город=all_city, ссылка=all_url, ЗП_от=all_salary_from, ЗП_до=all_salary_to)
            )
            df.to_excel('../src/file.xlsx')
            print(vacancies)

    elif user_choice == '3':
        user_city = input('Введите город для сортировки')
        all_name = []
        all_city = []
        all_salary_from = []
        all_salary_to = []
        all_url = []


        for vacancies in vacancies_list:
            if vacancies.area == user_city:
                all_name.append(vacancies.name)
                all_city.append(vacancies.area)
                all_url.append(vacancies.url)
                all_salary_from.append(vacancies.salary_from)
                all_salary_to.append(vacancies.salary_to)

                df = pd.DataFrame(
                    dict(специальность=all_name, город=all_city, ссылка=all_url, ЗП_от=all_salary_from, ЗП_до=all_salary_to)
                )

                df.to_excel('../src/file.xlsx')
                print(vacancies)

