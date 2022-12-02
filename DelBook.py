from LibraryManual import Library

class Delete(Library):
    def __init__(self, BookList):
        super().__init__(BookList)
        self.BookList = []
        self.deleteBook()

    def deleteBook(self):
        while True:
            info = input("삭제할 도서명(저자)를 입력하세요(취소하려면 엔터): ")
            if info == "":
                break
            print(f'<{info}> 도서를 삭제하였습니다.')
            self.BookList.append(info)