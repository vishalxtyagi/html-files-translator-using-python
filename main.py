from englisttohindi.englisttohindi import EngtoHindi
from bs4 import BeautifulSoup

def translate_html_file(input_file_path, output_file_path):
    # Read the input HTML file and create a BeautifulSoup object
    with open(input_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Find all the HTML tags that contain text
    tags = soup.find_all(string=True)

    for tag in tags:
        if tag.parent.name in ['script', 'style']:
            continue  # skip script and style tags
        english_text = tag.text.strip()
        if english_text:
            hindi_text = EngtoHindi(english_text).convert
            print(english_text, '->', hindi_text)
            tag.replace_with(hindi_text)

    # Save the modified HTML to a new file
    with open(output_file_path, 'w+', encoding='utf-8') as file:
        file.write(str(soup))

if __name__ == '__main__':
    translate_html_file('source/index.html', 'translated/index.html')