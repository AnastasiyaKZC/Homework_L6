from selene import browser


def test_fill_form():
    # Заполняю личные данные
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").type("Анастасия")
    browser.element("#lastName").type("Кузнецова")
    browser.element("#userEmail").type("kuznetsova@mail.com")