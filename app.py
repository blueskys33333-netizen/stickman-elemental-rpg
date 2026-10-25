import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="졸라맨 원소 RPG - 마을 & 퀘스트",
    page_icon="🍺",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { background-color: #080b12; }
    .stApp { background-color: #080b12; color: #ffffff; }
    iframe { border-radius: 12px; border: 1px solid #00e5ff !important; }
</style>
""", unsafe_allow_html=True)

st.title("🍺 졸라맨 원소 RPG: 주점과 슬라임 성지")
st.caption("마을에서 주점 퀘스트를 수락하고 슬라임 성지로 떠나세요!")

with st.sidebar:
    st.header("🎮 마을 & 던전 조작법")
    st.markdown("---")
    st.markdown("""
    - **이동:** `←` / `→` (좌우 방향키)
    - **점프:** `Space`
    - **건물 / 포탈 상호작용:** `↑` (상단 방향키)
    - **주점 퀘스트 열기:** 주점 앞에서 `Q` 키
    - **대장간 / 상점:** `E` / `R` 키
    - **기본 공격 (검격):** `Z`
    - **원소 스킬:** `X`
    """)
    st.markdown("---")
    st.info("💡 Tip: 게임 캔버스를 한 번 클릭해야 키보드 입력이 정상 작동합니다.")

try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=620, width=1000, scrolling=False)
except FileNotFoundError:
    st.error("⚠️ 'index.html' 파일을 찾을 수 없습니다. app.py와 같은 디렉토리에 위치시켜 주세요.")
