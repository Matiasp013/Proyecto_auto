from turtle import title
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Validacion que existen productos visibles en la pantalla al menos verificar uno

def test_validacion_productos( driver ):
    login(driver, "standard_user", "secret_sauce")

    productos = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))

    assert len(productos) > 0