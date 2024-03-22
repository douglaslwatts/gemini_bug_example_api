# gemini_bug_example_api

## Bug

When using the chat-bison models, we can return the chat session history in the response body, and
accept it in the request body with success using a list of `ChatMessage`, which is the history data
structure used for those models. However, when we try this using Gemini, there is an error stating
that the `Content` object, which is the history data structure for Gemini models, is not JSON
serializable.

## Bug Repro Instructions

1. Create a service acount JSON credentials file and place it in the root of the project with the
   name `vertex_creds.json`. The `GOOGLE_APPLICATION_CREDENTIALS` environment variable already
   points to this file name/location in the `.env` file.
2. Ensure that you are using Python 3.12.2 (`python -V` -> `Python 3.12.2`)
3. `python -m venv venv`
4. `source venv/bin/activate`
5. `pip3 install -r requirements.txt`
6. `flask run --reload`
7. Send a request to http://localhost:5000/api/v1/chat-message with the following request body
   using your favorite tool such as Insomia, Postman, curl, etc.

```
{
    "prompt": "How high do eagles fly?"
}
```
8. See successful response, and `Content` object printed to console as below

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
9. In `api/model/chat_request.py`:<br>Uncomment lines 16, 17, 27 and 28<br>
   In `api/controller/chat_controller.py`:<br>Uncomment lines 51 and 61<br>comment out lines 52 and 62
10. Send the same request again and see the `Content` object still printed out but with the below error
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
The above demonstrates the bug for attempting to return the history in the response. Ideally, we
will also be able to take that exact history which is returned, and send it in a subsequent request
in the optional `history` field in the request model. However, this does not work as the same bug
applies there as well.

