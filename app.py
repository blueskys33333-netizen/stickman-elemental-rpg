import streamlit as st
import streamlit.components.v1 as components

# 페이지 기본 설정
st.set_page_config(
    page_title="졸라맨 원소 RPG",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 커스텀 CSS 스타일링
st.markdown("""
<style>
    .main { background-color: #0b0e14; }
    .stApp { background-color: #0b0e14; color: #ffffff; }
    .css-1d3b13b { background-color: #121824; }
    .stButton>button {
        background-color: #1a2332;
        color: #00e5ff;
        border: 1px solid #00e5ff;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00e5ff;
        color: #000000;
    }
</style>
""", unsafe_allow_allow_html=True)

# 메인 타이틀
st.title("⚔️ 졸라맨 원소 RPG (Stickman Elemental RPG)")
st.caption("GitHub & Streamlit Community Cloud 기반 2D 횡스크롤 판타지 웹 게임")

# 사이드바: 게임 가이드 및 조작법
with st.sidebar:
    st.header("🎮 게임 가이드")
    st.markdown("---")
    st.subheader("⌨️ 조작법")
    st.markdown("""
    - **이동:** `←` / `→` (좌우 방향키)
    - **점프:** `Space`
    - **포탈 이동:** `↑` (상단 방향키)
    - **기본 공격 (검격):** `Z`
    - **원소 스킬:** `X`
    - **속성 즉시 전환:** `1` (불), `2` (물), `3` (흙), `4` (공기)
    """)
    st.markdown("---")
    st.subheader("🔥 4대 원소 고유 특성")
    st.markdown("""
    - **🔥 불 (Fire):** 폭발형 광역 피해 및 높은 스킬 데미지
    - **💧 물 (Water):** 빙결 제어 및 적 이동 속도 둔화
    - **🪨 흙 (Earth):** 묵직한 중량 공격 및 높은 방어 감쇄
    - **💨 공기 (Air):** 빠른 연타 속도 및 날카로운 연속 참격
    """)

# 게임 캔버스 렌더링 영역
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # Streamlit 컴포넌트를 통해 HTML 게임 화면 임베딩
    components.html(html_content, height=600, width=1000, scrolling=False)
except FileNotFoundError:
    st.error("⚠️ 'index.html' 파일을 찾을 수 없습니다. app.py와 같은 폴더에 위치시켜 주세요.")
