from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="M&M 리뷰 스튜디오",
    page_icon="◌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent
BASE_CSS = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")

if "monochrome" not in st.session_state:
    st.session_state.monochrome = False

if st.session_state.monochrome:
    theme_vars = """
    :root {
      --app-bg: #21232E;
      --ink: #F4F5F8;
      --muted: #A7ABBA;
      --accent: #105BFF;
      --accent-soft: #FE8500;
      --glass: rgba(255,255,255,.065);
      --line: rgba(255,255,255,.13);
      --glass-shadow: 0 24px 70px rgba(0,0,0,.24);
      --toggle-bg: rgba(16,91,255,.22);
      --toggle-text: #F4F5F8;
      --app-glow:
        radial-gradient(ellipse at 78% 4%, rgba(16,91,255,.20), transparent 34%),
        radial-gradient(ellipse at 8% 72%, rgba(254,133,0,.055), transparent 28%);
    }
    """
else:
    theme_vars = """
    :root {
      --app-bg: #E9E5D6;
      --ink: #222526;
      --muted: #737A7B;
      --accent: #2589D8;
      --accent-soft: #FE6574;
      --glass: rgba(255,255,255,.42);
      --line: rgba(34,37,38,.10);
      --glass-shadow: 0 22px 62px rgba(53,58,54,.08);
      --toggle-bg: #222526;
      --toggle-text: #E9E5D6;
      --app-glow:
        radial-gradient(ellipse at 78% 0%, rgba(37,137,216,.13), transparent 35%),
        radial-gradient(ellipse at 8% 72%, rgba(254,101,116,.08), transparent 30%);
    }
    """

st.html(f"<style>{BASE_CSS}\n{theme_vars}</style>")

# Streamlit의 기본 메뉴는 숨기고, 아래에서 만든 한국어 내비게이션을 사용합니다.
home_page = st.Page("views/home.py", title="개요", url_path="overview", default=True)
cases_page = st.Page("views/case_library.py", title="사례 아카이브", url_path="cases")
review_page = st.Page("views/case_review.py", title="리뷰 룸", url_path="review")
quiz_page = st.Page("views/learning_check.py", title="학습 점검", url_path="knowledge-check")
current_page = st.navigation(
    [home_page, cases_page, review_page, quiz_page],
    position="hidden",
)

nav = st.columns([2.0, 0.85, 1.05, 1.0, 0.95, 1.3], vertical_alignment="center")
with nav[0]:
    st.markdown(
        '<div class="top-brand">M&amp;M <span>리뷰 스튜디오</span></div>',
        unsafe_allow_html=True,
    )
with nav[1]:
    st.page_link(home_page, label="개요")
with nav[2]:
    st.page_link(cases_page, label="사례 아카이브")
with nav[3]:
    st.page_link(review_page, label="리뷰 룸")
with nav[4]:
    st.page_link(quiz_page, label="학습 점검")
with nav[5]:
    toggle_label = "MONOCHROME · ON" if st.session_state.monochrome else "MONOCHROME · OFF"
    if st.button(toggle_label, key="theme_toggle", use_container_width=True, type="secondary"):
        st.session_state.monochrome = not st.session_state.monochrome
        st.rerun()

st.markdown('<div class="nav-rule"></div>', unsafe_allow_html=True)
current_page.run()
