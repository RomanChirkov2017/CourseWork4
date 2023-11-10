def get_top_n_vacancies(vacancy_list: list, n: int) -> list:
    """Функция для извлечения первых N-вакансий из списка."""
    return vacancy_list[:n]


def filter_vacancies(vacancy_list: list) -> list:
    """Функция для фильтрации вакансий."""
    return sorted(vacancy_list, key=lambda x: x.name)


def sorted_by_salary_from(vacancy_list: list) -> list:
    """Функция для сортировки вакансий по зарплате."""
    return sorted(vacancy_list, reverse=True)


def print_vacancies(vacancy_list: list) -> None:
    """Выводит информацию о вакансиях."""
    for vacancy in vacancy_list:
        print(
            f"{vacancy.name.capitalize()}\n"
            f"з/п от {vacancy.salary_from} до {vacancy.salary_to} {vacancy.currency}\n"
            f"{vacancy.url}\n"
            f"{vacancy.description}\n",
        )
