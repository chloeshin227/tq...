import streamlit as st


@st.cache_resource
def _register_scroll_story():
    """브라우저에서 스크롤 위치를 감지하는 메인 인트로 컴포넌트."""
    html = """
    <section class="mm-story" aria-label="M&M 리뷰 스튜디오 소개">
      <div class="mm-story__meta">
        <span>M&amp;M REVIEW STUDIO</span>
        <span>교육 · 시스템 · 환자 안전</span>
      </div>

      <div class="mm-story__line" data-scroll-line><span>모든 결과에는<br><em>질문이 남습니다.</em></span></div>
      <div class="mm-story__line" data-scroll-line><span>놓친 신호는<br><em>무엇이었을까요?</em></span></div>
      <div class="mm-story__line" data-scroll-line><span>어디에서<br><em>시스템이 흔들렸을까요?</em></span></div>
      <div class="mm-story__line" data-scroll-line><span>비난이 아니라,<br><em>더 나은 시스템을.</em></span></div>

      <div class="mm-story__footer">
        <span>이환율·사망률 컨퍼런스 교육</span>
        <span>스크롤하여 살펴보기 ↓</span>
      </div>
    </section>
    """

    css = """
    .mm-story { box-sizing: border-box; width: 100%; }
    .mm-story * { box-sizing: border-box; }
    """

    js = """
    export default function({ parentElement }) {
      const lines = parentElement.querySelectorAll('[data-scroll-line]');
      if (!lines.length) return;
      const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          entry.target.classList.toggle('is-active', entry.isIntersecting);
        });
      }, {
        root: null,
        rootMargin: '-43% 0px -43% 0px',
        threshold: 0
      });
      lines.forEach((line) => observer.observe(line));
      return () => observer.disconnect();
    }
    """

    return st.components.v2.component(
        name="mm_scroll_story_ko",
        html=html,
        css=css,
        js=js,
        isolate_styles=False,
    )


def render_hero():
    component = _register_scroll_story()
    component()
