import streamlit as st

st.title("🎉 飲み会日程調整アプリ 🍻")

# 幹事ページセクション
st.markdown(f"<h2 style='color: red;'>幹事の方はこちらから！ </h2>", unsafe_allow_html=True)
kanji_button = st.button("幹事ページ")  # ボタンにユニークな変数を割り当てる

if kanji_button:  # ボタンが押された場合
    st.markdown(
        """
        <a href="https://kanji2-ltiusfvke8mapptquxd8zef.streamlit.app/" target="_blank">
            <button style="background-color:blue; color:white; padding:10px; border:none; cursor:pointer;">
                Go to Kanji Page
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

# 参加者ページセクション
st.markdown(f"<h2 style='color: blue;'>参加者の方はこちらから！ </h2>", unsafe_allow_html=True)
participant_button = st.button("参加者ページ")  # ボタンにユニークな変数を割り当てる

if participant_button:  # ボタンが押された場合
    st.markdown(
        """
        <a href="https://kanji2-qbwo25tjdbadjhwxla3ns3.streamlit.app/" target="_blank">
            <button style="background-color:blue; color:white; padding:10px; border:none; cursor:pointer;">
                Go to Participant Page
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
