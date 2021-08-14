#!/usr/bin/env python3
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Base Methods to use in framework.

class Util():

    def __init__(self, driver):
        self.driver = driver

    # click function on element passed to it when element visibility of is located.
    def click(self, locator: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()
    
    # assert compare of text from a web element vs test element text.
    def assert_el_text(self, locator: str, el_text: str):
        web_el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        assert web_el.text == el_text
    
    # returns a bool depending if visible or not.
    def is_visible(self, locator: str):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(element)

    # hovers mouse over element passed too.
    def hover_to(self, locator: str):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()




#     def find_element_by(self, element_methods: str, element: str):
#         #! from selenium.webdriver.common.by import By
#         # element_name: exp. => by_id ...etc
#         # enter name
#         # passes correct suffix
#         # element: name of specific
#         # {element_name} you chosen
#         pass

#     def test(self, element_name):

#         element_names = {
#             "class_name": By.CLASS_NAME,
#             "css_selector": By.CSS_SELECTOR,
#             "id": By.ID,
#             "link_text": By.LINK_TEXT,
#             "partial_link_text": By.LINK_TEXT,
#             "partial_link": By.LINK_TEXT,
#             "xpath": By.XPATH,
#         }

#         if element_name in element_names:
#             print(element_name)
            
#         else:
#             print('wrong')

# c = Util(driver=1)

# c.test('partial_link')
            


