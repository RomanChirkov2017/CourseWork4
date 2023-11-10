from src.headhunter import HeadHunterAPI
from src.json_saver import JsonSaver
from src.superjob import SuperJobAPI
from src.utilites import get_top_n_vacancies, filter_vacancies, sorted_by_salary_from, print_vacancies


def main():
    """Основная функция программы."""
    platforms = ["HeadHunter", "SuperJob"]
    platform = None
    vacancies_in_json = []
    # Выбор платформы поиска
    try:
        selected_platform = int(
            input(
                '''Выберите платформу для поиска:\n 
                1 - HeadHunter\n 
                2 - SuperJob\n 
                3 - обе платформы\n'''
            )
        )
    except ValueError:
        print("Значение должно быть числом от 1 до 3.")
    else:
        while selected_platform not in [1, 2, 3]:
            try:
                selected_platform = int(input("Введено некорректное значение. Введите значение из предложенных.\n"))
            except ValueError:
                print("Значение должно быть числом от 1 до 3.")
        if selected_platform == 1:
            platform = platforms[0]
        elif selected_platform == 2:
            platform = platforms[1]
        elif selected_platform == 3:
            platform = platforms
        # Вывод сообщения о выбранной платформе
        if platform != platforms:
            print(f"Вы выбрали платформу {platform}.")
        else:
            print("Вы выбрали обе платформы из предложенных.")
        # Получение от пользователя названия вакансии
        keyword = input("Введите ключевые слова для поиска через пробел: \n").lower()
        try:
            page_count = int(input("Введите максимальное количество страниц поиска: \n"))
        except ValueError:
            print("Значение должно быть целым числом.")
            page_count = int(input("Введите максимальное количество страниц поиска: \n"))
        # Получение результатов с указанной платформы
        hh = HeadHunterAPI(keyword)
        sj = SuperJobAPI(keyword)
        if platform == "HeadHunter":
            hh.get_vacancies(page_count)
            vacancies_in_json.extend(hh.get_formatted_vacancies())
        elif platform == "SuperJob":
            sj.get_vacancies(page_count)
            vacancies_in_json.extend(sj.get_formatted_vacancies())
        elif platform == platforms:
            for api in (hh, sj):
                api.get_vacancies(page_count)
                vacancies_in_json.extend(api.get_formatted_vacancies())

        vacancies = JsonSaver(keyword, vacancies_in_json)
        filter_vac = filter_vacancies(vacancies.add_vacancy())
        print(f"\nВакансий по запросу: {len(filter_vac)}.")
        top_n = int(input("Введите количество первых по зарплате N вакансий для вывода: \n"))
        if not filter_vac:
            print("Нет вакансий, удовлетворяющих критериям поиска.")
            return

        sorted_vac = sorted_by_salary_from(filter_vac)
        top_vac = get_top_n_vacancies(sorted_vac, top_n)
        print_vacancies(top_vac)


main()
