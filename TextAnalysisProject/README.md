# Text Analysis Project

## Overview

This project performs text analysis on articles extracted from URLs specified in an input Excel file. The analysis includes calculating various textual metrics such as positive score, negative score, polarity score, and more. The results are then saved to an output Excel file.

## File Structure

- `src/`
  - `analyze_text.py` : Python script for text analysis.
  - `extract_articles.py` : Python script for extracting articles (if applicable).
  - `main.py` : Main script that integrates extraction and analysis.
- `data/`
  - `Input.xlsx` : Input Excel file containing article URLs and IDs.
  - `articles/` : Directory containing text files of articles.
  - `Output Data Structure.xlsx` : Output Excel file where results are saved.
  - `MasterDictionary/`
    - `positive-words.txt` : List of positive words.
    - `negative-words.txt` : List of negative words.
  - `StopWords/`
    - Various stop words files for different categories.

## Instructions

### Approach

1. **Data Extraction**:

   - Articles are extracted from URLs listed in `Input.xlsx`.
   - Each article is saved as a text file in the `articles` directory using its URL ID as the filename.

2. **Text Analysis**:

   - The `analyze_text.py` script performs text analysis on each extracted article.
   - Metrics such as positive score, negative score, polarity score, and more are computed using the `TextBlob` library.

3. **Output Generation**:
   - Results from the text analysis are compiled into a DataFrame and saved to `Output Data Structure.xlsx`.

### How to Run the .py File

1. **Install Dependencies**:
   Ensure all required libraries are installed. You can install them using the following command:

   ```bash
   pip install pandas nltk textblob openpyxl
   ```

2. **Run the Main Script**: Execute the main script to perform the analysis and generate the output file:

   `python src/main.py`

   This will read the input file, extract articles, perform text analysis, and save the results to the output Excel file.

## Dependencies

- `pandas`: For data manipulation and analysis.
- `nltk`: For natural language processing tasks.
- `textblob`: For sentiment analysis and other text processing.
- `openpyxl`: For reading/writing Excel files.

## Notes

- Ensure the `Input.xlsx` file is correctly formatted with `URL_ID` and `URL` columns.
- Verify that article files are named correctly and located in the `articles` directory.
- Check the `MasterDictionary` and `StopWords` files for completeness and accuracy.
