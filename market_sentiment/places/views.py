from django.shortcuts import render
from requests.api import request
import googlemaps 
import requests
from urllib.parse import urlencode
import json
from textblob import TextBlob

def googlesearch(Key_ID, search_string):

    #Send request to googlemaps
    response = requests.get(
        'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?' + urlencode(
            {'input' : search_string, 'inputtype': 'textquery', 'key':Key_ID }))

    resp_details = response.json()

    if resp_details['status'] == 'OK': 
        lat = resp_details['results'][0]['geometry']['location']['lat']
        lng = resp_details['results'][0]['geometry']['location']['lng']
        place_id = resp_details['results'][0]['place_id']
        return [lat, lng, place_id]

    else:
        print('Failed to get json response:', resp_details)
        return ['place_id is not found', search_string] 




def get_place_details(place_id, api_key):
    # Send request by API
    response = requests.get(
        'https://maps.googleapis.com/maps/api/place/details/json?' + urlencode(
            {'place_id': place_id, 'key': api_key}))
    # Read response as json
    resp_details = response.json()
    # status=OK: the place was successfully detected and at least one result was returned
    for i in range(len(resp_details)):

     if resp_details['status'] == 'OK':
        for i in range(len(resp_details)):
            review_rating = resp_details['result']['reviews'][i]['rating']
            review_time = resp_details['result']['reviews'][i]['relative_time_description']
            review_timestamp = resp_details['result']['reviews'][i]['time']
            review_text = resp_details['result']['reviews'][i]['text']
            return [place_id, review_rating, review_time, review_timestamp, review_text]
     else:
        print('Failed to get json response:', resp_details)
        return ['Review is not found', place_id]



def sentiment_analysis(Reviews):

    for i in range(len.Reviews):
        zen = TextBlob(i)
        return zen.sentiment.polarity

    



