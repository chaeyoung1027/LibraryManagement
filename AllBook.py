#모든 책을 조회하는 클래스
class AllBook:
    def __init__(self):
        self.BookList = []
        self.Title = ""  # 책의 제목
        self.Author = ""  # 책의 저자

    def __str__(self):
        if BookList == []:
            return "도서 목록이 없습니다."

