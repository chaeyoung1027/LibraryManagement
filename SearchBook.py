#도서의 이름의 일부를 입력하면 도서를 찾아주는 프로그램
class SearchBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.search()

    def search(self):
        word_book = []
        print(len(self.BookList))
        info = input("검색할 도서명(저자)을 입력하세요: ")
        for i in self.BookList:
            if info in i:
                word_book.append(i)
        if not word_book:
            print(f'검색 결과가 없습니다.')
        for i in word_book:
            print(f'- {i}')

