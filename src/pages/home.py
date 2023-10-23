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
                    **Hangman** is a classic paper and pencil guessing game for two or more players. One player thinks of a word, 
                    and the others try to guess it by suggesting letters within a certain number of guesses. In our digital version, 
                    you'll play against the computer, and you'll have some extra help at your disposal!

                    Here's how it works:

                    - **Starting the Game**: Click "Start" to begin. You'll be given a word to guess, represented by a row of dashes, 
                    indicating each letter of the word.
                    - **Making a Guess**: Suggest a letter you believe may be part of the word. If correct, the letter will appear in its 
                    correct position(s) in the word. If incorrect, part of the hangman's gallows will be drawn.
                    - **Winning and Losing**: The game ends when you either guess the word correctly or the hangman's body is fully drawn.

                    **Game Modes**:
                    - **Free Mode**: Play at your own pace. There's no time limit, so take your time thinking of your next letter.
                    - **Time Mode**: Race against the clock! You'll have a set amount of time to guess the word before the hangman is complete.

                    **Need Some Help?**:
                    - **Take a Hint**: Stuck on a word? Click the "Take a Hint" button for a nudge in the right direction. But use it wisely—you only have a few hints!
                    - **Fill a Letter**: Need a little more help? Use the "Fill a Letter" option to reveal one of the letters in the word. 
                    But remember, you can only use this help a limited number of times.

                    Ready to test your word-guessing skills? Let's play Hangman!
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
