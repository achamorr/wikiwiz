#=======================================================
# File: wikipedia-rest-search.py
# Description:  Search Wikimedia REST API for terms
# Created: 09.07.2019
# Updated: 
# Author: Andrea Chamorro
#=======================================================

import os, sys, shutil, datetime, random
import urllib, json

import wikipedia

#===GLOBAL VARIABLES==
#QUERY_TERM = "lkfakdsf"
QUERY_TERM = "Babe Ruth"
DEBUG = True

def convertTermToSearchTerm(queryTerm):
    pass


def wikiRestSimpleSearch(queryTerm):
    url = "https://en.wikipedia.org/api/rest_v1/page/summary" + queryTerm

    response = urllib.urlopen(url)
    reads = json.loads(response.read())

    print (reads)

def wikiPythonAPISearch(queryTerm, downloadImage = False):
    '''
    Using wikipedia Python API: https://www.simplifiedpython.net/wikipedia-api-python/
    downloadImage = if want to download image and return local location as imgURL
    '''
    try:
        page = wikipedia.page(queryTerm)
    except Exception:
        return None

    #init
    title = "None"
    url= "None"
    summary = "None
    imageLoc = "None"

    #name
    title = page.title

    #url
    url = page.url

    #summary
    summary = wikipedia.summary(queryTerm)

    #image
    imageLoc = page.images[0]
    if downloadImage:
        #unique-ify
        now = datetime.datetime.now()
        dateTimeStamp = now.strftime("%m.%d.%Y.%H.%M.%S")
        randomStamp = random.randint(1,500)

        #request
        imageUniqueName = "%s_%s_%s.jpg" %(queryTerm,randomStamp,dateTimeStamp)
        urllib.request.urlretrieve(imageLoc, imageUniqueName)

        #local 
        localDir = os.path.dirname(os.path.abspath(__file__))
        localPath = os.path.join(localDir, imageUniqueName)

        #new
        newDir = os.path.join(localDir,"img")
        newPath =  os.path.join(newDir,imageUniqueName)

        #create new
        if not os.path.exists(newDir):
            os.mkdir(newDir)
        
        #move
        os.rename(localPath, newPath)
        imageLoc = newPath

    #to Json
    if DEBUG:
        print (title, url, summary, imageLoc)

    return (title, url, summary, imageLoc)
       
        
def implementWikiApiAll(queryList):
    try:
        dictAllTerms = {"content": []}
        for queryTerm in queryList:
            if queryTerm not in dictAllTerms.keys():
                title, url, summary, imageLoc = wikiPythonAPISearch(queryTerm)

                #define
                dict_data = {
                "queryTerm": queryTerm,
                "title": title,
                "url": url,
                "summary": summary,
                "imageLoc": imageLoc
                }
                dictAllTerms["content"].append(dict_data)
        return json.dumps(dictAllTerms, indent = 4)
    except:
        return json.dumps({"content" : []]})



if __name__ == "__main__":
    #wikiRestSimpleSearch(QUERY_TERM)
    wikiPythonAPISearch(QUERY_TERM, downloadImage= True)



