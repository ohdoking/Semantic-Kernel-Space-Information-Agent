"""
Space Chatbot Streamlit Application

This module implements a conversational AI assistant for space-related queries,
integrating with OpenAI's API and Semantic Kernel for plugin management.
"""

# Core dependencies
import streamlit as st
import asyncio
import os
import logging
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, OpenAIChatPromptExecutionSettings
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.contents.chat_history import ChatHistory

# Custom plugin imports
from plugins.SpacePlugin import SpacePlugin
from plugins.FunFactsPlugin import FunFactsPlugin

# Environment configuration
load_dotenv()
service_id = "space_service"

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

async def chat_with_llm(
    kernel: Kernel,
    history: ChatHistory,
    prompt: str,
    chat_completion_service: OpenAIChatCompletion
) -> str:
    """
    Processes user input through LLM with plugin integration.

    Args:
        kernel: Initialized Semantic Kernel instance
        history: Conversation history context
        prompt: User's input message
        chat_completion_service: Configured OpenAI service

    Returns:
        str: Generated response from LLM
    """
    execution_settings = OpenAIChatPromptExecutionSettings(
        service_id=service_id,
        function_choice_behavior=FunctionChoiceBehavior.Auto(
            filters={"included_plugins": ["SpacePlugin", "FunFactsPlugin"]}
        )
    )
    
    history.add_user_message(prompt)
    result = await chat_completion_service.get_chat_message_content(
        chat_history=history,
        settings=execution_settings,
        kernel=kernel
    )
    return str(result)

async def main():
    """Main application flow for Streamlit space chatbot."""
    # Initialize AI kernel
    kernel = Kernel()

    # Configure OpenAI integration
    chat_completion_service = OpenAIChatCompletion(
        ai_model_id=os.getenv("OPENAI_CHAT_MODEL_ID"),
        api_key=os.getenv("OPENAI_API_KEY"),
        service_id=service_id
    )

    # Register custom plugins
    kernel.add_plugin(SpacePlugin(), "SpacePlugin")
    kernel.add_plugin(FunFactsPlugin(), "FunFactsPlugin")

    # Initialize session state
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = ChatHistory()

    # Application UI Layout
    st.markdown("""
    <style>
        .header { position: sticky; top: 0; background: white; z-index: 100; }
        .chat-container { margin-top: 120px; height: 65vh; overflow-y: auto; }
        .input-container { position: fixed; bottom: 0; width: 100%; background: white; }
    </style>
    """, unsafe_allow_html=True)

    # Header Section
    with st.container():
        st.title("🚀 Cosmic Chatbot")
        st.caption("Ask about space, type 'apod' for astronomy picture, or 'fact' for trivia")

    # Chat Message Display
    chat_container = st.container()
    with chat_container:
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display message history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Chat Input Handling
    if prompt := st.chat_input("Your space question:"):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate AI response
        response = await chat_with_llm(
            kernel,
            st.session_state["chat_history"],
            prompt,
            chat_completion_service
        )

        # Process image URLs
        image_url = None
        if "Image URL: " in response:
            image_url = response.split("Image URL: ")[1].split("\n")[0]
            response = response.replace("Image URL: " + image_url, "")

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(response)
        
        # Update message history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "image": image_url if image_url else None
        })

if __name__ == "__main__":
    asyncio.run(main())