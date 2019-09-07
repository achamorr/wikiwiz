#=======================================================
# File: webscrape.py
# Description:  Search html for text and extract queryTerms
# Created: 09.07.2019
# Updated: 
# Author: Andrea Chamorro
#=======================================================

from bs4 import BeautifulSoup

from google.cloud import language_v1
from google.cloud.language_v1 import enums

#===GLOBAL VARIABLES==
HTML_TEST = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

def isLegalType(word):
    # @todo: dictionary check?

    #filter stop words
    invalidDict = [None, "a", "for", "to", "and"]
    if word in invalidDict:
        return False
    return True

def getArrayOfOrderedWords(htmlString):
    htmlArray = htmlString.strip().split()
    htmlArray = [word for word in htmlArray if isLegalType(word)]
    return htmlArray

def tokenizeArrayOfWords(wordArray):
    pass

def initGoogleClientText():
    client = language_v1.LanguageServiceClient()

    type_ = enums.Document.Type.PLAIN_TEXT

    #autodetect language
    # @todo: allow this for several different languages :)

    document = {"content": wordString,
                "type": type_
                }
    
    encoding_type = enums.EncodingType.UTF8

    return client, document, encoding_type
    


def getEntitiesFromString(wordString):
    #init
    client, document, encoding_type = initGoogleClientText()

    response = client.analyze_entities(document, encoding_type = encoding_type)
    
    #entitiesArray = [entity.name for entity in response.entities]
    typesDict = {entity.name:entity.type for entity in response.entities}
    metadataDict = entity.metadata

    return typesDict, metadataDict

def getContentClassification(wordString):
    client, document, encoding_type = initGoogleClientText()

    response = client.classify_text(document)

    categoriesWithConfidenceList = [(category.name, category.confidence) for category in response.categories]

def parseQueryTermsFromHTMLContent(htmlString):
    soup = BeautifulSoup(htmlString, "html.parser")
    pageText = soup.get_text()

    queryTerms = []
    contentClassification = None

    #split and filter
    wordArray = getArrayOfOrderedWords(pageText)
        
    #tokenize
    queryTypesDict, queryMetaDict = getEntitiesFromString(pageText)

    #content classification, for good times
    categoriesWithConfidenceList = getContentClassification(pageText)

    return queryTypeDict, queryMetaDict, categoriesWithConfidenceList


if __name__ == "__main__":
    queryTypeDict, queryMetaDict, categoriesWithConfidenceList = parseQueryTermsFromHTMLContent(HTML_TEST)

    print (HTML_TEST)
    print (queryTypeDict, queryMetaDict, categoriesWithConfidenceList)