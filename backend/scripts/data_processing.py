import pandas as pd

def clean_book_data() -> pd.DataFrame:

    # Convert the csv to a dataframe
    book_data = pd.read_csv('datasets/BNTextbook_2022-02-05.csv')

    # Filter the dataframe to exclude non-vital columns
    book_columns = ['ISBN', 'title', 'edition', 'publisher']
    book_data = book_data[book_columns]

    # Remove rows with missing data
    book_data.dropna(axis='index', how='any', inplace=True)

    # Remove duplicate textbooks from the dataframe
    book_data.drop_duplicates(subset='title', keep='first', inplace=True)
    book_data.drop_duplicates(subset='ISBN', keep='first', inplace=True)

    return book_data