import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                /* Deep navy-to-indigo radial mesh gradient with a subtle dot-grid overlay */
                [data-testid="stAppViewContainer"],
                .stApp {
                    background-color: #0d0f2b !important;
                    background-image:
                        radial-gradient(ellipse 80% 60% at 20% 10%, rgba(88, 101, 242, 0.45) 0%, transparent 65%),
                        radial-gradient(ellipse 60% 50% at 80% 80%, rgba(110, 124, 255, 0.35) 0%, transparent 60%),
                        radial-gradient(ellipse 50% 40% at 55% 45%, rgba(235, 69, 158, 0.15) 0%, transparent 55%),
                        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40'%3E%3Ccircle cx='1' cy='1' r='1' fill='rgba(255,255,255,0.06)'/%3E%3C/svg%3E") !important;
                        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60'%3E%3Cpath d='M 60 0 L 0 0 0 60' fill='none' stroke='rgba(88,101,242,0.06)' stroke-width='1'/%3E%3C/svg%3E") !important
                    background-size: cover, cover, cover, 40px 40px !important;
                    background-attachment: fixed !important;
                }

                /* Card columns — yellow background */
                .stApp div[data-testid="stColumn"]{
                    background-color: #FFD700 !important;
                    padding: 2.5rem !important;
                    border-radius: 3rem !important;
                    box-shadow: 0px 10px 40px rgba(0, 0, 0, 0.35);
                }
        </style>  

                """
            ,unsafe_allow_html=True)


def style_background_dashboard():

    st.markdown("""
        <style>

                /* Soft cool-white gradient with a very faint grid line pattern */
                [data-testid="stAppViewContainer"],
                .stApp {
                    background-color:  #0d0f2b !important;
                    background-image:
                        radial-gradient(ellipse 80% 60% at 20% 10%, rgba(88, 101, 242, 0.45) 0%, transparent 65%),
                        radial-gradient(ellipse 60% 50% at 80% 80%, rgba(110, 124, 255, 0.35) 0%, transparent 60%),
                        radial-gradient(ellipse 50% 40% at 55% 45%, rgba(235, 69, 158, 0.15) 0%, transparent 55%),
                        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40'%3E%3Ccircle cx='1' cy='1' r='1' fill='rgba(255,255,255,0.06)'/%3E%3C/svg%3E") !important;
                        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60'%3E%3Cpath d='M 60 0 L 0 0 0 60' fill='none' stroke='rgba(88,101,242,0.06)' stroke-width='1'/%3E%3C/svg%3E") !important;
                    background-size: cover, 60px 60px !important;
                    background-attachment: fixed !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)



def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}

            /* Dialog / Modal background — consistent with dashboard palette */
            div[data-testid="stDialog"] > div > div {
                background-color: #f0f2ff !important;
                background-image:
                    linear-gradient(160deg, #ffffff 0%, #e8ecff 40%, #dde3ff 100%),
                    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='60' height='60'%3E%3Cpath d='M 60 0 L 0 0 0 60' fill='none' stroke='rgba(88,101,242,0.06)' stroke-width='1'/%3E%3C/svg%3E") !important;
                background-size: cover, 60px 60px !important;
                border-radius: 1.5rem !important;
                border: 1px solid rgba(88, 101, 242, 0.15) !important;
                box-shadow: 0 20px 60px rgba(13, 15, 43, 0.25) !important;
            }

        </style>  

                """
            ,unsafe_allow_html=True)
