from playwright.sync_api import expect
import pytest


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page):
    # Переходим на страницу авторизации
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Находим поле "E-mail" и заполняем его
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    # .locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    # Находим поле "Password" и заполняем его
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    # .locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill("password")

    # Находим кнопку "Login" и кликаем на нее
    login_button = chromium_page.get_by_test_id("login-page-login-button")
    # .locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    # Проверяем, что появилось сообщение об ошибке
    alert_message = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    # .locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(alert_message).to_be_visible()
    expect(alert_message).to_have_text("Wrong email or password")
