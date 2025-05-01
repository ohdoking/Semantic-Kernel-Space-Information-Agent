import requests
import os
from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function
from dotenv import load_dotenv

load_dotenv()

class SpacePlugin:
    """
    A Semantic Kernel plugin that provides information about space, specifically using the NASA APOD API.
    """
    @kernel_function(
        description="Get the Astronomy Picture of the Day (APOD) from NASA.",
        name="GetAPOD",
    )
    async def get_apod(self) -> str:
        """
        Calls the NASA APOD API to retrieve information (title, explanation, image URL)
        for the Astronomy Picture of the Day using an environment variable for the API key.
        """
        api_key = os.environ.get("NASA_API_KEY")
        if not api_key:
            return "Error: NASA API key is not set in environment variables."

        api_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            title = data.get("title", "No Title")
            explanation = data.get("explanation", "No Explanation")
            image_url = data.get("url", "No Image URL")
            return f"Today's Astronomy Picture:\nTitle: {title}\nExplanation: {explanation}\nImage URL: {image_url}"
        except requests.exceptions.RequestException as e:
            return f"Error fetching APOD data: {e}"