# M&M 리뷰 스튜디오

Streamlit 기반의 M&M(Morbidity & Mortality) Conference 교육용 웹사이트 프로토타입입니다. 기본 UI는 한국어이며, 사례는 모두 가상의 합성 사례입니다.

## GitHub Codespaces에서 실행

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py --server.address 0.0.0.0
```

Codespaces 하단 **Ports** 탭에서 `8501`을 열어 **Open in Browser**를 누르세요.

## 폴더 구조

- `app.py`: 앱 실행, 페이지 이동, MONOCHROME 테마 전환
- `assets/styles.css`: 전체 디자인, 글래스 효과, 스크롤 스타일
- `components/hero.py`: 스크롤에 반응하는 한국어 메인 문구
- `data/cases.json`: 가상의 교육 사례 데이터
- `utils/case_loader.py`: 사례 데이터 읽기
- `views/`: 개요, 사례 아카이브, 리뷰 룸, 학습 점검

## 주의

모든 사례는 교육용 합성 사례입니다. 실제 환자 기록, 환자 식별 정보, 병원 내부 자료를 업로드하지 마세요. 이 앱은 임상 의사결정이나 환자 진료를 위한 도구가 아닙니다.
