class Book:
    def __init__ (self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


    def __repr__(self):
      return  f"Book('{self.title}', '{self.author}', {self.year})"


    def __str__(self):
       return f"('{self.title}', by {self.author}, pblished in {self.year} )"
    

    def __del__ (self):
<<<<<<< HEAD
       print(f"Book '{self.title}' is being deleted.")
=======
       return f"{self.title} by {self.author}, published in {self.year}"
>>>>>>> 066839e2f988db14f239fb2feba74cb38b20b0ed
            
