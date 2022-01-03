import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_be_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)

    btn = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert btn, "button 'Add to busket'is missing"

