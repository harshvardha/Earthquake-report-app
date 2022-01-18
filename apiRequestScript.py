import requests
PAYLOAD_MOST_RECENT = {'starttime':0,'endtime':0}
PAYLOAD_MIN_MAGNITUDE = {'minmagnitude':0}
URL_1 = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02'
URL_2 = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=5'
def getEarthQuakeData(Type,starttime = None,endtime = None,minmagnitude = None):
    r = None
    if(Type=="most recent"):
        PAYLOAD_MOST_RECENT['starttime'] = starttime
        PAYLOAD_MOST_RECENT['endtime'] = endtime
        r = requests.get(URL_1,PAYLOAD_MOST_RECENT)
    elif(Type=="min magnitude"):
        PAYLOAD_MIN_MAGNITUDE['minmagnitude'] = minmagnitude
        r = requests.get(URL_2,PAYLOAD_MIN_MAGNITUDE)
    data = r.json()
    return data['features']