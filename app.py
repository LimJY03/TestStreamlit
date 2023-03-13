import streamlit as st

st.title('My First Streamlit App')
st.write('A stremalit app tested and deployed from GitHub Codespace')
st.write()
st.write('Sample Chart')
dataset = {
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 9]
}

st.line_chart(data=dataset, x='x', y='y')