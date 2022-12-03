class DeleteBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.delete_book()

    def delete_book(self):
        while True:
            title = input(f'삭제할 도서명을 입력하세요(취소하려면 엔터): ')
            if title == "":
                break
            for t, a in self.BookList.items():
                if t == title:
                    print(f'<{t}> - <{a}> 도서를 찾았습니다.')
            author = input(f'삭제할 {title} 도서의 저자를 입력하세요(취소하려면 엔터): ')
            if author == "":
                break
            for t, a in self.BookList.items():
                if t == title and a == author:
                    print(f'<{t}> - <{a}> 도서를 삭제하였습니다.')
                    del self.BookList[t]
                    break
                else:
                    print(f'<{t}> - <{a}> 도서가 없습니다.')
                    break


