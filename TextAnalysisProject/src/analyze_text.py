import nltk
from textblob import TextBlob
import os

# Ensure NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

def load_master_dictionary():
    with open('TextAnalysisProject/data/MasterDictionary/positive-words.txt', 'r', encoding='utf-8', errors='ignore') as file:
        positive_words = set(file.read().split())
    with open('TextAnalysisProject/data/MasterDictionary/negative-words.txt', 'r', encoding='utf-8', errors='ignore') as file:
        negative_words = set(file.read().split())
    return positive_words, negative_words

def load_stop_words():
    stop_words = set(nltk.corpus.stopwords.words('english'))
    
    # Load additional stop words from files
    stop_words_files = [
        'TextAnalysisProject/data/StopWords/StopWords_Names.txt',
        'TextAnalysisProject/data/StopWords/StopWords_Geographic.txt',
        'TextAnalysisProject/data/StopWords/StopWords_GenericLong.txt',
        'TextAnalysisProject/data/StopWords/StopWords_Generic.txt',
        'TextAnalysisProject/data/StopWords/StopWords_DatesandNumbers.txt',
        'TextAnalysisProject/data/StopWords/StopWords_Currencies.txt',
        'TextAnalysisProject/data/StopWords/StopWords_Auditor.txt'
    ]
    
    for file_path in stop_words_files:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            stop_words.update(file.read().split())
    
    return stop_words

positive_words, negative_words = load_master_dictionary()
stop_words = load_stop_words()

def analyze_text(text):
    blob = TextBlob(text)
    sentences = blob.sentences
    words = [word.lower() for word in blob.words if word.lower() not in stop_words]  # Exclude stop words

    positive_score = sum(1 for word in words if word in positive_words)
    negative_score = sum(1 for word in words if word in negative_words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = blob.sentiment.subjectivity
    avg_sentence_length = sum(len(sentence.words) for sentence in sentences) / len(sentences) if sentences else 0
    complex_words_count = sum(1 for word in words if len(word) > 2)  # Define your criteria for complex words
    percentage_of_complex_words = complex_words_count / len(words) * 100 if words else 0
    fog_index = 0.4 * (avg_sentence_length + percentage_of_complex_words)
    avg_number_of_words_per_sentence = avg_sentence_length
    word_count = len(words)
    syllables_per_word = sum(len(word) // 3 for word in words) / len(words) if words else 0  # Define your criteria
    personal_pronouns_count = sum(1 for word in words if word.lower() in ['i', 'we', 'me', 'us', 'my', 'our', 'mine', 'ours'])
    avg_word_length = sum(len(word) for word in words) / len(words) if words else 0

    return {
        'positive_score': positive_score,
        'negative_score': negative_score,
        'polarity_score': polarity_score,
        'subjectivity_score': subjectivity_score,
        'avg_sentence_length': avg_sentence_length,
        'percentage_of_complex_words': percentage_of_complex_words,
        'fog_index': fog_index,
        'avg_number_of_words_per_sentence': avg_number_of_words_per_sentence,
        'complex_words_count': complex_words_count,
        'word_count': word_count,
        'syllables_per_word': syllables_per_word,
        'personal_pronouns_count': personal_pronouns_count,
        'avg_word_length': avg_word_length
    }
