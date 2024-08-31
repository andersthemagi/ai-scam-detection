# Guardian AI - Scam detection and prevention



Identity theft and fraud have become alarmingly prevalent, with imposter scams emerging as the most common method. In 2023, the US Federal Trade Commission received over 856,000 reports of imposter scams, accounting for 43% of all fraud complaints and $2.7 billion in losses. The UK saw 45,367 impersonation scam cases in 2022, costing £177.6m.

Scams target vulnerable individuals, including the elderly, with four people aged 50+ scammed in England and Wales every minute. Older people often face unique risk factors, including isolation, digital literacy skill needs, and cognitive impairments, making them prime targets for fraudsters.

Our proposed solution is an AI-powered mobile and desktop application called "GuardianAI" that leverages advanced machine learning techniques to detect and prevent scams across various communication channels. The app will integrate seamlessly with users' devices to monitor communication channels, e.g. text messages, emails, and voice calls, for potential scam indicators.

Made during the [Hackathon for Technical AI Safety Startups.](https://www.apartresearch.com/event/ais-startup-hackathon) See [the full writeup here](https://docs.google.com/document/d/1SCztrhkaBOqpKkgcZsuhX8VfFEKtrqzWrK09s6eIBsg/edit?usp=sharing). 

Created by:
- [Andres Sepulveda Morales](https://www.linkedin.com/in/andres-sepulveda-morales/)
- [Doroteya Stoyanova](https://www.linkedin.com/in/doroteya-stoyanova-9a4848199/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
- [Junfeng (James) Feng](https://www.linkedin.com/in/junfeng-james-feng-5a22a9263/)
- [Patrick Huang](https://www.linkedin.com/in/patrickphuang/)
- [Wanjie Zhong](https://www.linkedin.com/in/wanjie-zhong-846b25288/)

## Requirements

- Python 3.12.3

Python package list is contained in `requirements.txt`. 

You may need to install additional extensions to utilize Python on your editor of choice. Consider https://marketplace.visualstudio.com/items?itemName=ms-python.python if you're using VSCode. 

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