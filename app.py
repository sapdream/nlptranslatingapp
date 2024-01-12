import streamlit as st
import time
import transformers

@st.cache_resource
def load_models():
    # English to Chinese
    EN_ZH_MODEL = "Helsinki-NLP/opus-mt-en-zh"
    en_zh_tokenizer = transformers.AutoTokenizer.from_pretrained(EN_ZH_MODEL)
    en_zh_model = transformers.AutoModelForSeq2SeqLM.from_pretrained(EN_ZH_MODEL)
    en_zh_translator = transformers.pipeline("text2text-generation", model=en_zh_model, tokenizer=en_zh_tokenizer)
    # Chinese to English
    ZH_EN_MODEL = "Helsinki-NLP/opus-mt-zh-en"
    zh_en_tokenizer = transformers.AutoTokenizer.from_pretrained(ZH_EN_MODEL)
    zh_en_model = transformers.AutoModelForSeq2SeqLM.from_pretrained(ZH_EN_MODEL)
    zh_en_translator = transformers.pipeline("text2text-generation", model=zh_en_model, tokenizer=zh_en_tokenizer)
    return en_zh_translator, zh_en_translator
    
en_zh_translator, zh_en_translator = load_models()

def en_to_zh(input_text):
    input_text = input_text.strip()
    if len(input_text) > 0:
        transation = en_zh_translator(input_text)[0]["generated_text"]
        return transation.strip()
    else:
        return ""

def zh_to_en(input_text):
    input_text = input_text.strip()
    if len(input_text) > 0:
        transation = zh_en_translator(input_text)[0]["generated_text"]
        return transation.strip()
    else:
        return ""

st.title("English-Chinese Translation App")

direction = st.selectbox("Direction", ["English -> Chinese", "Chinese -> English"])

input_text = st.text_area("Input text", value="")

start_time = time.time()
if direction == "English -> Chinese":
    translation = en_to_zh(input_text)
else:
    translation = zh_to_en(input_text)
end_time = time.time()

time_taken = str(round(end_time-start_time,2))
    
st.markdown("**Translation**: "+translation)

st.markdown("Time taken: "+str(time_taken)+"s")

