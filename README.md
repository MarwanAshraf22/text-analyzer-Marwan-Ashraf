# Text Analysis Tool

A simple Python tool for analyzing text files. This project counts words, sentences, and identifies the most frequent words in a given text.

## Features

- **Word Count**: Counts the total number of words in the text
- **Sentence Count**: Identifies and counts sentences based on punctuation marks (`.`, `!`, `?`)
- **Top 10 Most Frequent Words**: Displays the 10 most common words and their frequencies

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone this repository:
```bash
git clone <https://github.com/MarwanAshraf22/Mentorship-Abdo-Kamar.git>
cd Mentorship-Abdo-Kamar
```

2. No additional installation required - the project uses only Python standard library modules.

## Usage

1. Place your text file in the project directory (or modify `main.py` to point to your file)
2. Run the script:
```bash
python main.py
```

The script will analyze `sample_text.txt` by default and print the results:
- Total word count
- Total sentence count
- Top 10 most frequent words with their counts

## Example Output

```
{
    'word_count': 150,
    'sentence_count': 20,
    'top_10_words': [('the', 10), ('and', 8), ('to', 7), ...]
}
```

## Project Structure

```
Mentorship/
├── main.py              # Main analysis script
├── sample_text.txt      # Sample text file for testing
├── requirements.txt     # Python dependencies (empty - uses stdlib only)
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # This file
```

## How It Works

1. The script reads a text file (`sample_text.txt` by default)
2. Uses regular expressions to:
   - Split text into sentences based on punctuation
   - Clean text by removing punctuation and converting to lowercase
   - Split cleaned text into words
3. Uses Python's `Counter` from `collections` to count word frequencies
4. Returns and displays the analysis results

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Marwan Ashraf
