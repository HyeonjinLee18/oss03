import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="MBTI 검사",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 MBTI 검사")
st.write("몇 가지 질문에 답하면 나의 MBTI 성향을 간단히 확인할 수 있습니다.")

st.divider()

name = st.text_input("이름을 입력하세요")

st.subheader("1. 에너지 방향: E / I")

q1 = st.radio(
    "쉬는 날 나는 보통?",
    [
        "친구를 만나거나 밖에 나가서 에너지를 얻는다",
        "혼자 쉬거나 조용한 시간을 보내며 에너지를 얻는다"
    ]
)

q2 = st.radio(
    "처음 보는 사람들과 있을 때 나는?",
    [
        "먼저 말을 걸고 분위기에 잘 적응한다",
        "상대가 먼저 다가오면 편하게 대화한다"
    ]
)

st.subheader("2. 정보 인식: S / N")

q3 = st.radio(
    "문제를 해결할 때 나는?",
    [
        "현실적인 자료와 경험을 바탕으로 판단한다",
        "가능성과 아이디어를 중심으로 생각한다"
    ]
)

q4 = st.radio(
    "설명을 들을 때 더 편한 방식은?",
    [
        "구체적인 예시와 단계별 설명",
        "전체적인 흐름과 핵심 아이디어"
    ]
)

st.subheader("3. 판단 기준: T / F")

q5 = st.radio(
    "의사결정을 할 때 나는?",
    [
        "논리와 객관적인 기준을 우선한다",
        "사람들의 감정과 상황을 함께 고려한다"
    ]
)

q6 = st.radio(
    "친구가 고민을 말하면 나는?",
    [
        "문제 해결 방법을 먼저 제안한다",
        "감정을 공감하고 위로를 먼저 해준다"
    ]
)

st.subheader("4. 생활 방식: J / P")

q7 = st.radio(
    "과제를 할 때 나는?",
    [
        "미리 계획을 세우고 차근차근 진행한다",
        "마감이 가까워지면 집중해서 처리한다"
    ]
)

q8 = st.radio(
    "여행을 갈 때 나는?",
    [
        "일정과 동선을 미리 정해두는 편이다",
        "상황에 따라 자유롭게 움직이는 편이다"
    ]
)

st.divider()

if st.button("MBTI 결과 확인하기"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if name.strip() == "":
        st.warning("이름을 입력해주세요.")
        print(f"[LOG] MBTI 검사 버튼 클릭 / 이름 미입력 / 시간: {now}", flush=True)

    else:
        e_score = 0
        i_score = 0
        s_score = 0
        n_score = 0
        t_score = 0
        f_score = 0
        j_score = 0
        p_score = 0

        # E / I
        if q1 == "친구를 만나거나 밖에 나가서 에너지를 얻는다":
            e_score += 1
        else:
            i_score += 1

        if q2 == "먼저 말을 걸고 분위기에 잘 적응한다":
            e_score += 1
        else:
            i_score += 1

        # S / N
        if q3 == "현실적인 자료와 경험을 바탕으로 판단한다":
            s_score += 1
        else:
            n_score += 1

        if q4 == "구체적인 예시와 단계별 설명":
            s_score += 1
        else:
            n_score += 1

        # T / F
        if q5 == "논리와 객관적인 기준을 우선한다":
            t_score += 1
        else:
            f_score += 1

        if q6 == "문제 해결 방법을 먼저 제안한다":
            t_score += 1
        else:
            f_score += 1

        # J / P
        if q7 == "미리 계획을 세우고 차근차근 진행한다":
            j_score += 1
        else:
            p_score += 1

        if q8 == "일정과 동선을 미리 정해두는 편이다":
            j_score += 1
        else:
            p_score += 1

        mbti = ""
        mbti += "E" if e_score >= i_score else "I"
        mbti += "S" if s_score >= n_score else "N"
        mbti += "T" if t_score >= f_score else "F"
        mbti += "J" if j_score >= p_score else "P"

        st.success(f"{name}님의 간단 MBTI 결과는 {mbti} 입니다!")

        st.write("### 성향 점수")
        st.write(f"- E 점수: {e_score} / I 점수: {i_score}")
        st.write(f"- S 점수: {s_score} / N 점수: {n_score}")
        st.write(f"- T 점수: {t_score} / F 점수: {f_score}")
        st.write(f"- J 점수: {j_score} / P 점수: {p_score}")

        st.write("### 결과 해석")

        descriptions = {
            "E": "외향적인 성향이 강하며 사람들과의 교류에서 에너지를 얻는 편입니다.",
            "I": "내향적인 성향이 강하며 혼자만의 시간에서 에너지를 얻는 편입니다.",
            "S": "현실적이고 구체적인 정보를 중요하게 생각하는 편입니다.",
            "N": "가능성과 아이디어를 중심으로 생각하는 편입니다.",
            "T": "논리와 객관적인 기준을 바탕으로 판단하는 편입니다.",
            "F": "사람의 감정과 관계를 고려하여 판단하는 편입니다.",
            "J": "계획적이고 체계적으로 일을 진행하는 편입니다.",
            "P": "유연하고 상황에 따라 자유롭게 움직이는 편입니다."
        }

        for letter in mbti:
            st.write(f"- **{letter}**: {descriptions[letter]}")

        st.info("이 검사는 간단한 Streamlit 실습용 검사이며, 실제 MBTI 공식 검사와는 다를 수 있습니다.")

        print(
            f"[LOG] MBTI 검사 완료 / 이름: {name} / 결과: {mbti} / "
            f"E:{e_score}, I:{i_score}, S:{s_score}, N:{n_score}, "
            f"T:{t_score}, F:{f_score}, J:{j_score}, P:{p_score} / 시간: {now}",
            flush=True
        )
