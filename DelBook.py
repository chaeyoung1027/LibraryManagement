class DeleteBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.delete_book()

    def delete_book(self):
        while True:
            info = input(f'삭제할 도서명(저자)을 입력하세요(취소하려면 엔터): ')
            if info == "":
                break
            if info in self.BookList:
                self.BookList.remove(info)
                print(f'<{info}> 도서를 삭제하였습니다.')
            else:
                print(f'존재하지 않는 도서입니다.')

