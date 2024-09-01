import streamlit as st
from menu import menu

menu()

st.title('Guardian AI - Scam detection and prevention')

st.markdown("""
    Identity theft and fraud have become alarmingly prevalent, with imposter scams emerging as the most common method. In 2023, the US Federal Trade Commission received over 856,000 reports of imposter scams, accounting for 43% of all fraud complaints and $2.7 billion in losses. The UK saw 45,367 impersonation scam cases in 2022, costing £177.6m.

    Scams target vulnerable individuals, including the elderly, with four people aged 50+ scammed in England and Wales every minute. Older people often face unique risk factors, including isolation, digital literacy skill needs, and cognitive impairments, making them prime targets for fraudsters.

    Our proposed solution is an AI-powered mobile and desktop application called "GuardianAI" that leverages advanced machine learning techniques to detect and prevent scams across various communication channels. The app will integrate seamlessly with users' devices to monitor communication channels, e.g. text messages, emails, and voice calls, for potential scam indicators.

    Made during the [Hackathon for Technical AI Safety Startups](https://www.apartresearch.com/event/ais-startup-hackathon). See the [full writeup here](https://docs.google.com/document/d/1SCztrhkaBOqpKkgcZsuhX8VfFEKtrqzWrK09s6eIBsg/edit#heading=h.n6byr76t5xwj) and the Github repo [https://github.com/andersthemagi/ai-scam-detection].         
""")