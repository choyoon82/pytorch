import streamlit as st # pip install streamlit
import numpy as np


def show_numpy():
    pass
        
    code = st.code('''
        nparr = np.random.randint(2,10,5)
        print(nparr)
        ''')
    if st.button('실행'):
        pass
        st.text_area(eval(code))

with st.sidebar.expander('PYTHON'):
    page = st.radio(
        "",
        ["numpy"],
        index=None,
    )
    if page == 'numpy':
        show_numpy()



st.text('hello world')
