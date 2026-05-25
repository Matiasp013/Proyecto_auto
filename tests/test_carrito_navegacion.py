from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


#Agregar producto al carrito 

def test_agregar_producto_carrito( driver ):
    login(driver, "standard_user", "secret_sauce")

    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    assert "cart.html" in driver.current_url