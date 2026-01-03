import re
from collections import Counter

def analyze_text(text):
    # Count sentences
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])

    # Clean text and count words
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned_text.split()
    word_count = len(words)

    # Get top 10 most frequent words
    word_freq = Counter(words)
    top_10_words = word_freq.most_common(10)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "top_10_words": top_10_words
    }

with open('sample_text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

result = analyze_text(text)
print(result)
