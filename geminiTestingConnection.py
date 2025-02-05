import google.generativeai as genai
import streamlit as st
import getpass


genai.configure(api_key="AIzaSyAqCMVk7G_EbHiamCzFel1ir2Ryo2IcXYA")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")
print("model connected..")

def generate_response(model_name, user_input):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(user_input)
    return response.text

def main():
    st.title("Google Gemini Generative AI")

    # Select the model
    model_name = st.selectbox(
        "Choose a model:",
        ["gemini-pro", "chat-bison", "text-bison", "code-bison"]
    )

    # User input text box
    user_input = st.text_area("Enter your query:")

    if st.button("Generate Response"):
        if user_input:
            with st.spinner("Generating response..."):
                response = generate_response(model_name, user_input)
                st.success("Response Generated!")
                st.write(response)
        else:
            st.warning("Please enter a query to generate a response.")

if __name__ == "__main__":
    main()
