from . import page

class Domain:
    def __init__(self,request,url):
        self.url = url
        self.page = page.Page(self.url)
        self.table = self.get_table_data

    def get_table_data(self):
        return self.page.dictionary
