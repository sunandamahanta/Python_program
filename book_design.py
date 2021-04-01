#Design a 'book' class with title,author,publisher,price and author's royalty as instance variables.

class book:
    author_royalty=0.0
    def __init__(self,ti,au,pu,pr,cpy):
        self.title=ti
        self.author=au
        self.publisher=pu
        self.price=pr
        self.copies_sold=cpy

    #Provide getter and setter properties for all variables

    def gettitle(self):
        return self.title
    def getauthor(self):
        return self.author
    def getpublisher(self):
        return self.publisher
    def getprice(self):
        return self.price
    def getcopies_sold(self):
        return self.copies_sold

    def settitle(self,ti):
        self.title=ti
    def setauthor(self,au):
        self.author=au
    def setpublisher(self,pu):
        self.publisher=pu
    def setprice(self,pr):
        self.price=pr
    def setcopies_sold(self,cpy):
        self.copies_sold=cpy

    # define a method royalty() to calculate royalty amount author can expect to receive the following royalties

    def royalty(self):
        if self.copies_sold <= 500:
            book.author_royalty=0.1*self.price
        else:
            if self.copies_sold >= 1500:
                book.author_royalty=0.125*self.price
            else:
                book.author_royalty=0.15*self.price
        print("Royalty Amount is Rs.",self.author_royalty)

#design a new ‘ebook’ class inherited from ‘book’ class
#Add ebook format (EPUB, PDF, MOBI etc) as additional instance variable in inherited class

class ebook(book):
    def __init__(self,ti,au,pu,pr,cpy,epub,pdf,mobi):
        super().__init__(ti,au,pu,pr,cpy)
        self.EPUB=epub
        self.PDF=pdf
        self.MOBI=mobi

    def getEPUB(self):
        return self.EPUB
    def getPDF(self):
        return self.PDF
    def getMOBI(self):
        return self.MOBI

    def setEPUB(self,epub):
        self.EPUB=epub
    def setPDF(self):
        self.PDF=pdf
    def setMOBI(self):
        self.MOBI=mobi

    #Override royalty() method to deduct GST @12% on ebooks

    def royalty(self):
        super().royalty()
        book.author_royalty=book.author_royalty-(book.author_royalty*0.12)
        print("Royalty Amount after deductiong GST is Rs.",book.author_royalty)

b=book("Python Programming","Sheetal Taneja","Pearson",500,1000)
b.royalty()

eb=ebook("Python Programming","Sheetal Taneja","Pearson",500,1000,"S.Chand","C.pdf",8917590640)
eb.royalty()
