import unittest

import pythonAssesment as assessment


class NewsArticleAnalysisTest(unittest.TestCase):
    def test_extract_words_normalizes_case_and_apostrophes(self):
        text = "Apple pie isn't hard. Apple Pie isn\u2019t magic."

        self.assertEqual(
            assessment.extract_words(text),
            ["apple", "pie", "isn't", "hard", "apple", "pie", "isn't", "magic"],
        )

    def test_count_specific_word_uses_whole_words(self):
        text = "Pie pie-making pies apple-pie PIE."

        self.assertEqual(assessment.count_specific_word(text, "pie"), 4)
        self.assertEqual(assessment.count_specific_word(text, "pies"), 1)
        self.assertEqual(assessment.count_specific_word(text, ""), 0)

    def test_identify_most_common_word(self):
        self.assertEqual(assessment.identify_most_common_word("Apple pie apple"), "apple")
        self.assertIsNone(assessment.identify_most_common_word(""))

    def test_calculate_average_word_length_excludes_punctuation(self):
        self.assertEqual(assessment.calculate_average_word_length("Hi, you!"), 2.5)
        self.assertEqual(assessment.calculate_average_word_length(""), 0.0)

    def test_count_paragraphs(self):
        text = "First paragraph.\n\nSecond paragraph.\n\n\nThird paragraph."

        self.assertEqual(assessment.count_paragraphs(text), 3)
        self.assertEqual(assessment.count_paragraphs("   "), 0)

    def test_count_sentences(self):
        self.assertEqual(assessment.count_sentences("One. Two! Three?"), 3)
        self.assertEqual(assessment.count_sentences("No sentence ending"), 0)

    def test_article_analysis_values(self):
        article = assessment.load_text("news article.txt")

        self.assertEqual(assessment.count_specific_word(article, "pie"), 21)
        self.assertEqual(assessment.identify_most_common_word(article), "the")
        self.assertEqual(assessment.count_paragraphs(article), 19)
        self.assertEqual(assessment.count_sentences(article), 48)


if __name__ == "__main__":
    unittest.main()
