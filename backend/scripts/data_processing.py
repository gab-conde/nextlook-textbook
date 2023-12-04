import pandas as pd

def clean_book_data() -> pd.DataFrame:

    # Convert the csv to a dataframe
    book_data = pd.read_csv('datasets/BNTextbook_2022-02-05.csv')

    # Filter the dataframe to exclude non-vital columns
    book_columns = ['ISBN', 'title', 'edition', 'publisher']
    book_data = book_data[book_columns]

    # Remove rows with missing data
    book_data.dropna(axis='index', how='any', inplace=True)

    # Remove text within parentheses from titles
    book_data['title'] = book_data['title'].str.replace(r"\(.*?\)", "", regex=True).str.strip()

    # Remove duplicate textbooks from the dataframe
    book_data = book_data.drop_duplicates(subset=['title', 'ISBN'])

    return book_data
