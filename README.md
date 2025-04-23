# Outfit-recommendation-Using-Agentic-AI
# Skin Tone Analyzer

## Overview
Skin Tone Analyzer is a Python application that analyzes images of people, identifies their skin tone, and provides personalized outfit recommendations based on the analysis. The application uses Claude 3.5 Sonnet, an advanced AI model from Anthropic, to process images and generate tailored fashion advice.

## Features
- Image analysis to determine skin tone/color
- Personalized outfit recommendations based on skin tone
- Interactive command-line interface
- Streaming response for real-time feedback

## Requirements
- Python 3.8+
- Anthropic API key (for Claude 3.5 Sonnet)
- Internet connection (for DuckDuckGo search functionality)

## Installation

### 1. Install the required packages

```bash
pip install agno
```

### 2. Set up your API credentials
You'll need an Anthropic API key to use Claude 3.5 Sonnet. You can replace "Your_api_key" in the code with your actual API key, or use environment variables for better security.

## Usage

1. Save the script to a file (e.g., `skin_tone_analyzer.py`)
2. Run the script:
   ```bash
   python skin_tone_analyzer.py
   ```
3. When prompted, enter the relative path to your image file
4. The application will analyze the image and provide outfit recommendations based on the detected skin tone

## Code Explanation

The script uses the following components:

- `Agent` from the `agno` library to handle the AI interactions
- Claude 3.5 Sonnet as the AI model for image analysis
- DuckDuckGo search tools for additional information retrieval
- `pathlib` for file path handling
- Streaming responses for real-time feedback

## Example

```
$ python skin_tone_analyzer.py
Enter the path to the image file: photos/portrait.jpg
Analyzing image...
Skin tone detected: Medium olive
Recommended outfits:
- Rich jewel tones like emerald green, sapphire blue, and burgundy
- Earth tones like olive, terracotta, and mustard yellow
...
```

## Customization

You can modify the prompt to request different types of analysis or recommendations:

```python
agent.print_response(
    "Analyze the Image to find the skin color/skin tone of the person and recommend summer casual wear.",
    images=[Image(content=image_bytes)],
    stream=True,
)
```

## Security Notes

- Do not hardcode your API key in production code
- Consider implementing user consent mechanisms before analyzing personal images
- Be mindful of privacy concerns when handling personal photos

## License
[Specify your license information here]
