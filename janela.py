from breezypythongui import EasyFrame 


class LabelDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "hello", row=0, column=0)
def main():
    LabelDemo().prompterBox()
if __name__=="__main__":
    main()
        

