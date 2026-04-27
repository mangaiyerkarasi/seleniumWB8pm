from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def main():
    options = Options()
    options.add_argument("--start-maximized")

    # Selenium Manager will download the matching ChromeDriver automatically.
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.google.com")
        print("Opened google.com successfully")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
