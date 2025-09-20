import os
import allure
from selene.support.shared import browser
from selene import be, have
from utils import attach

IMAGE_PATH = os.path.join(os.path.dirname(__file__), 'resources/picture.jpg')

@allure.title("Filled registration form")
def test_fill_form(setup_browser):
    browser.open("/automation-practice-form")

    attach.add_screenshot(browser)

    with allure.step("Filled name and surname"):
        browser.element('[id="firstName"]').should(be.visible).type("Alisha")
        browser.element('[id="lastName"]').should(be.visible).type("Meier")

    with allure.step("Filled email"):
        browser.element('[id="userEmail"]').should(be.visible).type("alisha.meyerr@gmail.com")

    with allure.step("Choose gender"):
        browser.element('label[for="gender-radio-2"]').click()

    with allure.step("Fillen phone number"):
        browser.element('[id="userNumber"]').should(be.visible).type("7078083369")

    with allure.step("Choose DB"):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('November')
        browser.element('.react-datepicker__year-select').type('1995')
        browser.element('.react-datepicker__day--003').click()

    with allure.step("Choose subject"):
        browser.element('#subjectsInput').should(be.visible).type('Computer Science').press_enter()

    with allure.step("Choose hobbie"):
        browser.element('label[for ="hobbies-checkbox-3"]').click()

    with allure.step("Upload image"):
        browser.element('[id="uploadPicture"]').should(be.visible).send_keys(IMAGE_PATH)

    with allure.step("Filled address"):
        browser.element('[id="currentAddress"]').should(be.visible).type("Almaty")

    with allure.step("Choose state and city"):
        browser.element('#state input').type('NCR').press_enter()
        browser.element('#city input').type('Delhi').press_enter()

    with allure.step("Send form"):
        browser.element('#submit').click()

    with allure.step("Check success sent"):
        browser.element('[id="example-modal-sizes-title-lg"]').should(be.visible).should(have.text('Thanks for submitting the form'))
