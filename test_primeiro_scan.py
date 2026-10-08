from playwright.sync_api import Page
from pytest_playwright_axe import Axe

def test_primeiro_scan(page: Page):
    page.goto("https://dequeuniversity.com/demo/mars/")

    resultado = Axe().run(page)

    print("f\nViolacoes encontradas: {len(resultado['violations'])}")
    for violacao in resultado['violations']:
        print(f"-  [{violacao['impact']}] {violacao['id']}")
