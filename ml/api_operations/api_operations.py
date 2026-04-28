import pandas as pd
import requests as req
response =req.get('https://jsonplaceholder.typicode.com/comments')
result=response.json()
df=pd.DataFrame(result)
df.to_csv("output.csv", index=False)