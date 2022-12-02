#모든 책을 조회하는 클래스
class AllBook:
    def __init__(self, BookList):
        super().__init__(BookList)
        self.BookList = []

    def __str__(self, BookList):
        if not self.BookList:
            return "도서 목록이 없습니다."
        else:
            for i in self.BookList:
                print(self.BookList[i])

