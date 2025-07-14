import parse
import render
import Url_retrevive
import button_lct
import init
from google import genai
client = genai.Client()


#Ideas
    # persist URl
    # AI summary
    # structering in an enum
    # use click up as a collection
    # Use mongo db
    # User --> providers --> structerd enum list --> 



class main:
    def __init__(self, csv):
        self.csv = csv
        self.browser = init.start().browser
        self.page = init.start().page
    def close(self):
        self.browser.close()
        init.start().close()
        print("Browser closed and resources cleaned up.")
    def parse_page(self):
        all_texts = []
        targetnumber = render.count_occupied_rows(self.csv)
        targetnumber = targetnumber - 1
        print(targetnumber)
        index = 1
        results = []
        for i in range(targetnumber):
            target_page = render.get_csv_cell(self.csv, index)
            target_page = target_page + ' start service form'
            print(f"Parsing page: {target_page}")
            found_url = Url_retrevive.search_google(target_page)
            parser_instance = parse.parser(found_url, self)
            text = parser_instance.parse_page()
            all_texts.append(text)
            index += 1
        #render.save_all_to_pdf(all_texts)
        for i in range(targetnumber):
            results.append(all_texts[i]) 
    def execute(self):
        print(self.parse_page())
        self.close()
        
main_instance = main(r'./Sheet1.csv')
main_instance.execute()

