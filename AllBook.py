#모든 책을 조회하는 클래스
class AllBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.__str__()

    def __str__(self):
        if self.BookList:
            for i in range(len(self.BookList)):
                print(f'{i+1}. {self.BookList[i]}')
        else:
            print(f'도서 목록이 없습니다.')

