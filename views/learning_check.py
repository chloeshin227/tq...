import streamlit as st

from utils.case_loader import get_case, load_cases


cases = load_cases()
case_id = st.session_state.get("active_case_id", cases[0]["id"])
case = get_case(case_id) or cases[0]
quiz = case["quiz"]

st.markdown('<div class="eyebrow">03 / 학습 점검</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">최종 결과 너머를<br>생각해 보세요.</div>', unsafe_allow_html=True)
st.caption(f"{case['id']} · {case['title']}")

with st.form("knowledge_check_form"):
    answer = st.radio(quiz["question"], quiz["options"], index=None)
    submitted = st.form_submit_button("답안 제출")

if submitted:
    if answer is None:
        st.warning("답안을 선택한 뒤 제출해 주세요.")
    else:
        selected_index = quiz["options"].index(answer)
        if selected_index == quiz["answer_index"]:
            st.success("정답입니다. 이 사례에서 강조하는 시스템 수준의 문제를 잘 파악했습니다.")
        else:
            st.warning("아직 정답이 아닙니다. 타임라인과 기여 요인을 다시 살펴보고, 어떤 과정에서 문제가 생겼는지 생각해 보세요.")
        with st.container(border=True):
            st.markdown('<div class="eyebrow">해설</div>', unsafe_allow_html=True)
            st.write(quiz["explanation"])

st.write("")
st.markdown("### 나만의 리뷰 기록")
reflection = st.text_area(
    "어떤 시스템 수준의 개선책을 제안하겠습니까?",
    placeholder="실행 가능한 개선책 한 가지와 효과를 평가할 방법을 적어 보세요.",
    height=130,
)
if st.button("이 세션에 기록 저장"):
    if reflection.strip():
        st.session_state[f"reflection_{case_id}"] = reflection.strip()
        st.success("현재 브라우저 세션에 저장했습니다. 영구 계정이나 데이터베이스는 아직 연결되지 않았습니다.")
    else:
        st.warning("먼저 짧은 리뷰 의견을 작성해 주세요.")
