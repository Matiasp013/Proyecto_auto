from turtle import title
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#Validacion de menu

def test_validacion_menu( driver ):
    login(driver, "standard_user", "secret_sauce")

    menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))

    assert menu.is_displayed()

    menu.click()    

    logout = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='logout-sidebar-link']")))
    
    assert logout.is_displayed()