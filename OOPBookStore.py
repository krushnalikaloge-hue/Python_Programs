class BookStore:

    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.Name, "by", self.Author)
        print("No of Books :", BookStore.NoOfBooks)


obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming", "Dennis Ritchie")
obj2.Display()