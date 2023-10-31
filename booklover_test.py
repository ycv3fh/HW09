import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        book1 = test_object
        book1.add_book("Jane Eyre", 4)
        print(book_list.book_list)
        
        expected = 1
        self.assertEqual(len(student1.book_list), expected)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        book1 = BookLover("Apollo","johndoe@email.com", "comedy")
        book1.add_book("Jane Eyre", 4)
        print(book_list.book_list)
        
        expected = 1
        self.assertEqual(len(student1.book_list), expected)

    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        book1 = BookLover("Apollo","johndoe@email.com", "comedy")
        test_book = "Jane Eyre"
        actual = book1.has_read(test_book)

        expected = True
        self.assertEqual(actual, expected)
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        book1 = BookLover("Apollo","johndoe@email.com", "comedy")
        test_book = "Fight Club"
        book1.has_read(test_book)
        self.assertFalse(test_book in book_list.keys())

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        book1 = BookLover("Apollo","johndoe@email.com", "comedy")
        book1.add_book("The Divine Comedy", 5)
        book1.add_book("The Popol Vuh", 5)
        book1.num_books_read()
        
        expected = 3
        self.assertEqual(self.books_read, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        book1 = BookLover("Apollo","johndoe@email.com", "comedy")
        book1.add_book("I Found You", 2)
        book1.add_book("Deep", 1)
        book1.add_book("Gut", 2)
        book1.add_book("A Great Reckoning", 1)
        book1.fav_books()
        actual = len(self.favs)
        
        expected = 3
        self.assertEqual(actual, expected)

if __name__ == '__main__':

    unittest.main(verbosity=3)