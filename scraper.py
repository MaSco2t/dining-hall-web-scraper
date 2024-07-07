import time

from selenium.webdriver.common.by import By

def clear_pop_ups(driver):
    pop_up_1_exit = driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
    pop_up_1_exit.click()
    time.sleep(2)
    pop_up_2_exit = driver.find_element(By.CSS_SELECTOR, ".sc-hmdomO")
    pop_up_2_exit.click()

def get_meal(meal,driver):    

    select=None
    option=None
    match meal:
        case "breakfast":
            option="0"
            select="2"
        case "lunch":
            option="1"
            select="3"
        case "dinner":
            option="2"
            select="4"
    
    menu_selector = driver.find_element(By.CSS_SELECTOR,".DateMealFilterButton div")
    driver.execute_script("arguments[0].click()", menu_selector)

    menu_selector_toggle = driver.find_element(By.CSS_SELECTOR, ".css-geczwp-indicatorContainer")
    menu_selector_toggle.click()

    try:
        meal_button = driver.find_element(By.CSS_SELECTOR,"#react-select-"+select+"-option-"+option)
        meal_button.click()
    except:
        exit_button = driver.find_element(By.CSS_SELECTOR,".sc-eDPEul")
        exit_button.click()
        return
    
    done_button = driver.find_element(By.CSS_SELECTOR,".Done")
    done_button.click()
    time.sleep(4)
    print(meal.upper()+" --------------------")
    print()
    print_meal_options(driver)
    time.sleep(1)

def print_meal_options(driver):
    menu_categories = driver.find_elements(By.CSS_SELECTOR, ".MenuStation_no-categories")
    for category in menu_categories:
        section_name = category.find_element(By.CSS_SELECTOR, ".StationHeader")
        print(section_name.text.title()+":")
        menu_item_names = category.find_elements(By.CSS_SELECTOR, ".HeaderItemName")
        for item_name in menu_item_names:
            if item_name.text != "":
                print("\t"+item_name.text)
    print()