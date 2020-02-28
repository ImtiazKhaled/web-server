import re
import sys
from flask import Flask, make_response

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# the default page that is displayed
# when url is not provided
@app.route('/')
def default():
    try:
    # opens the index.html file in the current directory
      with open('index.htm') as file:
        file_display = file.read()
      return make_response(file_display, 200)
    except IOError:
      print ("Error: File does not appear to exist.")
      return make_response("that page does not exist", 404)    

# catches all urls that are provided
@app.route('/<path:url>')
def getAll(url):
    # regex to mactch if the query
    index_match = '^((\/.*)*.html)|((\/.*)*.htm)$'
    url_matched = re.match(index_match,'/'+url)
    if url_matched == None:
      # if the path entered is not valid
      return make_response("bad request", 400)
    else:
      # if the path entered is valid
      try:
      # opens the file that is provided in the url
        with open(url) as file:
          file_display = file.read()
        return make_response(file_display, 200)
      except IOError:
      # returns page doesnt exists if the url has a
      # non existing file path
        return make_response("that page does not exist", 404)    

if __name__ == '__main__':
    # port number defaults to 8080 if one is not
    # provided through the command line
    port = len(sys.argv) > 1 and sys.argv[1] or 8080
    app.run(port=port)