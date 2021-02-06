import json
class jsoncreator():
    def __init__(self):
        return 
    def create_json(self):  
        json1 ={}
        loop = 1
        inputer = input("Enter an item or type \"done\" to quit \n")
        if inputer != "done":
            json1.setdefault((str(loop) + ":"),inputer)
            loop += 1
            


        while inputer != "done":
             json1.setdefault(str(loop) + ":",inputer)
             loop += 1
             inputer = input("Enter an item or type \"done\" to quit \n")
             print(json1)
        with open('info.json','w') as f:
            json.dump(json1,f)
        return
pass
