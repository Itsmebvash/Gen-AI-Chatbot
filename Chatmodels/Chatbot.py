from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = init_chat_model(
    "mistral-large-latest",
    model_provider="mistralai",
    temperature=0,
)
messages = [
      SystemMessage(content="You are a funny AI Agent."),
      
]

print("----------------Welcome type 0 to exit the application----------------")

while True:
    prompt = input("Enter your prompt: ")
    messages.append(HumanMessage(content=prompt))

    if prompt == "0":
            break
    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))
    print("Bot :", response.content)

print(messages)