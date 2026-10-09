from playwright.sync_api import sync_playwright, expect


def test_wrong_email_or_password_authorization():
    # Запуск Playwright в синхронном режиме
    with sync_playwright() as playwright:
        # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        # Переходим на страницу авторизации
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        # Находим поле "E-mail" и заполняем его
        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        # .locator('//div[@data-testid="login-form-email-input"]//div//input')
        email_input.fill("user.name@gmail.com")

        # Находим поле "Password" и заполняем его
        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        # .locator('//div[@data-testid="login-form-password-input"]//div//input')
        password_input.fill("password")

        # Находим кнопку "Login" и кликаем на нее
        login_button = page.get_by_test_id("login-page-login-button")
        # .locator('//button[@data-testid="login-page-login-button"]')
        login_button.click()

        # Проверяем, что появилось сообщение об ошибке
        alert_message = page.get_by_test_id('login-page-wrong-email-or-password-alert')
        # .locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        expect(alert_message).to_be_visible()
        expect(alert_message).to_have_text("Wrong email or password")
