import transformers

def load_models():
    # English to Chinese
    EN_ZH_MODEL = "Helsinki-NLP/opus-mt-en-zh"
    en_zh_tokenizer = transformers.AutoTokenizer.from_pretrained(EN_ZH_MODEL)
    en_zh_model = transformers.AutoModelForSeq2SeqLM.from_pretrained(EN_ZH_MODEL)
    en_zh_translator = transformers.pipeline("text2text-generation", model=en_zh_model, tokenizer=en_zh_tokenizer, device=0)
    # Chinese to English
    ZH_EN_MODEL = "Helsinki-NLP/opus-mt-zh-en"
    zh_en_tokenizer = transformers.AutoTokenizer.from_pretrained(ZH_EN_MODEL)
    zh_en_model = transformers.AutoModelForSeq2SeqLM.from_pretrained(ZH_EN_MODEL)
    zh_en_translator = transformers.pipeline("text2text-generation", model=zh_en_model, tokenizer=zh_en_tokenizer, device=0)
    return en_zh_translator, zh_en_translator
    
en_zh_translator, zh_en_translator = load_models()

