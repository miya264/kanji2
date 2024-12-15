import streamlit as st

st.title("🎉 飲み会日程調整アプリ 🍻")

st.markdown(f"<h2 style='color: red;'>幹事の方はこちらから！ </h2>", unsafe_allow_html=True)
st.button("幹事ページ")

if st.button("幹事ページ"):
    # URLに飛ぶためのリンクを生成
    st.markdown(
        """
        <a href="https://kanji2-ltiusfvke8mapptquxd8zef.streamlit.app/" target="_blank">
            <button style="background-color:blue; color:white; padding:10px; border:none; cursor:pointer;">
                Go to Google
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

st.markdown(f"<h2 style='color: blue;'>参加者の方はこちらから！ </h2>", unsafe_allow_html=True)
st.button("参加者ページ")
if st.button("参加者ページ"):
    # URLに飛ぶためのリンクを生成
    st.markdown(
        """
        <a href="https://kanji2-qbwo25tjdbadjhwxla3ns3.streamlit.app/" target="_blank">
            <button style="background-color:blue; color:white; padding:10px; border:none; cursor:pointer;">
                Go to Google
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
