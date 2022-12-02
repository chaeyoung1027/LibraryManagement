from LibraryManual import Library

class Add(Library):
    def __init__(self, BookList):
        super().__init__(BookList)
        self.BookList = []
        self.addBook()

    def addBook(self):
        while True:
            info = input("추가할 도서명(저자)를 입력하세요(취소하려면 엔터): ")
            if info == "":
                break
            print(f'<{info}> 도서를 추가하였습니다.')
            self.BookList.append(info)



