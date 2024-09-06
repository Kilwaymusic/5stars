import streamlit as st

# 제목
st.title("에셋 스토어 별점 계산기")

# 입력 폼
five_star = st.number_input("5점 리뷰 수", min_value=0, value=0)
four_star = st.number_input("4점 리뷰 수", min_value=0, value=0)
three_star = st.number_input("3점 리뷰 수", min_value=0, value=0)
two_star = st.number_input("2점 리뷰 수", min_value=0, value=0)
one_star = st.number_input("1점 리뷰 수", min_value=0, value=0)

if st.button("계산하기"):
    # 리뷰 데이터
    ratings = {
        '5_star': five_star,
        '4_star': four_star,
        '3_star': three_star,
        '2_star': two_star,
        '1_star': one_star
    }

    # 현재 합계와 총 리뷰 수 계산
    current_sum = (5 * ratings['5_star'] + 4 * ratings['4_star'] + 3 * ratings['3_star'] + 2 * ratings['2_star'] + 1 * ratings['1_star'])
    total_reviews = sum(ratings.values())

    # 현재 평균 계산
    current_average = current_sum / total_reviews

    # 목표 평균
    target_average = 4.5

    # 목표 평균을 달성하기 위해 필요한 추가 5점 리뷰 수 계산
    additional_reviews = (target_average * total_reviews - current_sum) / (5 - target_average)
    additional_reviews = int(additional_reviews) + 1 if additional_reviews % 1 != 0 else int(additional_reviews)

    # 결과 출력
    st.write(f"현재 별점 평균: {current_average:.2f}")
    st.write(f"목표 평균을 달성하기 위해 필요한 추가 5점 리뷰 수: {additional_reviews}")
