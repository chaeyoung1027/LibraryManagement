class AddBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.add_book()

    def add_book(self):
        while True:
            title = input(f'추가할 도서명을 입력하세요(취소하려면 엔터): ')
            if title == "":
                break
            author = input(f'{title}의 저자를 입력하세요(취소하려면 엔터): ')
            for t, a in self.BookList.items():
                if t == title and a == author:
                    print(f'이미 존재하는 도서입니다.')
                    break
            else:
                self.BookList["title"] = author
                print(f'<{title}> 도서를 추가하였습니다.')




