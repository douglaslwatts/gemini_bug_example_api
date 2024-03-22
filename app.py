from flask_openapi3 import Info, OpenAPI
from dotenv import load_dotenv

from api.controller import ai_chat_view

info = Info(title="AI Chat API", version="1.0.0")
app = OpenAPI(__name__, info=info)

app.register_api(ai_chat_view)
app.doc_prefix = '/docs'

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
