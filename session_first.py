import streamlit as st
import time
import random
import session_two

st.header('st.session_state 세션 테스트')
def main():
    if 'user_list' not in st.session_state:
        st.session_state.user_list = []










