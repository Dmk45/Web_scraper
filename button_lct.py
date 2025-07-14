
class button_locater():
    def __init__(self, playwright_instance):
        self.playwright_instance = playwright_instance
        self.browser = self.playwright_instance.browser
        self.page = self.playwright_instance.page

    def lct_psbl_btns(self):
        # This method will locate all possible buttons on the page in order to navigate to the submit form page.
        # Option 1: Using CSS selectors
        css_buttons = self.page.query_selector_all("button, input[type='button'], input[type='submit']")
            
        # Option 2: Using <a> tags
        link_buttons = self.page.query_selector_all("a")
            
        # Option 3: Using XPath(not implemented here)
            
            
        # Option 4: Using ARIA roles
        aria_buttons = self.page.query_selector_all("[role='button']")
            
        # Option 5: Using text content feed to an AI (not implemented here)
            
        # Option 6: Using an AI vision model to identify buttons (not implemented here)
            
        return {
            "css_buttons": css_buttons,
            "link_buttons": link_buttons,
            "aria_buttons": aria_buttons
            }
        
    def page_test(self, selector):
        x = 0
        # used to check if the page conatins the fill out form