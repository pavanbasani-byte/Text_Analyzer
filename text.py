import streamlit as st
import re

def main():
    st.set_page_config(page_title="Text Analyzer", page_icon="⚗️", layout="centered")
    st.markdown("""
        <style>
            .main {background-color: #ebecda}
            .stTextArea, .stTextInput {border-radius: 10px}
            .stButton>button {background-color: blue; color: white; border-radius: 10px; padding: 10px}
        </style>
        """, unsafe_allow_html=True)
    
    st.title("Text Analyzer in Python")
    st.write("Analyze your text quickly and efficiently.")
    
    paragraph = st.text_area("✍️ Enter your text here:", "", height=150)
    
    if paragraph:
        st.markdown("---")
        st.subheader("📌 Analysis Result")
        
        words = paragraph.split()
        word_count = len(words)
        char_count = len(paragraph)
        
        col1, col2 = st.columns(2)
        col1.metric("🖹 Total Words", word_count)
        col2.metric("🖺 Total Characters", char_count)
        
        # Search and replace filter
        st.subheader("🔎 Search and Replace")
        search_word = st.text_input("Enter a word to search:")
        replace_word = st.text_input("Enter a word to replace with:")
        
        if search_word and replace_word:
            modified_paragraph = re.sub(rf'\b{re.escape(search_word)}\b', replace_word, paragraph)
            st.success("Modified text:")
            st.info(modified_paragraph)
        
        # Uppercase and lowercase feature
        st.subheader("⭐ Uppercase and Lowercase Feature")
        st.text_area("UPPERCASE:", paragraph.upper(), height=150)
        st.text_area("LOWERCASE:", paragraph.lower(), height=150)
        
        has_python = "python" in paragraph.lower()
        st.write(f"✔️ Contains 'python': {has_python}")
        
        # Average word length
        average_word_length = char_count / word_count if word_count else 0
        st.write(f"📏 Average word length: {average_word_length:.2f}")
    
    else:
        st.warning("⚠️ Please enter a paragraph for analysis.")

if __name__ == "__main__":
    main()
