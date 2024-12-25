import streamlit as st
import random

# Define English and Arabic word lists
word_lists = {
    "English": {
        "Grade1": ["adventure", "hill", "shirt", "black", "house", "stem"],
        "Grade2": ["africa", "curiosity", "mirror", "after", "dresser", "palestine"],
        "Grade3": ["apartment", "illuminate", "numbers", "backpack", "invent", "nutmeg"],
        "Grade4": ["ambiguous", "giraffe", "percentage", "antarctic", "glamorous", "phenomenal"],
        "Grade5": ["abdicate", "eccentricity", "perpendicular", "accommodate", "evaporate"],
        "Grade6": ["administration", "ephemeral", "mischievous", "advanced", "esoteric"],
        "Grade7": ["accompany", "enlisted", "perspicacity", "affirmation", "euphoria"],
        "Grade8": ["adage", "detrimental", "onomatopoeia", "affirmation", "dexterity"],
    },
    "Arabic": {
        "Grade1": ["مغامرة", "تل", "قميص", "أسود", "بيت", "جذع"],
        "Grade2": ["أفريقيا", "فضول", "مرآة", "بعد", "خزانة", "فلسطين"],
        "Grade3": ["شقة", "إضاءة", "أرقام", "حقيبة ظهر", "اختراع", "جوزة الطيب"],
        "Grade4": ["غامض", "زرافة", "نسبة مئوية", "أنتاركتيكا", "رائع", "ظاهرة"],
        "Grade5": ["تنحي", "غرابة", "عمودي", "استيعاب", "تبخر"],
        "Grade6": ["إدارة", "عابر", "مؤذ", "متقدم", "غامض"],
        "Grade7": ["مرافقة", "مجند", "بصيرة", "تأكيد", "نشوة"],
        "Grade8": ["مثل", "ضار", "محاكاة صوتية", "تأكيد", "براعة"],
    },
}

# Initialize state to track used words, contestants, and rounds
if "used_words" not in st.session_state:
    st.session_state["used_words"] = {"English": {grade: [] for grade in word_lists["English"].keys()},
                                      "Arabic": {grade: [] for grade in word_lists["Arabic"].keys()}}
if "contestants" not in st.session_state:
    st.session_state["contestants"] = {"English": {grade: [] for grade in word_lists["English"].keys()},
                                       "Arabic": {grade: [] for grade in word_lists["Arabic"].keys()}}
if "round" not in st.session_state:
    st.session_state["round"] = {"English": {grade: 1 for grade in word_lists["English"].keys()},
                                 "Arabic": {grade: 1 for grade in word_lists["Arabic"].keys()}}
if "round_history" not in st.session_state:
    st.session_state["round_history"] = {"English": {grade: {} for grade in word_lists["English"].keys()},
                                         "Arabic": {grade: {} for grade in word_lists["Arabic"].keys()}}

# Streamlit app title
st.title("📝 MD Tutorials: Spelling Bee Competition")

# Toggle button for language
language = st.radio("Select Language:", ["English", "Arabic"])

# Sidebar for grade and customization
st.sidebar.header("Customize Spelling Bee")
selected_grade = st.sidebar.selectbox("Select Grade:", options=list(word_lists[language].keys()))

# Input number of contestants
st.subheader("Setup Contestants")
num_contestants = st.number_input("Number of contestants:", min_value=1, step=1, key=f"{language}_contestants_input")

# Assign words for the current round
if st.button("Assign Words for Current Round"):
    available_words = [
        word for word in word_lists[language][selected_grade]
        if word not in st.session_state["used_words"][language][selected_grade]
    ]

    if len(available_words) >= num_contestants:
        assigned_words = random.sample(available_words, num_contestants)
        st.session_state["used_words"][language][selected_grade].extend(assigned_words)
        st.session_state["contestants"][language][selected_grade] = assigned_words

        # Save to round history
        current_round = st.session_state["round"][language][selected_grade]
        st.session_state["round_history"][language][selected_grade][current_round] = assigned_words

        st.success(f"Round {current_round} Words Assigned ({language}):")
        for i, word in enumerate(assigned_words, start=1):
            st.write(f"Contestant {i}: {word}")
    else:
        st.warning(f"Not enough {language} words available to assign to all contestants.")

# Display round history
st.subheader("Round History")
if selected_grade in st.session_state["round_history"][language]:
    for round_number, words in st.session_state["round_history"][language][selected_grade].items():
        st.markdown(f"**Round {round_number}:** {', '.join(words)}")

# Progress to the next round
if st.button("Next Round"):
    st.session_state["round"][language][selected_grade] += 1
    st.success(f"Advanced to Round {st.session_state['round'][language][selected_grade]} ({language}).")
