from deep_translator import GoogleTranslator
import os

def translate_file(input_file, output_file, source_lang='auto', target_lang='en'):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translated_text = translator.translate(text)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(translated_text)

if __name__ == "__main__":
    input_file_path = 'test_data/fr_CA/txt/ranked_terms_tfidf.txt'
    output_file_path = 'test_data/fr_CA/txt/ranked_terms_tfidf_EN.txt'
    
    translate_file(input_file_path, output_file_path)