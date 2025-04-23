from pathlib import Path
from agno.agent import Agent
from agno.media import Image
from agno.models.anthropic.claude import Claude
from agno.tools.duckduckgo import DuckDuckGoTools

agent = Agent(
    model=Claude(id="claude-3-5-sonnet-20241022", api_key="Your_api_key"),
    tools=[DuckDuckGoTools()],
    markdown=True
)

user_path = input("Enter the path to the image file: ")

image_path = Path(__file__).parent.joinpath(user_path)

# Read the image file content as bytes
image_bytes = image_path.read_bytes()

agent.print_response(
    "Analyze the Image to find the skin color/skin tone of the person in the image and Recommend a suitable outfit for the person.",
    images=[
        Image(content=image_bytes),
    ],
    stream=True,
)
