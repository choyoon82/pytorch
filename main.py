import streamlit as st # pip install streamlit
import numpy as np

with st.sidebar.expander('PYTHON'):
    page = st.radio(
        "",
        ["numpy"],
        index=None,
    )

if page == 'numpy':
    code = st.code('''nparr = np.random.randint(2,10,5)
        print(nparr)
        ''')
    if st.button('실행'):
        st.text_area(exec(code))


st.text('hello world')
