import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from src.pages.game_modes.game_utils import initialize_game, display_hints_sidebar, process_full_guess, \
                                            handle_fill_a_letter, handle_quit, update_retries, \
                                            validate_user_input, show_time_remaining, handle_guess_input, handle_hint

class TestGameUtils(unittest.TestCase):

    @patch('src.pages.game_modes.game_utils.st')
    def test_initialize_game(self, mock_st):
        # Set up session_state as a real dictionary
        mock_st.session_state = {}
        
        word_info = {'Word': 'test'}
        initialize_game(word_info)

        # Now st.session_state is a real dict and you can interact with it as expected
        self.assertEqual(mock_st.session_state['word'], 'test')
        self.assertEqual(mock_st.session_state['display_word'], ['_'] * 4)
        self.assertEqual(mock_st.session_state['max_guesses'], 5)
        self.assertEqual(mock_st.session_state['hints_taken'], [])
        self.assertEqual(mock_st.session_state['fill_a_letter_clicks'], 0)
        self.assertEqual(mock_st.session_state['user_guesses'], [""] * 4)

        # Test initialization with a timed game
        mock_st.session_state = {}
        initialize_game(word_info, is_timed=True)
        self.assertIsNotNone(mock_st.session_state.get('start_time'))
        self.assertIsNotNone(mock_st.session_state.get('end_time'))

    @patch('src.pages.game_modes.game_utils.st')
    def test_display_hints_sidebar(self, mock_st):
        mock_st.session_state.hints_taken = []
        display_hints_sidebar()
        mock_st.sidebar.text.assert_called_once_with("No hint taken")

        mock_st.session_state.hints_taken = [{'Part of Speech': 'noun', 'Definition': ['A test definition']}]
        display_hints_sidebar()
        self.assertEqual(mock_st.sidebar.text.call_count, 4)  # This number might need adjustment based on the actual calls

    @patch('src.pages.game_modes.game_utils.st')
    def test_handle_guess_input(self, mock_st):
        # Setup
        mock_st.session_state.word = 'test'
        mock_st.session_state.end_time = datetime.now() + timedelta(minutes=10)
        mock_st.session_state.user_guesses = [""] * 4
        mock_st.columns.return_value = [MagicMock()] * 4

        # Test
        all_filled, user_guesses = handle_guess_input()
        self.assertFalse(all_filled)
        self.assertIsNone(user_guesses)

    @patch('src.pages.game_modes.game_utils.st')
    def test_process_full_guess(self, mock_st):
        mock_st.session_state.word = 'test'
        mock_st.session_state.display_word = ['t', 'e', 's', '_']
        mock_st.session_state.user_guesses = ['t', 'e', 's', 't']
        process_full_guess(True)
        self.assertNotIn('_', mock_st.session_state.display_word)

    @patch('src.pages.game_modes.game_utils.st')
    def test_handle_fill_a_letter(self, mock_st):
        mock_st.session_state.word = 'test'
        mock_st.session_state.display_word = ['_', '_', '_', '_']
        mock_st.session_state.fill_a_letter_clicks = 0
        mock_st.session_state.user_guesses = [""] * 4

        handle_fill_a_letter()
        self.assertEqual(mock_st.session_state.fill_a_letter_clicks, 1)
        self.assertIn('_', mock_st.session_state.display_word)
        self.assertEqual(len([i for i in mock_st.session_state.display_word if i == '_']), 3)

    @patch('src.pages.game_modes.game_utils.st')
    def test_handle_hint(self, mock_st):
        mock_st.session_state.hints_taken = []
        word_info = {'Part of Speech 1': 'noun', 'Definitions 1': ['A test definition']}
        handle_hint(word_info)
        self.assertEqual(len(mock_st.session_state.hints_taken), 1)

    @patch('src.pages.game_modes.game_utils.st')
    def test_handle_quit(self, mock_st):
        mock_st.session_state.word = 'test'
        mock_st.session_state.user_guesses = ['_', '_', '_', '_']
        handle_quit()
        self.assertEqual(''.join(mock_st.session_state.user_guesses), 'test')

    @patch('src.pages.game_modes.game_utils.st')
    def test_show_time_remaining(self, mock_st):
        mock_st.session_state.end_time = datetime.now() + timedelta(seconds=10)
        show_time_remaining()
        self.assertEqual(mock_st.toast.call_count, 1)

    @patch('src.pages.game_modes.game_utils.st')
    def test_validate_user_input(self, mock_st):
        mock_st.session_state.word = 'test'
        validate_user_input(['t', 'e', 's', 't'])
        mock_st.success.assert_called_once()
        mock_st.balloons.assert_called_once()

    @patch('src.pages.game_modes.game_utils.st')
    def test_update_retries(self, mock_st):
        mock_st.session_state.word = 'test'
        mock_st.session_state.max_guesses = 3
        update_retries(['t', 'a', 's', 't'])
        self.assertEqual(mock_st.session_state.max_guesses, 2)
        self.assertEqual(mock_st.toast.call_count, 1)


if __name__ == '__main__':
    unittest.main()
