#도서의 이름의 일부를 입력하면 도서를 찾아주는 프로그램
class SearchBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.search()

    def search(self):
        pass
        # book_name = input("검색할 도서를 입력하세요: ")
        # for book_name in self.BookList:
        #     if book_name in self.BookList:
        #         print(f'<{book_name}> 도서를 찾았습니다.')