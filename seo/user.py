def prompt(feed,options=False,notice=False,custom=False,custom_space=False):
    if options:
        inter='%'+str(45)+'s'
        for key in feed.keys():
            print(str(inter)%str(key)+" "+str(feed[key]))
    elif custom:
        inter='%'+str(int(custom_space))+'s'
        print(str(inter)%str(feed))
    else:
        inter='%'+str(30)+'s'
        print(str(inter)%str(feed))
