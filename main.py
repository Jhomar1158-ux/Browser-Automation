from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('D:\\chromeDriver\\chromedriver.exe')

def get_driver():
    """ SET OPTIONS PAR HACER LA NAVEGACIÓN MÁS FÁCIL(EASIER) """
    options = webdriver.ChromeOptions()
    # Deshabilitar información publicitaria
    options.add_argument("disable-infobars")
    # Maximizar el tamaño del navegador
    options.add_argument("start-maximized")
    # Deshabilitar problemas con Linux
    options.add_argument("disable-dev-shm-usage")
    # Si queremos que nuestro script tenga mayores privilegios.
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=service, options=options)
    # Recibimos la URL
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def main():
    driver = get_driver()
    # x_path -> 
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())
