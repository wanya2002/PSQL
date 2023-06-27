import psycopg2

class DBManager():

    def __init__(self):
        """Инициализируем объект класса"""

        self.conn = psycopg2.connect(
        host='localhost',
        port='5433',
        database='north',
        user='postgres',
        password='Power6789012345'
        )


    def create_tables(self):
        """Создание таблиц для работы с базой данных"""
        try:
           with self.conn:
               with self.conn.cursor() as cur:
                   cur.execute("""
                       CREATE TABLE employees (
                       emp_id INTEGER PRIMARY KEY,
                       name VARCHAR(100))
                       """)

                   cur.execute("""
                       CREATE TABLE vacancies (
                       vac_id INTEGER PRIMARY KEY,
                       name VARCHAR(100),
                       city VARCHAR(20),
                       salary_from INTEGER,
                       salary_to INTEGER,
                       currency CHAR(5),
                       vacancy_url TEXT,
                       emp_id INTEGER REFERENCES employees(emp_id) ON DELETE CASCADE)
                        """)
        finally:
          self.conn.close()


    def compl_data(self, data, data1):
        """Функция заполнения данными таблиц базы данных"""
        try:
           with self.conn:
               with self.conn.cursor() as cur:
                   for el in data:
                       cur.execute("INSERT INTO employees VALUES(%s, %s)",
                               [el["employer_id"], el["employer"]])
                   for el in data1:
                       cur.execute("INSERT INTO vacancies VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",
                                   [el["title_id"], el["title"], el["title_city"], el["salary_from"],
                                    el["salary_to"], el["currency"], el["url"], el["employer_id"]])
        finally:
           self.conn.close()


    def get_companies_and_vacancies_count(self):
        """Функция получает список всех компаний и количество вакансий по каждой компании"""
        try:
           with self.conn:
               with self.conn.cursor() as cur:
                   cur.execute("SELECT employees.name, COUNT(*) AS kol_vac FROM employees "
                               "INNER JOIN vacancies USING(emp_id) "
                               "GROUP BY employees.name")
                   rows = cur.fetchall()
                   return rows
        finally:
           self.conn.close()


    def get_all_vacancies(self):
        """Функция возвращает список всех вакансий с указанием названия компании,
         названия вакансии и зарплаты и ссылки на вакансию"""
        try:
           with self.conn:
               with self.conn.cursor() as cur:
                   cur.execute("SELECT vacancies.vac_id, vacancies.name, employees.name, salary_from, vacancy_url "
                               "FROM employees INNER JOIN vacancies USING(emp_id)")
                   rows = cur.fetchall()
                   return rows
        finally:
           self.conn.close()


    def get_avg_salary(self):
        """Функция возвращает среднюю зарплату по вакансиям"""
        try:
           with self.conn:
               with self.conn.cursor() as cur:
                   cur.execute("SELECT round((AVG(salary_from)),2) FROM vacancies")
                   rows = cur.fetchone()
                   return rows
        finally:
           self.conn.close()


    def get_vacancies_with_higher_salary(self):
        """Функция возвращает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        try:
           with self.conn:
               with self.conn.cursor() as cur:
                   cur.execute("SELECT * FROM vacancies WHERE salary_from > (SELECT round((AVG(salary_from)),2) FROM vacancies)")
                   rows = cur.fetchall()
                   return rows
        finally:
           self.conn.close()


    def get_vacancies_with_keyword(self, word):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        try:
           with self.conn:
               with self.conn.cursor() as cur:
                   cur.execute(f"SELECT * FROM vacancies WHERE vacancies.name LIKE '%{word}%'")
                   rows = cur.fetchall()
                   return rows
        finally:
           self.conn.close()













