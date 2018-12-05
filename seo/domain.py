from . import page
from . import user
import pprint
import time

class Domain:
    def __init__(self,request,url):
        self.url = url
        self.page = page.Page(self.url)
        self.table = self.page.dictionary
        self.post_table = self.organize_table()

    def get_table_data(self):
        return self.post_table.dictionary
        #return {"blank":None}

    def organize_table(self):
        dictionary = {}
        meta_dict = self.table.pop('meta')

        id_array=["itemprop", "name", "property"]
        matter_array=["content"]

        #organize meta
        dictionary.update({"title":self.table['title']})
        dictionary.update(self.safe_update(meta_dict, "description", id_array, matter_array))
        dictionary.update(self.safe_update(meta_dict, "name", id_array, matter_array))
        dictionary.update(self.safe_update(meta_dict, "viewport", id_array, matter_array))
        dictionary.update(self.safe_update(meta_dict, "image", id_array, matter_array))
        dictionary.update(self.safe_update(meta_dict, "keywords", id_array, matter_array))

        #social media
        #Facebook
        facebook_dictionary={}
        facebook_dictionary.update(self.safe_update(meta_dict, 'og:title', id_array, matter_array))
        facebook_dictionary.update(self.safe_update(meta_dict, 'og:type', id_array, matter_array))
        facebook_dictionary.update(self.safe_update(meta_dict, 'og:url', id_array, matter_array))
        facebook_dictionary.update(self.safe_update(meta_dict, 'og:image', id_array, matter_array))
        facebook_dictionary.update(self.safe_update(meta_dict, 'og:description', id_array, matter_array))
        facebook_dictionary.update(self.safe_update(meta_dict, 'og:site_name', id_array, matter_array))
        facebook_dictionary.update(self.safe_update(meta_dict, 'fb:admins', id_array, matter_array))

        #Twitter
        twitter_dictionary={}
        twitter_dictionary.update(self.safe_update(meta_dict, 'twitter:card', id_array, matter_array))
        twitter_dictionary.update(self.safe_update(meta_dict, 'twitter:site', id_array, matter_array))
        twitter_dictionary.update(self.safe_update(meta_dict, 'twitter:title', id_array, matter_array))
        twitter_dictionary.update(self.safe_update(meta_dict, 'twitter:description', id_array, matter_array))
        twitter_dictionary.update(self.safe_update(meta_dict, 'twitter:creator', id_array, matter_array))
        twitter_dictionary.update(self.safe_update(meta_dict, 'twitter:image:src', id_array, matter_array))

        social_media_dictionary={}
        social_media_dictionary.update({"facebook":facebook_dictionary})
        social_media_dictionary.update({"twitter":twitter_dictionary})

        dictionary.update({"social media":social_media_dictionary})

        print("\n\n\n\n\nSCORE")
        sc = self.score(dictionary,{"score":0,"count":0})
        dictionary.update({"score": str(int(round(float( float(sc['score'] / sc['count']) * 100.00 ), 0))) })

        return dictionary

    def score(self, d, sc):
        for k, v in d.items():
            sc.update({"count":sc['count']+1})
            if not ( v == None or str(v) == 'None' or len(str(v)) < 2 or isinstance(v, dict)):
                sc.update({"score":sc['score']+1})
                print(str(k)+" : "+str(v))
            if isinstance(v, dict):
                return self.score(v, sc)
        return sc

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

    def safe_update(self, dict, lookup, ids, matters, contains=False):
        return_dictionary={}
        if 'dict' in str(type(dict)):
            for meta_key in dict.keys():
                dict_entry = dict[meta_key]
                key=None
                value=None
                if 'dict' in str(type(dict_entry)):
                    for i in ids:
                        try:
                            key = dict_entry[i]
                            for matter in matters:
                                try:
                                    value = dict_entry[matter]
                                    if contains:
                                        if str(lookup).lower() in str(key).lower():
                                            user.prompt(feed="found match: "+str(key)+": "+str(value), custom=75)
                                            return_dictionary.update({key:value})
                                            break
                                    else:
                                        if key == lookup:
                                            user.prompt(feed="found match: "+str(key)+": "+str(value), custom=75)
                                            return_dictionary.update({key:value})
                                            break
                                except Exception as e:
                                    num8=0
                                    #user.prompt(feed=str(e), notice=True)
                        except Exception as e:
                            num8=0
                            #user.prompt(feed=str(e), notice=True)

        #validate this dictionary before returning
        if not lookup in return_dictionary.keys():
            return_dictionary.update({lookup:None})
        user.prompt(feed=return_dictionary, type_of=True)
        return return_dictionary
