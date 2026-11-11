import streamlit as st

from utils.case_loader import get_case, load_cases


cases = load_cases()
case_id = st.session_state.get("active_case_id", cases[0]["id"])
case = get_case(case_id) or cases[0]

st.markdown('<div class="eyebrow">02 / 구조화된 사례 리뷰</div>', unsafe_allow_html=True)
st.markdown(f'<div class="section-heading">{case["title"]}</div>', unsafe_allow_html=True)
st.markdown(
    f'<span class="case-tag">{case["id"]}</span> '
    f'<span class="case-tag">{case["specialty"]}</span> '
    f'<span class="case-tag">{case["case_type"]}</span>',
    unsafe_allow_html=True,
)
st.write("")
st.info("가상의 교육 시나리오입니다. 실제 환자 기록이나 식별 가능한 환자 정보는 사용하지 않았습니다.")
st.markdown("### 사례 개요")
st.write(case["summary"])

st.markdown("### 01 — 사건 타임라인 재구성")
for event in case["timeline"]:
    with st.container(border=True):
        st.markdown(f'<div class="timeline-time">{event["time"]}</div>', unsafe_allow_html=True)
        st.markdown(f"#### {event['title']}")
        st.write(event["detail"])

left, right = st.columns(2, gap="large")
with left:
    st.markdown("### 02 — 사건에 영향을 준 조건")
    for item in case["contributors"]:
        st.markdown(f"- {item}")
with right:
    st.markdown("### 03 — 함께 생각해 볼 질문")
    for item in case["system_questions"]:
        st.markdown(f"- {item}")

st.markdown("### 04 — 학습 목표")
for objective in case["learning_objectives"]:
    st.markdown(f"- {objective}")

with st.container(border=True):
    st.markdown('<div class="eyebrow">핵심 정리</div>', unsafe_allow_html=True)
    st.write(case["takeaway"])

st.page_link("views/learning_check.py", label="학습 점검으로 이동 →")
