class AddBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.add_book()

    def add_book(self):
        while True:
            info = input(f'추가할 도서명(저자)를 입력하세요(취소하려면 엔터): ')
            if info == "":
                break
            print(f'<{info}> 도서를 추가하였습니다.')
            self.BookList.append(info)



