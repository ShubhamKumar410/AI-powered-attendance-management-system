import streamlit as st

def footer_home():
    st.markdown("""
        <div style="
            margin-top: 2rem;
            display: flex;
            gap: 6px;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
        ">
            <span style="font-weight: bold; color: white;">
                Created with ❤️ by
            </span>
            <span style="
                color: #FFB703;
                font-weight: bold;
                font-size: 16px;
            ">
                Shubham Kumar
            </span>
        </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
        <div style="
            margin-top: 2rem;
            display: flex;
            gap: 6px;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
        ">
            <span style="font-weight: bold; color: black;">
                Created with ❤️ by
            </span>
            <span style="
                color: #0099CC;
                font-weight: bold;
                font-size: 16px;
            ">
                Shubham Kumar
            </span>
        </div>
    """, unsafe_allow_html=True)
