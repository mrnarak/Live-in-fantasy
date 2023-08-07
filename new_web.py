import streamlit as st
from streamlit_option_menu import option_menu


st.markdown("<h1 style='text-align: center;'>LIVE IN FANTASY</h1>", unsafe_allow_html=True)
    # st.markdown("<h1 style='text-align: center;'>Centered Title</h1>", unsafe_allow_html=True)

st.write("\n")

selected = option_menu(
    menu_title=None,
    options=["Home", "Projects", "Contact"],
    icons=["house", "brush", "envelope"],
    default_index=0,
    orientation="horizontal"
)

if selected == "Home":
    st.write(f"Home")
if selected == "Projects":
    st.write(f"Project")
if selected == "Contact":

    # # Use Markdown to apply custom CSS to the container
    # container_style = """
    #     <style>
    #         .custom-container {
    #             background-color: lightgreen;
    #             padding: 20px;
    #             border: 1px solid #ccc;
    #             border-radius: 5px;
    #         }
    #     </style>
    # """

    # # Apply the custom CSS to the container using Markdown
    # st.markdown(container_style, unsafe_allow_html=True)

    with st.container():
        st.header("")
        st.write("")

    st.markdown("<h2 style='text-align: center;'>CONTACT</h2>", unsafe_allow_html=True)

    with st.container():
        st.header("")
        st.write("")
        
        # Create a link in the form of clickable text
    def create_link(text, link):
        return f'<a href="{link}" target="_blank">{text}</a>'

    # Create a clickable link
    link_text = create_link("TWITTER", "https://twitter.com/ZarakMr")
    link_text2 = create_link("PIXIV", "https://www.pixiv.net/en/users/64696661")
    link_text3 = create_link("EMAIL", "https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcSPFqslNmKmdjPCRTHfDlNGRqBTkKrsbZsNWGLvVRRXnfKQLMvmJSpkRjQnVrrcbGhktSrxM")
    

    custom_font = "font-family: 'Roboto', sans-serif; font-weight: bold;"
    all_links = f'<span style="{custom_font}">{link_text} <span style="margin: 0 20px;">|</span> {link_text2} <span style="margin: 0 20px;">|</span> {link_text3}</span>'


    # all_links = f"{link_text} <span style='margin: 0 20px;'>|</span> {link_text2} <span style='margin: 0 20px;'>|</span> {link_text3}"
    # all_links = f"{link_text} | {link_text2} | {link_text3}"

    centered_links = f'<div style="display: flex; justify-content: center;">{all_links}</div>'

    # Render the centered links using Markdown
    st.markdown(centered_links, unsafe_allow_html=True)