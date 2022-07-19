import requests
import pandas as pd


url = "https://streaming-availability.p.rapidapi.com/search/basic"

querystring = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"1","output_language":"en","language":"en"}

headers = {
	"X-RapidAPI-Key": "ceaf44ad44msh562646ba42ec2f1p1dd9fcjsn0a1d24d96772",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

response = response.json()

df = pd.DataFrame.from_dict(response)
csv_ = df.to_csv(index=False)
print(csv_)
