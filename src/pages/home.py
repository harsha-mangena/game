import streamlit as st

def show_homepage():
    """
    Render the homepage of the Hangman game with a start button.
    This page shows a welcoming image and a button to navigate to the game page.
    """

    # Main container to center content
    with st.container():

        # Creating columns to adjust the layout. The main content is in the middle column.
        col1, col2, col3 = st.columns([1, 6, 1])

        with col2:
            # Display the hangman image stored locally. Adjust the path if needed.
            # Ensure the image is in high resolution and the path is accessible.
            st.image("src/templates/images/hangman.png", use_column_width=True)  # ensure you replace "path_to_your_image" with the actual path

            # Create space between image and button
            st.empty()

            # Instructions expander
            with st.expander("How to Play 👇", expanded=True):
                st.write(
                    """
                    **Hangman** is a paper and pencil guessing game for two or more players. One player thinks of a word, 
                    and the others try to guess it by suggesting letters within a certain number of guesses.
                    - Click "Start" to begin the game.
                    - You will be given a word to guess, represented by a row of dashes, representing each letter of the word.
                    - You guess by suggesting a letter, which you believe may be a part of the word.
                    - If the word contains the suggested letter, the computer fills in the blanks with that letter in the right position.
                    - If the word does not contain the suggested letter, the computer draws one element of a hangman’s gallows.
                    - The game is over either when the player guesses the complete word, or the hangman's body is fully drawn.
                    Good luck!
                    """
                )

            # Row of columns, mainly using the middle one for the 'Start' button
            _col1, _col2, _col3 = st.columns(3)

            # Start button to begin the game. When clicked, it changes the session state to the game page.
            if _col2.button("🚀 Start Game", key='from_home_lets_start', help="Click to start the game"):
                # Set the session state to indicate the current page the user navigates to.
                st.session_state.page = "game_page"
                # Rerun the script from the top to reflect the session state changes.
                st.experimental_rerun()

# Make sure to replace "path_to_your_image" with the actual path where your image is stored.
