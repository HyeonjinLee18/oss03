import streamlit as st
from datetime import datetime

st.set_page_config(page_title="EC2 Streamlit Demo", page_icon="🚀")

st.title("🚀 EC2 Streamlit 배포 실습")
st.write("AWS Learner Lab의 EC2 환경에서 실행 중인 Streamlit 앱입니다.")

name = st.text_input("이름을 입력하세요")

menu = st.selectbox(
    "현재 학년을 선택하세요",
    ["1학년", "2학년", "3학년", "4학년"]
)

if st.button("결과 확인하기"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.success(f"{name}님은 현재 [{menu}]학년입니다.")
    st.write(f"실행 시간: {now}")

    print(f"[LOG] 버튼 클릭됨 / 이름: {name} / 선택: {menu} / 시간: {now}", flush=True)

st.divider()

st.subheader("과제 확인용 설명")
st.write("""
이 앱은 EC2 서버에서 Streamlit으로 실행되며,
브라우저에서 EC2 Public IPv4 주소와 8501 포트로 접속할 수 있습니다.
""")