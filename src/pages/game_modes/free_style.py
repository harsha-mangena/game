import streamlit as st
from src.apis import get_valid_word_with_definition
from .game_utils import (
    initialize_game,
    display_hints_sidebar,
    handle_guess_input,
    process_full_guess,
    handle_fill_a_letter,
    handle_hint,
    handle_quit,
    validate_user_input,
    update_retries
)

def play_free_style():

    st.markdown("""
    ## Free Style Mode!

    Dive into the fun—no time limits, just pure word guessing enjoyment! 🌟
    """)

    # Condensed game instructions in bullet points.
    st.markdown("""
    - **🔍 Navigate:** Click/Tap or `Tab` through inputs.
    - **🔤 Help:** Unsure? 'Fill a Letter' or 'Take a Hint.'
    - **✅ Submit:** Full inputs? Auto-validation kicks in!
    - **🔄 Continue/Quit:** Done? Play more or exit.
    """, unsafe_allow_html=True)

    # Get the desired word length from the session state
    length = st.session_state.word_length
    
    # Retrieve a word with the specified length and its accompanying information
    word_info = get_valid_word_with_definition(length)
    
    # Initialize the game state with the chosen word
    initialize_game(word_info)

    # Display the hints in the sidebar
    display_hints_sidebar()

    # Handle user input for guessing the word and check if all inputs are filled
    all_filled, user_inputs = handle_guess_input()

    # If all inputs are filled, validate them and update the retries left
    if all_filled:
        validate_user_input(user_inputs)
        update_retries(user_inputs)

    # Define layout for the main buttons
    col1, col2, col3 = st.columns(3)
    s_col1, s_col2, s_col3 = st.sidebar.columns(3)
    
    # Sidebar interaction for filling a letter or taking a hint
    if s_col2.button("Fill a Letter"):
        handle_fill_a_letter()

    if s_col2.button("Take a Hint"):
        handle_hint(word_info)

    # Layout for bottom control buttons
    button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)

    # Buttons for playing again and quitting the game
    if button_col2.button("Play Again"):
        st.session_state.clear()
        st.session_state.page = 'game_page'
        st.rerun()

    if button_col4.button("Quit"):
        handle_quit()

# End of the play_free_style function
