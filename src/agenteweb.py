import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL_IMAGEM = Path(__file__).parent.parent / "imgs" / "asuka.jpg"

def postar_status():

    options = Options()
    options.add_argument("-profile")
    options.add_argument(
        "/home/iggy/.config/mozilla/firefox/o4ovhji8.default-release"
    )

    driver = webdriver.Firefox(options=options)
    driver.get("https://web.whatsapp.com")

    wait = WebDriverWait(driver, 20)

    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Status"]'))
    )

    time.sleep(2)

    if button:
        button.click()

    time.sleep(2)

    add_status = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Add Status"]'))
    )

    if add_status:
        add_status.click()

    time.sleep(2)

    add_image = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Fotos e vídeos"]'))
    )

    if add_image:
        add_image.click()

    input = driver.find_element(
        By.CSS_SELECTOR, "input[type='file']"
    )

    #print("Inputs encontrados:", len(inputs)) Para debuggar

    input.send_keys(str(URL_IMAGEM.resolve()))

    time.sleep(2)

    enviar = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-label="Enviar 1 item selecionado"]'))
    )

    if enviar:
        enviar.click()

    wait_envio = WebDriverWait(driver, 20)

    _ = wait_envio.until(
        EC.invisibility_of_element_located(
            (By.XPATH, "//*[normalize-space(text())='Enviando...']")
        )
    )

    time.sleep(5)

    driver.quit()
