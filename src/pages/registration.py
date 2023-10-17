import streamlit as st
import bcrypt
import firebase_admin
from firebase_admin import credentials, firestore

from src.models.user import User
from src.utils import initialize_firebase_object

def register_user():

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title("User Registration")
    
        # User inputs
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        retyped_password = st.text_input("Retype Password", type="password")
    
        # Centered container for the "Register" button
        button_container = st.container()
    
        with button_container:
            col1, col2, col3 = st.columns(3)

            # Center the "Register" button
            with col2:
                if st.button("Register", key='register_button', use_container_width=True):
                    try:
                        # Validation
                        User.validate(username, password, retyped_password)

                        _db = initialize_firebase_object()
                        users_ref = _db.collection('users')
                    
                        # Check if username is already taken
                        existing_users = users_ref.where('username', '==', username).stream()
                        if any(existing_users):
                            raise ValueError("Username is already taken")
                    
                        # Hashing the password
                        salt = bcrypt.gensalt()
                        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

                        # User creation
                        users_ref.add({
                            'username': username,
                            'password': hashed_password.decode('utf-8'),
                        })
                
                        st.success("User registered successfully!")

                    except ValueError as e:
                        st.error(str(e))