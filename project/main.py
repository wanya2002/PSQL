from connect import HeadHunter
from utils import DBManager


def main():

    sum = []
    sum1 = []
    while True:
        keyword = input('Введите название компании\nили введите 1 для выхода\n')
        if keyword == '1':
            break
        else:
            ob = HeadHunter(keyword)
            res = ob.get_formatted_vacancies()
            sum.append(res[0])
            for el in res:
                sum1.append(el)

    obj = DBManager()
    obj.create_tables()
    obj = DBManager()
    obj.compl_data(sum, sum1)
    while True:
        num = input('Выберите из списка:\n1 - получить список всех компаний и количество вакансий у каждой\n'
                '2 - получить список всех вакансий с указанием названия компании, '
                'названия вакансии и зарплаты и ссылки на вакансию\n'
                '3 - получить среднюю зарплату по вакансиям\n'
                '4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям\n'
                '5 - получить список всех вакансий, в названии которых содержатся переданные в метод слова\n'
                '6 - выйти из программы\n')
        if num == '1':
            obj = DBManager()
            res = obj.get_companies_and_vacancies_count()
            for el in res:
                print(el)
        elif num == '2':
            obj = DBManager()
            res = obj.get_all_vacancies()
            for el in res:
                print(el)
        elif num == '3':
            obj = DBManager()
            res = obj.get_avg_salary()
            print(res)
        elif num == '4':
            obj = DBManager()
            res = obj.get_vacancies_with_higher_salary()
            for el in res:
                print(el)
        elif num == '5':
            obj = DBManager()
            key = input('Введите слово для поиска вакансии\n')
            res = obj.get_vacancies_with_keyword(key)
            for el in res:
                print(el)
        elif num == '6':
            quit()


if __name__ == "__main__":
    main()

