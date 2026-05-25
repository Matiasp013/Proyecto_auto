from turtle import title
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    #Validacion de Login exitoso

def test_login( driver ):
    login(driver, "standard_user", "secret_sauce")


    assert "inventory.html" in driver.current_url

    