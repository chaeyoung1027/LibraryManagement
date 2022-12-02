#모든 책을 조회하는 클래스
class AllBook:
    def __init__(self):
        self.BookList = []
        self.Title = ""  # 책의 제목
        self.Author = ""  # 책의 저자

    def __str__(self):
        for index, book in self.BookList:
            print(f'책 제목 : {self.BookList.Title}, 책 저자 : {self.booklist.Author}')
            return str(self.BookList)

