import contextlib
import io

from selenium import webdriver

import scraper
import mailer

if __name__ == "__main__":

    captured_standard_output = io.StringIO() 
    with contextlib.redirect_stdout(captured_standard_output):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options=options)
        driver.get("https://ucf.campusdish.com/en/locationsandmenus/63south//")
        driver.implicitly_wait(10)

        scraper.clear_pop_ups(driver)

        print("Greetings! Here are today's meal options!\n")
        scraper.get_meal("breakfast",driver)
        scraper.get_meal("lunch",driver)
        scraper.get_meal("dinner",driver)   

    mailer.send_email("Today's Meal Options",captured_standard_output.getvalue())
