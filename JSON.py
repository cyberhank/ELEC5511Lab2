class JSON():
    def __init__(self):
      pass
    def create_json(self):
        json = {}
        loop = 1
        inputer = input("Enter an item or type \"done\" to quit \n")
        if inputer != "done":
            json.setdefault((str(loop) + ":"),inputer)
            loop += 1
            
        else: 
            return
        while inputer != "done":
           json.setdefault(str(loop) + ":",inputer)
           loop += 1
           inputer = input("Enter an item or type \"done\" to quit \n")
          
        return

    pass




