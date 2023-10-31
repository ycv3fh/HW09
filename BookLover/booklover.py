class BookLover:
    
    # initializer
    def __init__(self, name, email, fav_genre, num_books, book_list):
        num_books = 0
        book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
        self.name = name 
        self.email = email
        self.fav_email = fav_genre
        self.num_books = num_books
        self.book_list = book_list
        
    # method 1
    def add_book(self, book_name, rating): 
        
        self.book_name = book_name
        self.rating = rating
        
        #add book to list
        if self.book_name in self.book_list.values():
            print("Yes, the value 'Rahul' exists in the student dictionary")
        else:
            new_book = pd.DataFrame({
                    'book_name': [book_name], 
                    'book_rating': [book_rating]
                                })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
    
    #method 2
    def has_read(self,book_name):
        if self.book_name in self.book_list.values():
            print("Yes, the value 'Rahul' exists in the student dictionary")
            return True
        else:
            return False
        
    #method 3
    def num_books_read(self):
        self.books_read = len(self.book_list)
    
    #method 4
    def fav_books(self):
        self.favs = {key:value for (key,value) in self.book_list.items() if value > 3}

if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    test_object.has_read("War of the Worlds")
    test_object.num_books_read()
    test_object.fav_books()
    