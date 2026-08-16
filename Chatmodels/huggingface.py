from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1")

model = ChatHuggingFace(
    llm=llm)

response = model.invoke("What is Gen AI and how can we learn this?")

print(response.content)


