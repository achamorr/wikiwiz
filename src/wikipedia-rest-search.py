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

def wikiRestAPISearch(queryTerm, downloadImage = False):
    '''
    Using wikipedia Python API: https://www.simplifiedpython.net/wikipedia-api-python/
    downloadImage = if want to download image and return local location as imgURL
    '''
    try:
        page = wikipedia.page(queryTerm)
    except Exception:
        return None

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


    if DEBUG:
        print (title, url, summary, imageLoc)

    return (title, url, summary, imageLoc)



if __name__ == "__main__":
    #wikiRestSimpleSearch(QUERY_TERM)
    wikiRestAPISearch(QUERY_TERM, downloadImage= True)



