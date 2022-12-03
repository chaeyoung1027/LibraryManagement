#도서의 이름의 일부를 입력하면 도서를 찾아주는 프로그램
class SearchBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.search()

    def search(self):
        print("도서 검색 키워드")
        print("1. 제목")
        print("2. 저자")

        book_keynum = input("검색 키워드를 선택하세요: ")
        book_keyword = input(f'검색할 키워드를 입력하세요(취소하려면 엔터): ')

        if book_keynum == 1:
            for book_keyword, a in self.BookList.items():
                if title in book_keyword:
                    print(f'<{book_keyword}> - <{a}> 도서를 찾았습니다.')
                else :
                    print(f'<{book_keyword}> - <{a}> 도서가 없습니다.')
        elif book_keynum ==2:
            for book_keyword, a in self.BookList.items():
                if author in book_keyword:
                    print(f'<{t}> - <{book_keyword}> 도서를 찾았습니다.')
                else :
                    print(f'<{t}> - <{book_keyword}> 도서가 없습니다.')
                    
        # for book_name in self.BookList:
        #     if book_name in self.BookList:
        #         print(f'<{book_name}> 도서를 찾았습니다.')
        #     else:
        #         print(f'<{book_name}> 도서가 없습니다.')