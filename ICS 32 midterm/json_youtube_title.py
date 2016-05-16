# this program issues a serach for youtube videos , given a particular search

import json
import urllib.parse
import urllib.request



GOOGLE_API_KEY = "AIzaSyAdpz4y7NlVi6diJnNUm61FxgV7qTxPFY0"

BASE_YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3'



def build_search_url(search_query:str, max_results: int) ->str:


    query_parameters = [
        ('key', GOOGLE_API_KEY),('part','snippet'),
        ('type', 'video'),('maxResults',str(max_results)),
        ('q',search_query)

    ]

    return BASE_YOUTUBE_URL + '/search?' + urllib.parse.urlencode(query_parameters)


def get_result(url:str)->'json':

    response = None

    try:

        response = urllib.request.urlopen(url)
        json_text = response.read().decode(encoding = 'utf-8')

        return json.loads(json_text)
    finally:

        if response != None:
            response.close()



def print_title_and_description(json_result: 'json') ->None:


    for item in json_result['items']:
        print(item['snippet']['title'])
        print(item['snippet']['description'])
        print()



if __name__ == '__main__':
    search_query = input('Query: ')
    result =  get_result(build_search_url(search_query, 10))
    print_title_and_description(result)
    #print(result)



    
