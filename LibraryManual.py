# 도서를 관리하는 콘솔 프로그램
# 도서 정보는 도서명, 저자로 구성
import Search
from AddBook import AddBook
from AllBook import AllBook
from DelBook import DeleteBook


class Library:
    BookList = []
    def __init__(self):
        self.BookList = []
    def library_manual(self):
        while True:
            self.show_manual()
            inp = input("원하시는 기능을 선택하세요: ")
            if inp == "1":
                AllBook(self.BookList)
            elif inp == "2":
                Search.search_book(self.BookList)
            elif inp == "3":
                AddBook()
            elif inp == "4":
                DeleteBook()
            elif inp == "5":
                print("\n도서 찾기 서비스를 종료합니다.")
                break

    def show_manual(self):
        print("도서 관리 프로그램입니다.")
        print("*" * 17)
        print("1. 도서 목록 보기")
        print("2. 도서 검색하기")
        print("3. 도서 추가하기")
        print("4. 도서 삭제하기")
        print("5. 종료하기")
        print("*" * 17)

if __name__ == "__main__":
    Library = Library()
    Library.library_manual()