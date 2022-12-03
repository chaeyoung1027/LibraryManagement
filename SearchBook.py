#도서의 이름의 일부를 입력하면 도서를 찾아주는 프로그램
class SearchBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.search()

    def search(self):
        info = input("검색할 도서명(저자)을 입력하세요: ")
        for i in self.BookList:
            if i == info:
                print(f'{i} 도서를 찾았습니다.')
                break
        else:
            print(f'검색 결과가 없습니다.')
