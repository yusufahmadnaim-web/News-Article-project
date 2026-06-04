import re
from collections import Counter
from pathlib import Path

WORD_PATTERN = re.compile(r"[A-Za-z0-9]+(?:['\u2019][A-Za-z0-9]+)?")
SENTENCE_ENDING_PATTERN = re.compile(r"[.!?]+")
PARAGRAPH_SEPARATOR_PATTERN = re.compile(r"(?:\r?\n){2,}")


def extract_words(text):
    """Return a list of lowercase words found in the text."""
    if not text:
        return []

    return [word.replace("\u2019", "'").lower() for word in WORD_PATTERN.findall(text)]


def word_length(word):
    """Return the number of letters or digits in a word."""
    return sum(character.isalnum() for character in word)


def count_specific_word(text, word):
    """Return the number of whole-word occurrences of a search word in the text."""
    if not text or not word:
        return 0

    search_words = extract_words(word)
    if len(search_words) != 1:
        return 0

    search_word = search_words[0]
    return sum(current_word == search_word for current_word in extract_words(text))


def identify_most_common_word(text):
    """Return the most common word in the text, or None if no words are found."""
    words = extract_words(text)
    if not words:
        return None

    counter = Counter(words)
    return counter.most_common(1)[0][0]


def calculate_average_word_length(text):
    """Return the average word length in the text, excluding punctuation."""
    words = extract_words(text)
    if not words:
        return 0.0

    total_length = sum(word_length(word) for word in words)
    return total_length / len(words)


def count_paragraphs(text):
    """Return the number of paragraphs in the text based on empty lines between blocks."""
    if text is None or text.strip() == "":
        return 0

    paragraphs = [block for block in PARAGRAPH_SEPARATOR_PATTERN.split(text.strip()) if block.strip()]
    return len(paragraphs)


def count_sentences(text):
    """Return the number of sentences in the text using terminal punctuation marks."""
    if text is None or text.strip() == "":
        return 0

    endings = SENTENCE_ENDING_PATTERN.findall(text)
    return len(endings)


def load_text(filename):
    """Read text from a file in the same folder as this script."""
    path = Path(__file__).resolve().parent / filename
    return path.read_text(encoding="utf-8")


def main():
    article_text = load_text("news article.txt")
    search_word = "pie"

    print("News Article Text Analysis")
    print("--------------------------")
    print(f"Count of '{search_word}': {count_specific_word(article_text, search_word)}")
    print(f"Most common word: {identify_most_common_word(article_text)}")
    print(f"Average word length: {calculate_average_word_length(article_text):.2f}")
    print(f"Paragraph count: {count_paragraphs(article_text)}")
    print(f"Sentence count: {count_sentences(article_text)}")


if __name__ == "__main__":
    main()
