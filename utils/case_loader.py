import json
from pathlib import Path

import streamlit as st


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "cases.json"


@st.cache_data
def load_cases():
    with DATA_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def get_case(case_id: str):
    return next((case for case in load_cases() if case["id"] == case_id), None)
