import sys
import requests

if __name__ == '__main__':
    port = len(sys.argv) > 1 and sys.argv[1] or '8080'
    file = len(sys.argv) > 2 and sys.argv[2] or ''
    url = 'http://localhost:'+port+'/'+file
    receive = requests.get(url)
    print('the status code is:', receive.status_code)
    print('the server url is:', url)
    print(receive.text)