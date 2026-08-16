# Now I am going to download one model from HuggingFace and create embeddings using the langchain_huggingface library. The model I will use is "sentence-transform

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Hello, this is Bhavya Vashisht",
    "Hello, your name is Youtube",
    "And you all are very beautiful"
]
vector = embeddings.embed_documents(texts)

print(vector)
print(f"Dimensions: {len(vector)}")

# from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings

# load_dotenv()

# embeddings = OpenAIEmbeddings(
#     model = 'text-embedding-3-large',
#     dimensions = 64
# )

# vector = embeddings.embed_query("You are going to learn Gen AI")

# print(vector)