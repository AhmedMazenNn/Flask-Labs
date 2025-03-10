from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_books():
    response = requests.get("https://freetestapi.com/api/v1/books")
    if response.status_code == 200:
        return response.json()
    return []

@app.route('/')
def book_list():
    books = get_books()
    return render_template('book_list.html', books=books)

@app.route('/books/<int:book_id>')
def book_detail(book_id):
    books = get_books()
    for book in books:
        if book["id"] == book_id:
            return render_template('book_detail.html', book=book)
        
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404   

if __name__ == '__main__':
    app.run(debug=True)