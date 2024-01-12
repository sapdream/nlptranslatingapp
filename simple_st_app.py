import streamlit as st

st.title("Calculator App")

input_1 = st.number_input("Input 1", min_value=None, max_value=None)
input_2 = st.number_input("Input 2", min_value=None, max_value=None)

output_str = str(input_1 + input_2)

st.markdown("Output: `"+output_str+"`")
