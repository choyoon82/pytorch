import streamlit as st # pip install streamlit
import numpy as np

with st.sidebar.expander('PYTHON'):
    page = st.radio(
        "",
        ["numpy"],
        index=None,
    )

if page == 'numpy':
    nparr = []
    code = st.code('nparr = np.random.randint(2,10,5)')
    if st.button('실행') and not('import' in code): 
        exec(code)
        st.text_area(nparr)


st.text('hello world')
