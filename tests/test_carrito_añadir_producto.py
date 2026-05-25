from turtle import title
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Agregar producto al carrito 

def test_agregar_producto_carrito( driver ):
    login(driver, "standard_user", "secret_sauce")

    añadir_producto = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    
    añadir_producto.click()
