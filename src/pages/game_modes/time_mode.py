import streamlit as st
import random
from src.apis import get_valid_word_with_definition
from .game_utils import (
    initialize_game,
    display_hints_sidebar,
    handle_guess_input,
    process_full_guess,
    handle_fill_a_letter,
    handle_hint,
    handle_quit,
    show_time_remaining,
    validate_user_input,
    update_retries
)
from datetime import datetime, timedelta

def play_time_mode():
    st.markdown("""
    ## ⏳ Time Mode!

    Race against the clock—each guess counts in this thrilling challenge! 🚀
    """)

    # Condensed game instructions in bullet points.
    st.markdown("""
    - **🔍 Navigate:** Quick! Click/Tap or `Tab` through inputs.
    - **🔤 Help:** Stuck? 'Fill a Letter' or 'Take a Hint.' But hurry!
    - **⏲️ Watch:** Keep an eye on the timer, it's ticking!
    - **✅ Submit:** Inputs ready? They're checked instantly!
    - **🔄 Continue/Quit:** Time's up? Try again or wave goodbye.
    """, unsafe_allow_html=True)


    length = st.session_state.word_length if 'word_length' in st.session_state else 5
    word_info = get_valid_word_with_definition(length)

     # assuming the function can accept a second parameter to specify timed mode
    initialize_game(word_info, is_timed=True) 

    # Get the current time
    current_time = datetime.now()

    # If the current time is beyond the end time, the game is over.
    if current_time >= st.session_state.end_time:
        st.warning("Time's up!")
        if st.button("Try Again"):
            st.session_state.clear()  # This clears all variables in the session state
            st.session_state.page = 'game_page'
            st.rerun()
        return  # Exit the function here, game over.


    display_hints_sidebar()

    # Handle user input for guessing the word and check if all inputs are filled
    all_filled, user_inputs = handle_guess_input()

    process_full_guess(all_filled)

    # If all inputs are filled, validate them and update the retries left
    if all_filled:
        validate_user_input(user_inputs)
        update_retries(user_inputs)

    col1, col2, col3 = st.columns(3)
    s_col1, s_col2, s_col3 = st.sidebar.columns(3)

    show_time_remaining()

    if s_col2.button("Fill a Letter"):
        handle_fill_a_letter()

    if s_col2.button("Take a Hint"):
        handle_hint(word_info)

    button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns(5)

    if button_col2.button("Play Again"):
        st.session_state.clear()
        st.session_state.page = 'game_page'
        st.rerun()

    if button_col4.button("Quit"):
        handle_quit()

