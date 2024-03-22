# gemini_bug_example_api

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
 * Detected change in 'gemini_bug_example_api/api/controller/chat_controller.py', reloading
 * Restarting with stat
 * Detected change in 'gemini_bug_example_api/api/model/chat_request.py', reloading
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
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/app.py", line 1463, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/app.py", line 873, in full_dispatch_request
    return self.finalize_request(rv)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/app.py", line 892, in finalize_request
    response = self.make_response(rv)
               ^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/app.py", line 1183, in make_response
    rv = self.json.response(rv)
         ^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/json/provider.py", line 214, in response
    f"{self.dumps(obj, **dump_args)}
", mimetype=self.mimetype
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/json/provider.py", line 179, in dumps
    return json.dumps(obj, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/json__init__.py", line 238, in dumps
    **kw).encode(obj)
          ^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/json/encoder.py", line 200, in encode
    chunks = self.iterencode(o, _one_shot=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/json/encoder.py", line 258, in iterencode
    return _iterencode(o, 0)
           ^^^^^^^^^^^^^^^^^
  File ".pyenv/versions/3.12.2/lib/python3.12/site-packages/flask/json/provider.py", line 121, in _default
    raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")
TypeError: Object of type Content is not JSON serializable
127.0.0.1 - - [22/Mar/2024 09:04:03] "POST /api/v1/chat-message HTTP/1.1" 500 -
```

