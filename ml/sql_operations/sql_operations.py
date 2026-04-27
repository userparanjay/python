import pandas as pd
from sqlalchemy import create_engine

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///data.db')

df=pd.read_sql_table("select * from user_details",engine)
print(df)

# Close the engine
engine.dispose()