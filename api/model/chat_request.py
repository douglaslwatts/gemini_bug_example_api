from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from vertexai.generative_models import Content


class ChatRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    prompt:str = Field(None,
                       description="prompt for AI")

    context: Optional[str] = Field(None,
                                   description="prompt for AI")

    # Uncomment the below field to see the not JSON serializable error

    # history: Optional[list[Content]] = Field(None,
    #                                          description='AI chat history')


class ChatResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
    response: str = Field(None,
                          description='Response from AI'),

    # Uncomment the below field to see the not JSON serializable error

    # history: list[Content] = Field(None,
    #                                description='AI chat history')
