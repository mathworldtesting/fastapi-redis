from fastapi import Body, FastAPI
import random
import uvicorn

app = FastAPI()

BOOKS = [

    {'title': 'title One', 'author': 'Author 1', 'category': 'science'},
    {'title': 'title two', 'author': 'Author 2', 'category': 'reading'},
    {'title': 'title three', 'author': 'Author 3', 'category': 'math'},
    {'title': 'title four', 'author': 'Author 4', 'category': 'algegra'},
    {'title': 'title five', 'author': 'Author 5', 'category': 'history'},
    {'title': 'title six', 'author': 'Author 6', 'category': 'physical'},
    {'title': 'title seven', 'author': 'Author 7', 'category': 'reading'},
    {'title': 'title eight', 'author': 'Author 8', 'category': 'shop'},
    {'title': 'title nine', 'author': 'Author 9', 'category': 'geometry'},
    {'title': 'title ten', 'author': 'Author 10`', 'category': 'science'}
]

@app.get("/")
async def read_all_books():
    return BOOKS

@app.get("/random")
def random_number():
    return {"random number": random.randint(0, 12)}


@app.get("/books/{book_author}")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_id}")
async def read_by_id(book_id: int):
    for book in BOOKS:
        if book.get('id') == book_id:
            return book
        


@app.get("/books/{book_title}")
async def read_title_by_query(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

