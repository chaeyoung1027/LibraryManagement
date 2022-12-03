#모든 책을 조회하는 클래스
class AllBook:
    def __init__(self, book_list):
        self.BookList = book_list
        self.show_list()

    def show_list(self):
        index = 0
        print()
        if not self.BookList:
            print(f'도서 목록이 비어있습니다.')
        else:
            for i in self.BookList:
                print(f'{index+1}. {i}')
                index += 1
            print(f'총 {index}권의 도서가 있습니다.')


