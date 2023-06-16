
# import libraries
import streamlit as st

# layout
st.set_page_config(layout="wide")

st.markdown(""" 
<style>

    /* above the header */
    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }

    /* central part */
    [data-testid="stAppViewContainer"] {
    background-color: white;
    }

    /* sidebar menu */
    [data-testid="stSidebarNav"] {
    background-color: #044389;
    }

    /* sidebar*/
    [data-testid="stSidebar"] {
    background-color: #044389;
    }

    /* Sidebar links*/
    .css-17lntkn {
    color:white;
    font-size: 20px;
    }
    .css-17lntkn:hover {
    color:#FF4B4B !important;
    font-size: 20px;
    }
    .css-pkbazv {
    color:white;
    font-size: 20px;
    }
    .css-pkbazv:hover {
    color:#FF4B4B !important;
    font-size: 20px;
    }
    
    /* Titles*/
    .css-10trblm {
    color:#044389;
    }

    /* Streamlit link*/
    .css-1vbd788 {
    color:#044389 !important;
    text-decoration-line:underline;
    }
    .css-1vbd788:hover {
    color:#FF4B4B !important;
    }

    /* Links*/
    a {
    color:#044389 !important;
    }
    a:hover {
    color:#FF4B4B !important;
    }

</style>       
""",unsafe_allow_html=True)

# title
st.write("<h1>Getaround analysis - Prediction</h1>",unsafe_allow_html=True)

# subtitle
st.write("<p style='font-size:20px;'>API to predict optimal prices for car \
    owners</p>",unsafe_allow_html=True)
st.markdown("[Please follow this link](https://cnmgetaroundprediction.herokuapp.com/docs)")