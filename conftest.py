import pytest
from playwright.sync_api import Page

@pytest.fixture
def logado(page : Page):
    page.goto("")
    page.locator("#login-email").fill('cliente@shopdemo.com')
    page.locator("#login-senha").fill('senha123')
    page.get_by_test_id("login-submit-button").click()
    yield page

