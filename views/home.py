import streamlit as st

from components.hero import render_hero
from utils.case_loader import load_cases


render_hero()
cases = load_cases()

st.markdown('<div class="eyebrow">미래의 의료인을 위한 사례 기반 학습</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">결과를 되짚고,<br>다음의 안전을 설계합니다.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-copy">M&amp;M 컨퍼런스에서 영감을 받은 사례 기반 학습 공간입니다. '
    '가상의 임상 사례를 살펴보고, 사건의 흐름을 재구성하며, 시스템적 요인을 분석하고, 이해한 내용을 점검해 보세요.</div>',
    unsafe_allow_html=True,
)

st.write("")
metric_cols = st.columns(3)
metrics = [
    (f"{len(cases):02d}", "가상 교육 사례"),
    ("04", "구조화된 리뷰 단계"),
    ("01", "핵심 원칙 · 비난보다 개선"),
]
for col, (number, label) in zip(metric_cols, metrics):
    with col:
        with st.container(border=True):
            st.markdown(f'<div class="metric-number">{number}</div><div class="metric-label">{label}</div>', unsafe_allow_html=True)

st.write("")
left, right = st.columns([1.25, 1], gap="large")
with left:
    st.markdown('<div class="eyebrow">리뷰 방법</div>', unsafe_allow_html=True)
    st.markdown("### 결과에서 이해로")
    st.markdown(
        "1. **재구성** — 어떤 일이 언제 일어났는지 확인합니다.\n\n"
        "2. **해석** — 당시의 정보와 판단, 사건에 영향을 준 조건을 살펴봅니다.\n\n"
        "3. **개선** — 평가 가능한 시스템 수준의 개선책을 제안합니다."
    )
with right:
    with st.container(border=True):
        st.markdown('<div class="eyebrow">여기서 시작하기 · 01</div>', unsafe_allow_html=True)
        st.markdown("### 사례 아카이브로 이동")
        st.write("가상의 사례를 선택하고 단계별 리뷰를 시작해 보세요.")
        st.page_link("views/case_library.py", label="사례 살펴보기 →")

st.write("")
st.caption("교육용 프로토타입 · 모든 사례는 가상의 합성 사례이며 실제 임상 의사결정이나 환자 진료에 사용할 수 없습니다.")
