from abc import ABC, abstractmethod
import requests
import json


class AbstractClassApi(ABC):

    @abstractmethod
    def json_file_saver(self):
        pass

    @abstractmethod
    def read_json_file(self):
        pass



class HeadHunterAPI(AbstractClassApi):

    def __init__(self, text):
        self.text = text

    def json_file_saver(self):

        """сохранение данных в json файл
        через range пытаюсь сохранить больше вакансий , но получается макисмум 100 шт"""

        for i in range(3):
            params = {
                'text': self.text,
                'per_page': 100,
                'page': i

            }
            response = requests.get('https://api.hh.ru/vacancies', params=params).json()
            with open('../src/HeadHunterAPI_response.json', 'w', encoding='UTF-8') as file:
                json.dump(response, file, indent=4, ensure_ascii=False)

    def read_json_file(self):

        """чтение файла json"""

        with open(f'../src/HeadHunterAPI_response.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data


class SuperJobAPI(AbstractClassApi):
    def __init__(self, text):
        self.text = text

    def json_file_saver(self):

        """сохранение данных в json файл"""

        for i in range(3):
            params = {
                'keywords': self.text,
                'count': 100,
                'page': i,
            }
            headers = {
                    'X-Api-App-Id': 'v3.r.124995159.800c8b31cf2ba10edba29ad69698637a5aeee7e8.6d5300f67dae85418bfe62f339f1b10412aba8a0'
            }
            response = requests.get('https://api.superjob.ru/2.0/vacancies', headers=headers, params=params).json()
            with open('../src/SuperJobAPI_response.json', 'w', encoding='UTF-8') as file:
                json.dump(response, file, indent=4, ensure_ascii=False)

    def read_json_file(self):

        """чтение файла json"""

        with open(f'../src/SuperJobAPI_response.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data






