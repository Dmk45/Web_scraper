

class parser:
    def __init__(self, url, playwright_instance):
        self.url = url
        self.browser = playwright_instance.browser
        self.page = playwright_instance.page

    def parse_page(self):
        self.page.goto(self.url)
        self.page.wait_for_load_state("load")
        text = self.page.inner_text("body")
        return text
