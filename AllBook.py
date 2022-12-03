#모든 책을 조회하는 클래스
class AllBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.BookList = []

    def __str__(self):
        if not self.BookList:
            return f'도서 목록이 없습니다.'
        else:
            for i in self.BookList:
                return self.BookList[i]

