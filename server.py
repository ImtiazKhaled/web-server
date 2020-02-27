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
      file = open("index.html", "r").read()
      return make_response(file, 200)
    except IOError:
      print ("Error: File does not appear to exist.")
      return make_response("that page does not exist", 404)    

# catches all urls that are provided
@app.route('/<path:url>')
def getAll(url):
    try:
    # opens the file that is provided in the url
      file = open(url, "r").read()
      return make_response(file, 200)
    except IOError:
    # returns page doesnt exists if the url has a
    # non existing file path
      return make_response("that page does not exist", 404)    

if __name__ == '__main__':
    # port number defaults to 8080 if one is not
    # provided through the command line
    port = len(sys.argv) > 1 and sys.argv[1] or 8080
    app.run(port=port)