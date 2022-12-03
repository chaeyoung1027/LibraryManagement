class AddBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.add_book()

    def add_book(self):
        while True:
            info = input(f'추가할 도서명(저자)를 입력하세요(취소하려면 엔터): ')
            if info == "":
                break
            if info in self.BookList:
                print(f'<{info}> 도서가 이미 있습니다.')
            else:
                self.BookList.append(info)
                print(f'<{info}> 도서를 추가하였습니다.')




