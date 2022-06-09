from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Ubicación del chromedrive local para aplicaciones de Selenium
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
    # Hacemos la solicitud a la siguiente URL
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def clean_text(text):
    # Nos quedamos solo con el número usando split() para recortarlo 
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    # El número que queremos aparece luego de 2 seg en el navegador por lo que debemos usar sleep para
    # esperar a que aparezca y capturarlo
    time.sleep(3)
    # Accedemos a la etiqueta que contiene nuestro texto
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    # Convertimos a TEXTO usando la propiedad text
    return clean_text(element.text)

print(main())
