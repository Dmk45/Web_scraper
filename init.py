from playwright.sync_api import sync_playwright
playwright = sync_playwright().start()

class start:
    def __init__(self):
        self.browser = playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()
    def close(self):
        self.browser.close()
        playwright.stop()
