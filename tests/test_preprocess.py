import unittest
from toolkit.preprocess import MiniNLPToolkit

class TestMiniNLPToolkit(unittest.TestCase):

    def setUp(self):
        self.toolkit = MiniNLPToolkit()
        self.sample_text = "This is a simple sentence with punctuation, numbers 123, and stopwords!"

    def test_tokenize(self):
        sentences, words = self.toolkit.tokenize(self.sample_text)
        self.assertTrue(len(sentences) > 0)
        self.assertTrue(len(words) > 0)

    def test_normalize(self):
        normalized = self.toolkit.normalize(self.sample_text)
        self.assertEqual(normalized, "this is a simple sentence with punctuation numbers  and stopwords")

    def test_remove_stopwords(self):
        words = self.sample_text.split()
        filtered_words = self.toolkit.remove_stopwords(words)
        self.assertNotIn("is", filtered_words)
        self.assertNotIn("and", filtered_words)

    def test_stem(self):
        words = ["running", "jumps", "easily"]
        stemmed_words = self.toolkit.stem(words)
        self.assertEqual(stemmed_words, ["run", "jump", "easili"])

    def test_lemmatize(self):
        words = ["running", "jumps", "easily"]
        lemmatized_words = self.toolkit.lemmatize(words)
        self.assertEqual(lemmatized_words, ["running", "jump", "easily"])

    def test_preprocess(self):
        preprocessed = self.toolkit.preprocess(self.sample_text)
        self.assertTrue(preprocessed)
        self.assertNotIn("is", preprocessed.split())
        self.assertNotIn("and", preprocessed.split())

if __name__ == "__main__":
    unittest.main()
