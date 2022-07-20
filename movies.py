import requests
import pandas as pd


url = "https://streaming-availability.p.rapidapi.com/search/basic"
APIkey = "ceaf44ad44msh562646ba42ec2f1p1dd9fcjsn0a1d24d96772"

def getStreamingService():
    streaming_services = ['Netflix', 'Prime', 'Disney', 'Hulu', 
                          'Peacock', 'Paramount', 'Starz', 'Showtime', 'Apple', 'Mubi']
    
    print("Here is a list of streaming services available: \n")
    print(streaming_services)
    selected_service = input("What streaming service do you want to use? ")
    
    if selected_service.capitalize() in streaming_services:
        return selected_service
    else:
        print("Please enter a streaming service that is \
              present in the list provided!")
        getStreamingService()
        
    

def get_response(streaming_service):
    querystring = {"country":"us","service":streaming_service.lower(),
               "type":"movie","page":"20",
               "output_language":"en","language":"en"}

    headers = {
	"X-RapidAPI-Key": APIkey,
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    try:
        final_response = response.json()
        return final_response
    except:
        print("Invalid request!")

def createDatabase(response):
    response = response['results']

    try:
        df = pd.DataFrame.from_dict(response)
        df_withSelectColumns = df[['title', 'year', 'age', 'genres', 'runtime', 'overview', 'posterURLs']]
        print(df_withSelectColumns)
    
        column_names = ['title', 'year', 'age', 'genres', 'runtime', 'overview', 'posterURLs']

        csv_ = df_withSelectColumns.to_csv(columns=column_names, header=True, index=False)
    except KeyError:
        print("No movies found")
        



def main():
    streaming_service = getStreamingService()
    response = get_response(streaming_service)
    createDatabase(response)

if __name__=='__main__':
    main()
