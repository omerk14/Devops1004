from selenium import webdriver

def calculte_tip(my_driver):
    my_driver.get("C:/Users/User/Downloads/tip_calc/tip_calc/index.html")
    my_driver.find_element_by_id("billamt").send_keys("100")
    my_driver.find_element_by_xpath("//*[@id=\"serviceQual\"]/option[3]").click()
    my_driver.find_element_by_id("peopleamt").send_keys(4)
    my_driver.find_element_by_id("calculate").click()
    return  my_driver.find_element_by_id("tip").text


my_driver = webdriver.Chrome(executable_path="/Users/User/Downloads/Chromedriver")

expected = "6.0"
assert calculte_tip(my_driver) != expected
# if expected == actual:
#     print("all good")
# else:
#     print("you broke the test")

#my_driver.get("http://github.com")