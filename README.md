# AI Scam Detection

This description will be built out as we continue working on the project. 

Made for the AI Tech Startup Hackathon. 

Created by Andres Sepulveda Morales & Patrick Huang

## Requirements

- Python 3.12.3

Python package list is contained in `requirements.txt`. 

## Installation Instructions

I am utilizing my CMD on Windows, however most steps will be similar for MacOs / Linux. 

1. Clone this repository to your local device
```
# Terminal
git clone https://github.com/andersthemagi/ai-scam-detection
```

2. Navigate to the folder where your project resides.
```
# Terminal
cd ai-scam-detection
```

3. Install all required python packages using the following command
```
# Terminal
pip install -r requirements.txt
```

4. You will need to create a `secrets.toml` file in the `.streamlit` directory. In the file, please include your OPENAI_API_KEY variable.

```
OPENAI_API_KEY = "API KEY HERE"
```

5. Once that process completes, you should be able to create a local instance of the streamlit app using:
```
# Terminal
streamlit run app.py
```