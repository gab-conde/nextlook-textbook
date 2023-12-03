import pandas as pd

def process_book_data():

    # Convert the csv to a dataframe
    book_data = pd.read_csv('datasets/BNTextbook_2022-02-05.csv')

    # Filter the dataframe to exclude non-vital columns
    book_columns = ['title', 'edition', 'publisher', 'ISBN']
    book_data = book_data[book_columns]

    # Remove rows with missing data
    book_data.dropna(axis='index', how='any', inplace=True)

    # Remove duplicate textbooks from the dataframe
    book_data.drop_duplicates(subset='title', keep='first', inplace=True)
    book_data.drop_duplicates(subset='ISBN', keep='first', inplace=True)

    book_data.to_json('datasets/book_data.json')