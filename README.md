# Web Client and Server

## Run Instructions

### Server
The server is written in ``python3`` and its dependencies are ``flask``, if you're using an UNIX enviroment, install all the dependencies with the command
 ````
 python3 start.py
 ````
in this directory. Or manually install the dependencies. 

After installing the dependencies, run
 ````
 python3 server.py <portnumber>
 ```` 
to start the webserver, the port number is optional, and if not provided the web server listens on port ``8080``.

### Client
The Client is done in vanilla python3, so no dependencies are required. After starting the server, run
```
python3 client.py <portnumber> <directory>
```
where portnumber and directory are optional, portnumber defaults to 8080, and directory defaults to ' '. ``The portnumber of the client and server must match``, ``Directory should list the directory required without a '/' to start with``. and example command would be,
```
python3 client.py 8080 test/index.html
```


## References

[flask](https://palletsprojects.com/p/flask/ "flask py documentaion"),
[sys](https://docs.python.org/3/library/sys.html "sys py documentaion"),
[requests](https://requests.readthedocs.io/en/master/ "requests py documentaion")
