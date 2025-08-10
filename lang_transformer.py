from transformers import MarianMTModel, MarianTokenizer


class Translator:
    def __init__(self, l_from, l_to):
        model_name = f"Helsinki-NLP/opus-mt-{l_from}-{l_to}"
        self.tokenizer = MarianTokenizer.from_pretrained(model_name)
        self.model = MarianMTModel.from_pretrained(model_name)

    def translate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True)
        translated = self.model.generate(**inputs)
        tgt_text = [self.tokenizer.decode(t, skip_special_tokens=True) for t in translated]
        return tgt_text
