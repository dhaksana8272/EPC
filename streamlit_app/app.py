import streamlit as st
import streamlit as st

st.markdown("""
<style>
/* Login input fields */
input[type="text"], input[type="password"] {
    background-color: rgba(225, 245, 255, 0.6) !important;
    color: black !important;
    border-radius: 8px;
    padding: 10px;
    border: 2px solid #4A6A7A;
}

/* Labels */
label {
    color: #0a2540;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
st.set_page_config(
    page_title="EPC Reasoning Engine",
    layout="wide"
)

# -------- BACKGROUND IMAGE + THEME --------
st.markdown("""
<style>
.stApp {
    background-image: url("https://mcdn.wallpapersafari.com/medium/83/2/mPgjy4.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    
}
.stApp::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-color: rgba(0, 0, 0, 0.25); /* dark overlay */
    z-index: -1;
}

.block-container {
    background-color: rgba(240, 248, 255, 0.40);
    padding: 40px;
}

/* Navbar */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 20px;
    font-weight: bold;
}

.navbar a {
    margin-left: 25px;
    text-decoration: none;
    color: #0b4da2;
    font-size: 18px;
}

/* Section spacing */
.section {
    margin-top: 80px;
    
}
/* Common text color (same as navbar) */
.text-theme {
    color: #0b4da2;
}
         
</style>
""", unsafe_allow_html=True)
# -------- NAVBAR --------
st.markdown("""
<div class="navbar">
    <div style="font-size:22px;color:#083a7a;">EPC Reasoning Engine</div>
    <div>
        <a href="#home">Home</a>
        <a href="#about">About Us</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact Us</a>
    </div>
</div>
""", unsafe_allow_html=True)

# -------- ABOUT + LOGIN SIDE-BY-SIDE --------
st.markdown('<div id="about" class="section">', unsafe_allow_html=True)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("<h2 style='color:#0b4da2;'>About Us</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#0b4da2; margin-bottom:2px;'>EPC Reasoning Engine is an AI-powered platform built to understand,</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#0b4da2; margin-bottom:2px;'>analyze, and reason over Engineering, Procurement, and</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#0b4da2;'>Construction (EPC) documents to provide insights faster.</p>", unsafe_allow_html=True)

with col_right:
    st.markdown("<h2 style='color:#0b4da2;'>Login</h2>", unsafe_allow_html=True)

    st.markdown("<label style='color:#0b4da2;'>Email</label>", unsafe_allow_html=True)
    email = st.text_input("", label_visibility="collapsed")

    st.markdown("<label style='color:#0b4da2;'>Password</label>", unsafe_allow_html=True)
    password = st.text_input("", type="password", label_visibility="collapsed")

    if st.button("Sign In"):
        st.switch_page("pages/page2.py")

    st.markdown(
        "<p style='margin-top:10px; text-align:center; color:#0b4da2;'>"
        "Don’t have an account? "
        "<span style='text-decoration:underline; cursor:pointer;'>Sign up</span>"
        "</p>",
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)