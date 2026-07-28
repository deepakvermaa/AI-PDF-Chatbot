from config import GEMINI_MODEL

def generate_answer(client, question, context, chat_history):
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the information provided in the context.

If the answer is not available in the context, reply:
"I couldn't find the answer in the provided document."

Use the previous conversation only to understand follow-up questions like "he", "she", "it", "their", etc.

Previous Conversation:
{chat_history}


Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text
