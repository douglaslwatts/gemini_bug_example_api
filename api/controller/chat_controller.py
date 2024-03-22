from vertexai.generative_models import (
    GenerativeModel,
    GenerationConfig,
    HarmCategory,
    HarmBlockThreshold
)

from flask_openapi3 import APIView, Tag

from api.model import ChatRequest, ChatResponse

api_key = {
    'type': 'api_key',
    'scheme': 'bearer',
    'bearerFormat': 'api_key'
}

security = [{'api_key': []}]

api_view = APIView(url_prefix='/api/v1/',
                   view_tags=[Tag(name='Chat Requests')],
                   view_security=security)


@api_view.route('/chat-message')
@api_view.doc(description='Get an AI chat message')
class ChatController:

    def post(self, body: ChatRequest):

        generation_config = GenerationConfig(
            temperature=0.0,
            top_k=1,
            top_p=0.0,
            max_output_tokens=2048
        )

        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
        }

        model = GenerativeModel(model_name='gemini-pro',
                                generation_config=generation_config,
                                safety_settings=safety_settings)

        # Uncomment the below line and comment out the line below it to see the not JSON serializable error

        # conversation = model.start_chat(history=body.history)
        conversation = model.start_chat()

        response = conversation.send_message(body.prompt)

        response_message = response.text
        print(conversation.history)

        # Uncomment the below line and comment out the line below it to see the not JSON serializable error

        # return ChatResponse(response=response_message, history=conversation.history).model_dump()
        return ChatResponse(response=response_message).model_dump()

