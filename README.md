# gemini&#95;bug&#95;example&#95;api

```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
[role: "user"
parts {
  text: "How high do eagles fly?"
}
, role: "model"
parts {
  text: "Eagles can fly at altitudes of up to 10,000 feet (3,000 meters) above sea level."
}
]
127.0.0.1 - - [22/Mar/2024 08:59:13] "POST /api/v1/chat-message HTTP/1.1" 200 -

```


```
 * Detected change in 'gemini&#95;bug&#95;example&#95;api/api/controller/chat&#95;controller.py', reloading
 * Restarting with stat
 * Detected change in 'gemini&#95;bug&#95;example&#95;api/api/model/chat&#95;request.py', reloading
 * Restarting with stat
[role: "user"
parts {
  text: "How high do eagles fly?"
}
, role: "model"
parts {
  text: "Eagles can fly at altitudes of up to 10,000 feet (3,000 meters) above sea level."
}
]
[2024-03-22 09:04:03,805] ERROR in app: Exception on /api/v1/chat-message [POST]
Traceback (most recent call last):
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/app.py", line 1463, in wsgi&#95;app
    response = self.full&#95;dispatch&#95;request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/app.py", line 873, in full&#95;dispatch&#95;request
    return self.finalize&#95;request(rv)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/app.py", line 892, in finalize&#95;request
    response = self.make&#95;response(rv)
               ^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/app.py", line 1183, in make&#95;response
    rv = self.json.response(rv)
         ^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/json/provider.py", line 214, in response
    f"{self.dumps(obj, **dump&#95;args)}
", mimetype=self.mimetype
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/json/provider.py", line 179, in dumps
    return json.dumps(obj, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/json&#95;&#95;init&#95;&#95;.py", line 238, in dumps
    **kw).encode(obj)
          ^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/json/encoder.py", line 200, in encode
    chunks = self.iterencode(o, &#95;one&#95;shot=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/json/encoder.py", line 258, in iterencode
    return &#95;iterencode(o, 0)
           ^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/json/provider.py", line 121, in &#95;default
    raise TypeError(f"Object of type {type(o).&#95;&#95;name&#95;&#95;} is not JSON serializable")
TypeError: Object of type Content is not JSON serializable
127.0.0.1 - - [22/Mar/2024 09:04:03] "POST /api/v1/chat-message HTTP/1.1" 500 -
```

