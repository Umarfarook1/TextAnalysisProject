import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def extract_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Attempt to extract the title
    title_element = soup.select_one('header h1')
    
    if title_element:
        title = title_element.text
    else:
        title = "Title not found"

    # Attempt to extract the article text
    article_text_element = soup.find('div', class_='td-ss-main-content')
    
    if article_text_element:
        article_text = article_text_element.text
    else:
        article_text = "Article text not found"

    return title, article_text

def main():
    input_df = pd.read_excel('TextAnalysisProject/data/Input.xlsx')
    articles_dir = 'TextAnalysisProject/data/articles/'

    if not os.path.exists(articles_dir):
        os.makedirs(articles_dir)

    for index, row in input_df.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        
        title, article_text = extract_article(url)
        
        with open(f'{articles_dir}{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write(title + "\n\n" + article_text)

if __name__ == '__main__':
    main()
