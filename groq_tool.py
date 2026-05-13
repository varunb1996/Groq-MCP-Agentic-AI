import os
from groq import Groq
from dotenv import load_dotenv
from utils.config import MODEL_NAME

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def query_groq(prompt):

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content