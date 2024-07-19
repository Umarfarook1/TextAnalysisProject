import pandas as pd
import os
from analyze_text import analyze_text

def main():
    # Use raw string literals or double backslashes
    input_path = r'TextAnalysisProject\data\Input.xlsx'
    articles_dir = r'TextAnalysisProject\data\articles'
    output_path = r'TextAnalysisProject\data\Output Data Structure.xlsx'

    input_df = pd.read_excel(input_path)
    
    output_columns = [
        'URL_ID', 'URL', 'positive_score', 'negative_score', 'polarity_score',
        'subjectivity_score', 'avg_sentence_length', 'percentage_of_complex_words',
        'fog_index', 'avg_number_of_words_per_sentence', 'complex_words_count',
        'word_count', 'syllables_per_word', 'personal_pronouns_count', 'avg_word_length'
    ]
    output_df = pd.DataFrame(columns=output_columns)

    results_list = []

    for index, row in input_df.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        file_path = os.path.join(articles_dir, f'{url_id}.txt')
        
        # Check if the file exists before trying to read it
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                text = file.read()
            
            analysis_results = analyze_text(text)
            analysis_results['URL_ID'] = url_id
            analysis_results['URL'] = url
            results_list.append(analysis_results)
        else:
            print(f'File not found: {file_path}')

    # Convert list of dictionaries to DataFrame and save to Excel
    output_df = pd.DataFrame(results_list, columns=output_columns)
    output_df.to_excel(output_path, index=False)

if __name__ == '__main__':
    main()
