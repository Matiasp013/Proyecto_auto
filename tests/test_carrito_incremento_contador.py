from turtle import title
from conftest import driver
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Iniciamos sesion 

def test_validar_aumento_carrito( driver ):
    login(driver, "standard_user", "secret_sauce")

    #Validamos el contador del carrito antes de agregar el producto

    carrito_vacio = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")

    assert carrito_vacio.text == ""

    #Agregamos el producto al carrito

    agregar_producto = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    
    agregar_producto.click()

    #Validamos que el contador del carrito aumento a 1

    carrito_con_producto = driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")

    assert carrito_con_producto.text == "1"
