import requests
from exception import ParsingError


class HeadHunter():
    """Создаем класс для парсинга с HeadHunter """

    url = 'https://api.hh.ru/vacancies'


    def __init__(self, keyword):
        """Инициализируем объект класса"""

        self.params = {
            "per_page": 50,
            "page": None,
            "text": keyword,
        }
        self.headers = {}


    def __str__(self):
        return "Создаем объект класса HeadHunter для получения данных о вакансиях с hh.ru"



    def get_requests(self):
        """Получаем данные"""

        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise ParsingError(f'Ошибка получения вакансий! Статус {response.status_code}')
        return response.json()["items"]


    def get_formatted_vacancies(self):
        """Получаем список словарей с выбранными полями"""

        formatted_vacancies = []
        vacancies = self.get_requests()
        for vacancy in vacancies:
            formatted_vacancy = {
                "title_id": vacancy["id"],
                "title_city": vacancy["area"]["name"],
                "employer_id": vacancy['employer']['id'],
                "employer": vacancy['employer']['name'],
                "title": vacancy["name"],
                "url": vacancy["alternate_url"],
            }

            salary = vacancy["salary"]
            if salary:
               formatted_vacancy["salary_from"] = salary['from']
               formatted_vacancy["salary_to"] = salary["to"]
               formatted_vacancy["currency"] = salary["currency"]
            else:
                formatted_vacancy["salary_from"] = None
                formatted_vacancy["salary_to"] = None
                formatted_vacancy["currency"] = None
            formatted_vacancies.append(formatted_vacancy)

        return formatted_vacancies



