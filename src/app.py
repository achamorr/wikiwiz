from flask import Flask, request
from wikipedia-rest-search import wikiPythonAPISearch, convertToJson

app = Flask(__name__)
#App secret key?

@app.route("/", methods = ['POST'])
def processPOST():
    queryString = request.form['queryCommaSeparated'] #if 1, return list of len 1
    queryList = queryString.split(',')

    if queryList is None:
        queryList = []
        
    #process
    jsonText = implementWikiApiAll(queryList)


if __name__ == "__main__":
    app.run()
