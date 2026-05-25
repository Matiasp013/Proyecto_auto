from turtle import title
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Validacion de titulo de la pantalla sea correcto (products)

def test_pantalla_inicio( driver ):
    login(driver, "standard_user", "secret_sauce")

    title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']")))


    assert title.text == "Products"