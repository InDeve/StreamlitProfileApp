import streamlit as st

# ''' Page setup '''
profile = st.Page(
    page="pages/profile.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

city_classificaiton_page = st.Page(
    page="pages/city_model.py",
    title="City Classification",
    icon=":material/location_city:",
)

echo_bot_page = st.Page(
    page="pages/chatbot.py",
    title="Echo Bot",
    icon=":material/smart_toy:",
)

anime_recommend_page = st.Page(
    page="pages/anime_recommend.py",
    title="Anime Recommendation",
    icon=":material/comic_bubble:",
)

toxic_check_page = st.Page(
    page="pages/toxicity_model.py",
    title="Toxic Comment Check",
    icon=":material/fact_check:"
)

# ''' NAVIGATION SETUP (No sections) '''
# pg = st.navigation(pages=[profile, project_1_page, project_2_page])

# ''' Navigation with Sections '''
pg = st.navigation(
    {
        "Profile": [profile],
        "Projects": [city_classificaiton_page, anime_recommend_page, toxic_check_page, echo_bot_page],
    }
)

# ''' SHARED ON ALL pages '''
st.logo("assets/heart.png")
st.sidebar.text("Made by Test Dev | Base dashboard from Sven @CodingIsFun")

# ''' RUN NAVIGATION '''
pg.run()