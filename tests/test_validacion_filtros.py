from turtle import title
from conftest import driver
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Validacion de titulo de la pantalla sea correcto (products)

def test_validacion_filtros( driver ):
    login(driver, "standard_user", "secret_sauce")

    filtro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
    
    select = Select(filtro)
    select.select_by_value("lohi")
