from src.HHvac import HH_api_db
from src.DBManager import DBManager
from config import config
from src.utils import create_database, create_table


def main():
    params_db = config()
    create_database('HH_vacancy', params_db)
    create_table(params_db)
    db_vacancies = HH_api_db()
    db_vacancies.employers_to_db()
    db_vacancies.vacancies_to_db()


if __name__ == '__main__':
    main()
    DBManager.get_all_vacancies()
    # DBManager.get_avg_salary()
    # DBManager.get_vacancies_with_keyword('Python')
    # DBManager.get_companies_and_vacancies_count()
    # DBManager.get_vacancies_with_higher_salary()
