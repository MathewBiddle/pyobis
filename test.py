# import requests
import pandas as pd


def getExtensions(data):
    lis=[]
    a = pd.json_normalize(data, "mof", ["scientificName", "eventDate","id"])
    ids = a.id.unique()    
    for i in range(len(ids)):
        lis+= [a[a['id']==ids[i]] ] #whichever id the user wants or we can iter through a loop for each id.
    return lis

def returnMOF():
    response = occurrences.search(scientificname="Abra",mof=True,hasextensions="MeasurementOrFact") 
    # requests.get("https://api.obis.org/occurrence?scientificname=Abra&mof=true&hasextensions=MeasurementOrFact")
    results = response["results"]
    print(getExtensions(results))

from pyobis import taxa
res=taxa.annotations(scientificname="Egg")
print(res["results"])
print(pd.DataFrame(res["results"]))