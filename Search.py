#도서의 이름의 일부를 입력하면 도서를 찾아주는 프로그램

def search_book(book_list, book_name):
    for book in book_list:
        if book_name in book.name:
            print(book.name)
