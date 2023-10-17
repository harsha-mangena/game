# main_app.py
import streamlit as st
from src.pages import home, login, registration
from src.pages.game_modes import home_mode, free_style, time_mode

def __get_page_redirect(page) -> callable:
    PAGE_FUNCTION = {
        "home": home.show_homepage,
        "login": login.login_user,
        "register": registration.register_user,
        "game_page" : home_mode.show_gameplay,
        "free_style_mode" : free_style.play_free_style,
        "time_mode": time_mode.play_time_mode
    }
    return PAGE_FUNCTION.get(page)

def set_and_render_page(page: str) -> None:
    st.session_state.page = page
    page_function = __get_page_redirect(page)
    page_function()

if __name__ == "__main__":
    if "page" not in st.session_state:
        st.session_state.page = "home"
    
    set_and_render_page(st.session_state.page)
