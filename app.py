import streamlit as st
import google.generativeai as genai

# পেজ সেটআপ
st.set_page_config(page_title="Esy chat", page_icon="🚀")

# আপনার API Key এখানে বসান
genai.configure(api_key="আপনার_API_Key_এখানে_বসান")

# AI নির্দেশনাবলী
instructions = "তুমি Esy chat। তুমি গণিত এবং কোডিংয়ের একজন বিশেষজ্ঞ। ব্যবহারকারীর সাথে বন্ধুসুলভ আচরণ করো।"
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instructions)

st.title("🚀 Esy chat: Math & Coding AI")

# চ্যাট ইনপুট
prompt = st.chat_input("আপনার প্রশ্ন এখানে লিখুন...")

if prompt:
    with st.spinner("Esy chat ভাবছে..."):
        response = model.generate_content(prompt)
        st.chat_message("user").write(prompt)
        st.chat_message("assistant").write(response.text)
