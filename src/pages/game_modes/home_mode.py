import streamlit as st
from src.pages.game_modes.game_utils import select_word_length

def show_gameplay():
    """
    Display the gameplay mode selection screen with two options: Free Mode and Time Mode.
    Players can choose their preferred mode to start the game.
    """

    # Container holding the main content
    with st.container():

        # Creating columns for layout: images and buttons will be in the first and third columns, respectively
        st.markdown("<h2 style='text-align: center;'>Please Choose Game Mode</h2>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 5, 1])

        with col2:
            st.session_state.word_length = select_word_length()

        col1, col2, col3 = st.columns([6, 1, 6])
        with col1:
            # Display the image for Free Mode. Make sure the image is accessible and the path is correct.

            st.image("src/templates/images/no_time_limit.gif", use_column_width=True, caption="Free Mode: Play without time pressure!")

            _col1, _col2, _col3 = st.columns(3)
            # Button to select Free Mode
            if _col2.button("Free Mode", key='game_mode_free_mode', help="Click to play without time constraints."):
                # Set the session state to navigate to the Free Mode page
                st.session_state.page = 'free_style_mode'
                # Rerun the script from the top to navigate to the selected mode
                st.rerun()

        with col3:
            # Display the image for Time Mode. Ensure the image path is correct.
            st.image("src/templates/images/time_limit.gif", use_column_width=True, caption="Time Mode: Race against the clock!")

            _col1, _col2, _col3 = st.columns(3)
            # Button to select Time Mode
            if _col2.button("Time Mode", key='game_mode_time_mode', help="Click to play with a time limit."):
                # Set the session state to navigate to the Time Mode page
                st.session_state.page = 'time_mode'
                # Rerun the script from the top to navigate to the selected mode
                st.rerun()
