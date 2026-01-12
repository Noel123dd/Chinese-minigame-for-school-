import streamlit as st
import random

vocab = [
    {"char": "照片", "pinyin": "zhàopiàn", "def": "photo picture"},
    {"char": "家", "pinyin": "jiā", "def": "family"},
    {"char": "口", "pinyin": "kǒu", "def": "measure word"},
    {"char": "爷爷", "pinyin": "yéye", "def": "paternal grandpa"},
    {"char": "奶奶", "pinyin": "nǎinai", "def": "paternal grandma"},
    {"char": "爸爸", "pinyin": "bàba", "def": "dad"},
    {"char": "妈妈", "pinyin": "māma", "def": "mom"},
    {"char": "哥哥", "pinyin": "gēge", "def": "elder brother"},
    {"char": "姐姐", "pinyin": "jiějie", "def": "elder sister"},
    {"char": "只", "pinyin": "zhǐ", "def": "only"}
]

if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_q = 0
    st.session_state.quiz_complete = False
    random.shuffle(vocab)
    st.session_state.shuffled_vocab = vocab

st.title("Chinese Character Quiz (Lesson 10)")
st.write("Test your knowledge of these 10 words!")

if not st.session_state.quiz_complete:
    idx = st.session_state.current_q
    word = st.session_state.shuffled_vocab[idx]
    
    st.subheader(f"Question {idx + 1} of 10")
    st.info(f"What does this mean? **{word['char']}** ({word['pinyin']})")

    correct = word['def']
    others = [w['def'] for w in vocab if w['def'] != correct]
    
    if 'current_options' not in st.session_state or st.session_state.opt_idx != idx:
        opts = random.sample(others, 3) + [correct]
        random.shuffle(opts)
        st.session_state.current_options = opts
        st.session_state.opt_idx = idx

    answer = st.radio("Choose the correct definition:", st.session_state.current_options)

    if st.button("Submit Answer"):
        if answer == correct:
            st.success("Correct! ✨")
            st.session_state.score += 1
        else:
            st.error(f"Wrong! The correct answer was: {correct}")

        if st.session_state.current_q < 9:
            st.session_state.current_q += 1
            st.rerun() 
        else:
            st.session_state.quiz_complete = True
            st.rerun()

else:
    st.balloons()
    st.header("Quiz Completed!")
    st.metric("Final Score", f"{st.session_state.score} / 10")
    
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.current_q = 0
        st.session_state.quiz_complete = False
        random.shuffle(vocab)
        st.session_state.shuffled_vocab = vocab
        st.rerun()