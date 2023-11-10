import json


from src.abstract_classes import FileSaver
from src.vacancy import Vacancy

class JsonSaver(FileSaver):
    """Класс для работы с json-файлом."""

    def __init__(self, keyword, vacancies_json) -> None:
        """Инициализатор класса JsonSaver"""
        self.keyword = keyword
        self.filename = "vacancies_JSON.json"
        self.save_data(vacancies_json)
        self.vacancy_list = []

    def save_data(self, vacancies_json) -> None:
        """Запись данных в json-файл."""
        with open(self.filename, "w", encoding="UTF-8") as file:
            json.dump(vacancies_json, file, indent=4, ensure_ascii=False)

    def add_vacancy(self) -> list:
        """Добавляет вакансии в список vacancy_list."""
        with open(self.filename, "r", encoding="UTF-8") as file:
            vacancies = json.load(file)

        for vacancy in vacancies:
            new_vacancy = Vacancy(
                vacancy['name'],
                vacancy['url'],
                vacancy['salary_from'],
                vacancy['salary_to'],
                vacancy['currency'],
                vacancy['description'],
            )
            self.vacancy_list.append(new_vacancy)
        return self.vacancy_list

    def del_vacancy(self) -> None:
        """Удаляет данные о вакансиях из json-файла."""
        with open(self.filename, "w") as file:
            json.dump("", file, indent=4, ensure_ascii=False)
