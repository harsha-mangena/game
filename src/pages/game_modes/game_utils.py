# game_utils.py
import streamlit as st
from datetime import datetime, timedelta
import time
import string
import secrets

col1, col2, col3 = st.columns(3)

# Constants
MIN_LENGTH = 3
MAX_LENGTH = 8
MAX_RETRIES = 6
MAX_FILL_A_LETTER_CLICKS = 2
GAME_TIME_MINUTES = 15

def select_word_length():
    return st.slider('Select Word Length', min_value=MIN_LENGTH, max_value=MAX_LENGTH, value=MIN_LENGTH)

def initialize_game(word_info, is_timed=False):
    if is_timed:
        if 'start_time' not in st.session_state:
            st.session_state.start_time = datetime.now()
            st.session_state.end_time = st.session_state.start_time + timedelta(minutes=15)  # 15 minutes from now
    
    if 'word' not in st.session_state:
        st.session_state.word = word_info['Word'].lower()
        st.session_state.display_word = ["_"] * len(st.session_state.word)
        st.session_state.max_guesses = 6
        st.session_state.hints_taken = []
        st.session_state.fill_a_letter_clicks = 0

    if 'user_guesses' not in st.session_state:
        st.session_state.user_guesses = [""] * len(st.session_state.word)

    if 'guesses' not in st.session_state:
        st.session_state.guesses = []

def display_hints_sidebar():
    st.sidebar.title("Hints")
    if st.session_state.hints_taken:
        for i, hint in enumerate(st.session_state.hints_taken):
            st.sidebar.text(f"Hint {i+1}:")
            st.sidebar.text(f"Type: {hint['Part of Speech']}\n---")
            for def_index, definition in enumerate(hint['Definition']):
                wrapped_def = "\n".join([definition[j:j+50] for j in range(0, len(definition), 50)])
                st.sidebar.text(f"Definition {def_index + 1}:\n{wrapped_def}\n---")
    else:
        st.sidebar.text("No hint taken")

def handle_guess_input(is_timed=False):
    current_time = datetime.now()
    err_msg = None 

    # Check if the game time is over or if the max guesses have been exhausted
    if not is_timed:
        input_disabled = st.session_state.max_guesses <= 0
        err_msg = "You are out of tries. Please start the game again."
    
    else:
        input_disabled = current_time >= st.session_state.end_time or st.session_state.max_guesses <= 0
        err_msg = "Time's up! You can't enter more inputs."

    # If the input is disabled due to the time being up, show a message
    if input_disabled:
        st.warning(err_msg)

    cols = st.columns(len(st.session_state.word))
    user_guesses = []
    all_filled = True

    for i, _ in enumerate(st.session_state.word):
        guess = cols[i].text_input("", value=st.session_state.user_guesses[i], key=f"letter_{i}", max_chars=1, disabled=input_disabled)
        user_guesses.append(guess.lower())
        if guess == "":
            all_filled = False

    # Display letter buttons
    st.write("")
    st.write("")
    cols = st.columns(7)

    for i, letter in enumerate(string.ascii_lowercase):
        with cols[i % 7]:
        # Check if the letter is in the target word
            if letter in st.session_state.word:
                indices = [i for i, main_letter in enumerate(st.session_state.word) if main_letter not in st.session_state.display_word]
                if indices:
                    print(st.session_state.guesses)
                    # If the letter is clicked, fill it in the input box
                    if st.button(letter, key=f"button_{letter}", disabled=(input_disabled or (letter in st.session_state.guesses))):
                        st.session_state.guesses.append(letter)
                        for idx, ltr in enumerate(st.session_state.word):
                            if ltr == letter:
                                st.session_state.user_guesses[idx] = letter
                        st.rerun()
            else:
                # If the letter is not in the word, provide feedback to the user only when clicked
                if st.button(letter, key=f"button_{letter}", disabled=(input_disabled or (letter in st.session_state.guesses))):
                    st.session_state.guesses.append(letter)
                    if st.session_state.max_guesses > 0 and not input_disabled:
                        st.toast(f"{letter} is not a valid letter!")
                        # Decrease the number of retries left
                        update_retries(st.session_state.user_guesses)

    st.session_state.user_guesses = user_guesses

    if all_filled:
        return all_filled, user_guesses

    return all_filled, None


def process_full_guess(all_filled):
    if all_filled:
        st.session_state.display_word = [letter if letter in st.session_state.user_guesses else "_" for letter in st.session_state.word]
        if "_" not in st.session_state.display_word:
            st.success("Congratulations! You've guessed the word!")
            
def handle_fill_a_letter():
    if st.session_state.fill_a_letter_clicks < 2:
        indices = [i for i, letter in enumerate(st.session_state.word) if letter not in st.session_state.display_word]
        if indices:
            chosen_index = secrets.choice(indices)
            chosen_letter = st.session_state.word[chosen_index]
            for i, letter in enumerate(st.session_state.word):
                if letter == chosen_letter:
                    st.session_state.display_word[i] = chosen_letter
                    st.session_state.user_guesses[i] = chosen_letter
            st.session_state.fill_a_letter_clicks += 1
            st.rerun()
    else:
        st.toast("You are out of 'Fill a Letter' clicks!")

def handle_hint(word_info):
    hint_num = len(st.session_state.hints_taken) + 1
    part_of_speech_key = f"Part of Speech {hint_num}"
    definition_key = f"Definitions {hint_num}"
    
    if part_of_speech_key in word_info and definition_key in word_info:
        hint = {
            "Part of Speech": word_info[part_of_speech_key],
            "Definition": word_info[definition_key]
        }
        st.session_state.hints_taken.append(hint)
        st.rerun()
    else:
        st.toast("No more hints available")


def handle_quit():
    # Fill in the correct word
    # st.session_state.user_guesses = list(st.session_state.word)
    
    # Optional: You might want to display a message or otherwise indicate that the game is over.
    st.info("Game over. \n The word was: " + st.session_state.word)

    time.sleep(2)
    st.session_state.clear()
    st.session_state.page = 'home'

    # Rerun to update the UI with the revealed word
    st.rerun()

def show_time_remaining():
    current_time = datetime.now()
    time_left = st.session_state.end_time - current_time

    # If less than 10 seconds are left, display a warning toast.
    if 0 < time_left.total_seconds() <= 10:
        st.toast(f"Hurry up! Only {int(time_left.total_seconds())} seconds left!")
    elif time_left.total_seconds() > 0:
        st.toast(f"Time remaining: {time_left.seconds // 60} minutes {time_left.seconds % 60} seconds")
    else:
        st.toast("Time's up!", duration=3)

def validate_user_input(user_inputs):
    if user_inputs is not None:
        # Join the user inputs to form a string and compare it with the actual word.
        user_word = ''.join(user_inputs)
        if user_word == st.session_state.word:
            st.success("Congratulations! You've guessed the word correctly!")
            st.balloons()
            # You can add any code here to handle the correct guess (e.g., redirecting, scoring, etc.)
        else:
            st.error("That's not correct! Please try again.")
            # Any other feedback or handling for incorrect guesses.

MAX_RETRIES = 5

def update_retries(user_input):
    # Assuming st.session_state.word is the correct word the user should guess
    correct_word = st.session_state.word
    user_word = ''.join(user_input)

    if user_word != correct_word:
        # Decrease the retry count if the guess is incorrect
        st.session_state.max_guesses -= 1
        if st.session_state.max_guesses >= 1:
            st.toast(f"Incorrect! You have {st.session_state.max_guesses} retries left.")
        else:
            st.toast("You've run out of retries! Better luck next time.")
            st.snow()

