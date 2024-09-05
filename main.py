import streamlit as st


def main():
    st.title("Quaver Multimodal Chat App")
    # Define Chat Container
    chat_container = st.container()

    # User Input
    user_input = st.text_input("Type your message here", key="user_input")
    send_button = st.button("Send", key="send_button")

    if send_button:
        llm_response = "This is a response from the LLM model"

    with chat_container:
        st.chat_message("user").write(user_input)
        st.chat_message("ai").write("This is Quaver's Answer")

if __name__ == "__main__":
    main()