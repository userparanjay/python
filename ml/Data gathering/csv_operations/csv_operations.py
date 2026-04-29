import pandas as pd

# Function to format movie title text
# capitalize() -> first letter uppercase, rest lowercase
def nameChangef(name):
    return str(name).strip().capitalize()


# Function to format year/date column
# Converts to numeric, invalid values become NaN
def yearChangef(year):
    return pd.to_numeric(year, errors="coerce")


# Read large TSV file in chunks
dfs = pd.read_csv(

    "/content/movie_titles_metadata.tsv",   # File path

    sep="\t",                              # Separator is TAB because .tsv file

    names=[
        "S.no",
        "title",
        "year",
        "rating",
        "money",
        "tags"
    ],                                     # Custom column names

    index_col="S.no",                      # Make S.no column as index

    usecols=[
        "S.no",
        "title",
        "year",
        "money"
    ],                                     # Load only selected columns

    dtype={
        "money": float
    },                                     # Force money column datatype

    skiprows=[0, 2],                       # Skip row number 0 and 2

    nrows=100,                             # Read only first 100 rows

    encoding="utf8",                       # File text encoding

    on_bad_lines="skip",                   # Skip broken rows

    converters={
        "title": nameChangef,             # Apply title formatting
        "year": yearChangef              # Apply year formatting
    },

    na_values=["m4"],                      # Treat m4 as NaN

    chunksize=500,                         # Read 500 rows at a time

    engine="python",                       # Better for messy files

    low_memory=False                       # Better datatype inference
)


# chunksize returns iterator, so loop chunk by chunk
for chunk in dfs:
    print(chunk.head())
    break