from flask import Flask
from dotenv import load_dotenv

from models.Book import Book
from scripts import data_processing

# Load environment variables
load_dotenv()

# Create app
app = Flask(__name__)

# Create DataFrame from book data
book_df = data_processing.clean_book_data()

# Create a set to hold books
books = set()

# Create an adjacency list for resources
graph = {}

# Create book objects and add to graph
for row in book_df.itertuples(index=False, name=None):
    book_n = Book(row[0], row[1], row[2], row[3])
    books.add(book_n)
    for topic in book_n.topics:
        if topic in graph:
            related_books = graph[topic]
            related_books.append(book_n)
            graph[topic] = related_books
        else:
            graph[topic] = [book_n]

# Home page functionality
@app.route('/')
def home():
    # print('hi')
    return 'hi'

# Debug reloads the app when changes are made to the code
if __name__ == '__main__':
    app.run(debug=True)