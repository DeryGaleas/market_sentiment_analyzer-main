from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from requests.api import request
import googlemaps 
import requests
from urllib.parse import urlencode
import json
from textblob import TextBlob


class GoogleMaps_Query(APIView):

    def get_place_id(api_key, search_string):
            #Send request to googlemaps
        response = requests.get(
            'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?' + urlencode(
            {'input' : search_string, 'inputtype': 'textquery', 'key':api_key }))

        resp_details = response.json()

        if resp_details['status'] == 'OK': 
            lat = resp_details['results'][0]['geometry']['location']['lat']
            lng = resp_details['results'][0]['geometry']['location']['lng']
            place_id = resp_details['results'][0]['place_id']
            return Response({'lat':lat, 'lng':lng, 'place_id':place_id})

        else:
            print('Failed to get json response:', resp_details)
            error = (f'place_id is not found {search_string}')
            return Response({'error':error})




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
                    return Response({'place_id':place_id, 'review_rating':review_rating, 'review_time':review_time, 'review_timestamp':review_timestamp, 'review_text':review_text})
            else:
                print('Failed to get json response:', resp_details)
                error = f'Review is not found {place_id}'
                return Response({'error':error})