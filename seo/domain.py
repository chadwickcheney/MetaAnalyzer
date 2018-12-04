from . import page
from . import user
import pprint

class Domain:
    def __init__(self,request,url):
        self.url = url
        self.page = page.Page(self.url)
        self.table = self.page.dictionary
        self.post_table = self.organize_table()

    def get_table_data(self):
        #return self.post_table.dictionary
        return {"blank":None}

    def organize_table(self):
        '''array=["title","description","viewport","social media"]
        for a in array:
            for key in self.table.keys():
                user.prompt(feed="\nkey__________________________\n"+str(key)+"\n", custom=50)

                if 'dict' in str(type(self.table[key])):
                    for subkey in self.table[key].keys():
                        user.prompt(feed="\nsubkey__________________________\n"+str(subkey)+"\n", custom=50)

                        value = self.get_value_safe(self.table, key, subkey)
                        if "str" in str(type(value)):
                            print(value)

                        if 'dict' in str(type(self.table[key][subkey])):
                            for subsubkey in self.table[key][subkey].keys():
                                user.prompt(feed="\nsubsubkey__________________________\n"+str(subsubkey)+"\n", custom=50)

                                value = self.get_value_safe(self.table, key, subkey, subsubkey)
                                if "str" in str(type(value)):
                                    print(value)

                else:
                    value = self.get_value_safe(self.table, key)
                    if "str" in str(type(value)):
                        print(value)'''

        dictionary = {}
        meta_dict = self.table.pop('meta')

        id_array=["itemprop", "name", "property"]
        matter_array=["content"]
        pprint.pprint(meta_dict)
        for key in meta_dict.keys():
            dictionary.update(self.safe_update(meta_dict[key], "description", id_array, matter_array))
            dictionary.update(self.safe_update(meta_dict[key], "name", id_array, matter_array))
            dictionary.update(self.safe_update(meta_dict[key], "viewport", id_array, matter_array))
            dictionary.update(self.safe_update(meta_dict[key], "image", id_array, matter_array))
            dictionary.update(self.safe_update(meta_dict[key], "keywords", id_array, matter_array))
        pprint.pprint(dictionary)

    def get_value_safe(self, dict, key, subkey=None, subsubkey=None):
        try:
            if subkey and not subsubkey:
                value = dict[key][subkey]
                return value
            elif subsubkey:
                value = dict[key][subkey][subsubkey]
                return value
            else:
                value = dict[key]
                return value
        except:
            return False

    def safe_update(self, dict, lookup, ids, matters):
        key=None
        value=None
        if 'dict' in str(type(dict)):
            for i in ids:
                try:
                    key = dict[i]
                    for matter in matters:
                        try:
                            value = dict[matter]
                            if key == lookup:
                                user.prompt(feed="found match: "+str(key)+": "+str(value), custom=75)
                            return {key:value}
                        except:
                            num7=0
                except:
                    num7=0
        return {lookup:None}
