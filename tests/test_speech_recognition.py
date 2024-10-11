import unittest
from utils.speech_recognition import speech_to_text

class TestSpeechRecognition(unittest.TestCase):

    def test_speech_to_text(self):
        result = speech_to_text()
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()