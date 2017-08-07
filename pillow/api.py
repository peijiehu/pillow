#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Interface to query Zillow APIs to get information about homes.
Returns data in json.
"""

import json
import requests
import xmltodict
from error import PillowError

BASE_URL = "http://www.zillow.com/webservice"
ZWS_ID = "X1-ZWz1dyb53fdhjf_6jziz"

def search_by_address(address, citystatezip, rentzestimate=False):
    """
    Zillow GetSearchResults API finds a property for a specified address.
    """
    url = '%s/GetSearchResults.htm' % (BASE_URL)
    parameters = {'zws-id': ZWS_ID}
    if address and citystatezip:
        parameters['address'] = address
        parameters['citystatezip'] = citystatezip
    else:
        raise PillowError({'message': 'address and citystatezip are required.'})
    response = requests.get(url, params=parameters)
    response = xmltodict.parse(response.content)
    results = response['SearchResults:searchresults']['response']['results']['result']
    return results


if __name__ == 'main':
    json_data = search_by_address("2114 Bigelow Ave", "Seattle, WA")
    print json.dumps(json_data, indent=2)

    json_data = search_by_address("Bigelow Ave", "Seattle, WA")
    print json.dumps(json_data, indent=2) # code 508, no exact match found
