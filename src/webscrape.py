#=======================================================
# File: webscrape.py
# Description:  Search html for text and extract queryTerms
# Created: 09.07.2019
# Updated: 
# Author: Andrea Chamorro
#=======================================================

from bs4 import BeautifulSoup

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

def parseQueryTermsFromHTMLContent(HTMLContent):
    soup = BeautifulSoup(html_doc, HTMLContent)
    pageText = soup.get_text()

    queryTerms = []

    #split and filter
    queryTerms = getArrayOfOrderedWords(pageText)
        
    #tokenize
    queryTerms = tokenizeArrayofWords(wordArray)

