import random
from semantic_kernel.functions import kernel_function

class FunFactsPlugin:
    """
    A Semantic Kernel plugin that provides fun space facts.
    """
    SPACE_FACTS = [
        "The Sun makes up 99.86% of the total mass of the Solar System.",
        "Jupiter has the shortest day of all the planets in our Solar System, spinning once every 9 hours and 56 Earth minutes.",
        "Saturn's rings are made mostly of chunks of ice and rock.",
        "Uranus spins on its side.",
        "Neptune was the first planet located through mathematical predictions rather than direct astronomical observation.",
        "A light-year is the distance that light travels in one Earth year – about 9.46 trillion kilometers.",
        "The Milky Way galaxy is estimated to contain 100-400 billion stars.",
        "Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape.",
        "The International Space Station (ISS) orbits Earth at an average altitude of 400 kilometers (250 miles).",
        "Mars is known as the 'Red Planet' due to the iron oxide (rust) on its surface.",
    ]

    @kernel_function(
        description="Get a random fun fact about space.",
        name="GetSpaceFact",
    )
    async def get_space_fact(self) -> str:
        """
        Returns a random fun fact about space.
        """
        return random.choice(self.SPACE_FACTS)