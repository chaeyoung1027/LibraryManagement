#도서의 이름의 일부를 입력하면 도서를 찾아주는 프로그램

class search_book:
    def __init__(self, book_list, book_name):
        self.book_list = book_list
        self.book_name = book_name

    def search(self):
        for book in self.book_list:
            if self.book_name in book.name:
                print(book.name)