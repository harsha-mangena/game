import streamlit as st
from src.utils import initialize_firebase_object
import bcrypt

def login_user():

    # User inputs
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
    
    # Centered container for the "Login" button
        button_container = st.container()
    
        with button_container:
            col1, col2, col3 = st.columns(3)

            # Center the "Login" button
            if col2.button("Login", key='login_button', use_container_width=True):
                try:
                # Retrieve user from Firestore
                    db = initialize_firebase_object()
                    users_ref = db.collection('users')
                    
                # Query Firestore for the user
                    query = users_ref.where('username', '==', username).stream()
                    user_data = next(iter(query), None)
                    
                # Check if user exists and if the password is correct
                    if user_data is None:
                        raise ValueError("Invalid username or password")
                    
                    hashed_password = user_data.to_dict().get('password')
                    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                        raise ValueError("Invalid username or password")
                    
                    st.success("Login successful!")

                    st.session_state.page = 'game_page'
                    st.rerun()

                
                except ValueError as e:
                    st.error(str(e))