"""Utility functions for interacting with the Groq LLM."""
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from app.core.config import settings


async def get_llm_response(prompt: str) -> str:
    """Get a response from the Groq LLM based on the provided prompt.
    """
    try:
        model = ChatGroq(
            model_name=settings.GROQ_MODEL,
            api_key=settings.GROQ_API_KEY,
            temperature=0.7,
            max_tokens=1500,
            top_p=0.9,
        )

        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful assistant."),
                ("user", prompt),
            ]
        )

        chain = prompt_template | model
        response = await chain.ainvoke({"user_prompt": prompt})
        return response.content

    except Exception as e:
        print(f"Error in getting LLM response: {e}")
        return "An error occurred while processing your request."
