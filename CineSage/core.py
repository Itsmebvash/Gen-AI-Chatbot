from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatMistralAI(
    model = "mistral-large-latest")

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert movie information extraction assistant.

Analyze the provided paragraph and extract the most useful information
about the movie.

Extract the following information when available:

- Movie Name
- Release Year
- Director
- Genre
- Main Cast
- Plot
- Setting / Location
- Main Themes
- Music / Composer
- IMDb Rating
- Critical Reception
- Notable Facts

Also provide a quick summary of the paragraph in 2-3 sentences.

Rules:
- Use only the information provided in the paragraph.
- Do not use outside knowledge.
- Do not invent missing information.
- If something is not mentioned, write "Not mentioned".
- Keep the extracted information concise.
- List each cast member separately.
- List multiple genres or themes separately.
- Do not copy the entire paragraph under Plot.
- Correct obvious spelling mistakes only when the intended meaning is clear.

Return the information in a clean and readable format.
"""
    ),
    (
        "human",
        """
Extract useful information from this paragraph:

{paragraph}
"""
    )
])

para = input("Enter your paragraph: ")

final_prompt = prompt.invoke({"paragraph": para})

response = model.invoke(final_prompt)

print(response.content)
