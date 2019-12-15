class Book():

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    def __str__(self):
        return 'Title:{} Author:{} Pages:{}'.format(self.title,self.author,self.pages)

    def __del__(self):
        print('A book is a destroyed.')

b=Book('OOP','Rabbi','200')
print(b)
del b
