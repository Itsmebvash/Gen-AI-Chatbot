# from dotenv import load_dotenv
# # from langchain.chat_models import init_chat_model

# load_dotenv()

# model = init_chat_model(
#     "llama-3.3-70b-versatile",
#     model_provider="groq"
# )

# response = model.invoke("What is cricket?")

# print(response.content)

## We can use other models also

## Mistral AI

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "mistral-large-latest",
    model_provider="mistralai",
    temperature=0,
)

response = model.invoke("Write a poem about the beauty of nature.")

print(response.content)



