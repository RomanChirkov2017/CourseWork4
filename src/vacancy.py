class Vacancy:

    def __init__(
            self, name: str, url: str, salary_from: float, salary_to: float, currency: str, description: str
    ) -> None:
        """Инициализатор класса Vacancy"""
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description

    def __repr__(self) -> str:
        """Строковое представление обЪекта"""
        return f"Вакансия: {self.name}, Зп: {self.salary_from} - {self.salary_to} {self.currency}."

    def __eq__(self, other) -> bool:
        """Проверка равенства обЪектов класса Vacancy."""
        return self.salary_from == other.salary_from

    def __lt__(self, other) -> bool:
        """Проверяет, является ли один обЪект класса Vacancy меньше другого обЪекта этого класса."""
        return self.salary_from < other.salary_from

    def __gt__(self, other) -> bool:
        """Проверяет, является ли один обЪект класса Vacancy больше другого обЪекта этого класса."""
        return self.salary_from > other.salary_from
