import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Esy chat", page_icon="🚀")

# আপনার API Key এখানে দিন
genai.configure(api_key="AIzaSyAwxvoQynWdAcBIFKP1hOcOP_GCTgFGqO0")

instructions = "তুমি Esy chat। গণিত এবং কোডিং বিশেষজ্ঞ। খুব দ্রুত এবং টাইপ করার মতো করে উত্তর দাও।"
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction=instructions)

st.title("🚀 Esy chat: Math & Coding AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("আপনার প্রশ্ন এখানে লিখুন...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # 'stream=True' করার কারণে ৫ সেকেন্ডের আগেই উত্তর আসা শুরু হবে
        result = model.generate_content(prompt, stream=True)
        
        for chunk in result:
            full_response += chunk.text
            response_placeholder.markdown(full_response + "▌")
        
        response_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})
