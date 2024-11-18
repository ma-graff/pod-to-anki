import pypandoc
import os

# INPUT_FOLDER = '/Users/matt/Documents/Ça s_explique'

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith('.docx'):
        docx_path = os.path.join(INPUT_FOLDER, filename)
        txt_path = os.path.splitext(docx_path)[0] + '.txt'
        pypandoc.convert_file(docx_path, 'plain', outputfile=txt_path)
        print(f'Converted {docx_path} to {txt_path}')