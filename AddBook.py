class AddBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.add_book()

    def add_book(self):
        while True:
            info = input(f'추가할 도서명(저자)을 입력하세요(취소하려면 엔터): ')
            if info == "":
                break
            for i in self.BookList:
                if i == info:
                    print(f'이미 존재하는 도서입니다.')
                    break
            else:
                self.BookList.append(info)
                print(f'<{info}> 도서를 추가하였습니다.')




