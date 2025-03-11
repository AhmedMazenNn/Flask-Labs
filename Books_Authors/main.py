from flask import Flask, render_template, redirect ,url_for 
from forms.form import BookForm, AuthorForm
from database import db
from models import Author, Book
from flask_bootstrap import Bootstrap5


main = Flask(__name__)
main.config['SECRET_KEY'] = 'd2b0873fb7c652daa2ccc52b5b479edd'
main.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
bootstrap = Bootstrap5(main)
db.init_app(main)

with main.app_context():
    db.create_all()

@main.route('/', endpoint="index", methods=['GET'])
def hello():
    return render_template('index.html')



@main.route('/bookForm',endpoint="bookForm", methods=['POST', 'GET'])
def bookForm():
    form = BookForm()
    
    form.author.choices = [(author.id, author.name) for author in Author.query.all()]
    
    if form.validate_on_submit():
        book = Book(
            title=form.title.data, 
            author_id=int(form.author.data),
            publish_date=form.publish_date.data,
            price=form.price.data, 
            create_date=form.create_date.data
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('base'))

    return render_template('book_form.html', form=form)

@main.route('/authorForm', endpoint="authorForm", methods=['POST' , 'GET'])
def authorForm():
    form = AuthorForm()
    if form.validate_on_submit():
        author = Author(name=form.name.data)
        db.session.add(author)
        db.session.commit()
        return redirect(url_for('base'))
    return render_template('author_form.html', form=form)

@main.route('/books', endpoint="books", methods=['GET'])
def get_books():
    books = Book.query.all()
    return render_template('books.html', books=books)

@main.route('/book/<int:book_id>', methods=['GET'])
def book_details(book_id):
    book = Book.query.get_or_404(book_id) 
    return render_template('book_details.html', book=book)

@main.route('/author/<int:author_id>', methods=['GET'])
def author_details(author_id):
    author = Author.query.get_or_404(author_id) 
    return render_template('author_details.html', author=author)


@main.route('/authors', methods=['GET'])
def get_authors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)

if __name__ == '__main__':
    main.run(debug=True)