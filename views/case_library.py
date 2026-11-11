import streamlit as st

from utils.case_loader import load_cases


st.markdown('<div class="eyebrow">01 / 사례 아카이브</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">사례를 살펴보세요.</div>', unsafe_allow_html=True)
st.markdown('<div class="section-copy">각 사례는 구조화된 리뷰와 비난 없는 시스템 분석을 연습하기 위해 만든 가상 교육 사례입니다.</div>', unsafe_allow_html=True)

cases = load_cases()
query = st.text_input("사례 검색", placeholder="제목, 진료과 또는 주제로 검색하세요.")
all_specialties = sorted({case["specialty"] for case in cases})
specialty = st.selectbox("진료과 선택", ["전체 진료과", *all_specialties])

filtered = []
for case in cases:
    searchable = f"{case['title']} {case['specialty']} {case['topic']}".lower()
    matches_query = query.lower() in searchable
    matches_specialty = specialty == "전체 진료과" or case["specialty"] == specialty
    if matches_query and matches_specialty:
        filtered.append(case)

st.write("")
if not filtered:
    st.info("선택한 조건에 맞는 사례가 없습니다.")

for case in filtered:
    with st.container(border=True):
        meta_left, meta_right = st.columns([3, 1])
        with meta_left:
            st.markdown(f'<span class="case-tag">{case["id"]}</span> <span class="case-tag">{case["level"]}</span>', unsafe_allow_html=True)
            st.markdown(f"### {case['title']}")
            st.write(case["summary"])
            st.caption(f"{case['specialty']}  ·  {case['topic']}")
        with meta_right:
            st.write("")
            if st.button("사례 열기 ↗", key=f"open_{case['id']}", use_container_width=True):
                st.session_state.active_case_id = case["id"]
                st.switch_page("views/case_review.py")
