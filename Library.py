'''
도서 관리 프로그램

1. 도서 목록 보기
2. 도서 검색하기
3. 도서 추가하기
4. 도서 삭제하기
5. 종료하기

다음 기능 중 원하는 번호를 입력하면 그에 맞는 화면으로 넘어가진다.
매뉴얼 파일에서 5번을 누르면 프로그램이 종료된다.
그 외엔 엔터를 누르면 매뉴얼 화면으로 돌아간다.
'''

from LibraryManual import Library

Library = Library()
Library.library_manual()