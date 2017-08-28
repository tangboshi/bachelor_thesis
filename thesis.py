import datetime

# Introduction Chapter
class bachelor_thesis:
    def __init__(self):
        basics  = ["802.11", "CSMA", "ALOHA", "GNU Radio", "Python", "Bash", "Latex"]
        scripts = ["measurement", "plotting", "automatization"]
        self.study_some(basics)
        self.program(scripts)
        self.modify("flow charts")

        finished = True
        while not finished:
            self.launch(self.scripts[:-1])
            if self.results() == True:
                finished = False
            else:
                self.curse(["hardware", self])
                self.fix("problem")
                if self.is_fixed("problem"):
                    self.rejoice()
                else:
                    self.distract("Peng")

        self.write("bachelor_thesis")

        now = datetime.datetime.now()
        submit_date = datetime(2017,10,24)

        while now < submit_date:
            self.edit_and_compile(self)

    # Background Chapter
    def study_some(self, items):
        for item in items:
            book = self.get_book(item)
            if book is not None:
                self.read(book)
            else:
                self.read(self.search("the internet"))
            self.write_summary(item)

    # Measurement Chapter
    def program(self, items):
        self.scripts = []
        for item in items:
            while not self.works(item):
                self.edit(item)
            self.scripts += [item]

    def modify(self, flowchart):

    def results(self):
