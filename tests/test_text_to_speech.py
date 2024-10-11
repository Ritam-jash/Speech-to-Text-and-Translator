import unittest
from utils.text_to_speech import text_to_speech

class TestTextToSpeech(unittest.TestCase):

    def test_text_to_speech(self):
        # This is difficult to test as it generates an audio file
        # We can just check if it runs without errors
        try:
            text_to_speech("Hello")
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
