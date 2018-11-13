from . import page

class Domain:
    def __init__(self,request,url):
        self.url = url
        self.page = page.Page(self.url)
        self.table = self.get_table_data()

        #Organize dictionary and return only relevant information

    def get_table_data(self):
        return self.page.dictionary
