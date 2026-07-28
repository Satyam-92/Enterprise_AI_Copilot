from services.scraper_service import run_scraper


def main():
    run_scraper()
    print("ETL Pipeline executed successfully!")


if __name__ == "__main__":
    main()