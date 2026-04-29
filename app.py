import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("GlowUp AI Content Generator")

business_type = st.text_input("Business Type")
content_type = st.selectbox("Content Type", ["Instagram Caption", "Product Description", "TikTok Script"])
tone = st.selectbox("Tone", ["Professional", "Funny", "Luxury", "Casual"])

if st.button("Generate"):
    prompt = f"""
    Create a {tone} {content_type} for a {business_type}.
    Make it engaging and ready to post.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)
    