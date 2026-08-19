import streamlit as st

def order():
    st.write('-------------- session_two.py문서  order() --------------')
    if 'user_list'  in st.session_state:
        st.write("test")
    else:
        st.write('세션목록에 없습니다')
