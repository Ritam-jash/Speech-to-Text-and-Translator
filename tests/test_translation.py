# import unittest
# from utils.translation import translate_text

# class TestTranslation(unittest.TestCase):

#     def test_translate_text(self):
#         translated = translate_text("Hello", "es")  # Translate to Spanish
#         self.assertEqual(translated, "Hola")  # Adjust based on the expected output

# if __name__ == "__main__":
#     unittest.main()








# import unittest
# import warnings
# from utils.translation import translate_text

# # Suppress Deprecation and Resource Warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)
# warnings.filterwarnings("ignore", category=ResourceWarning)

# class TestTranslation(unittest.TestCase):

#     def test_translate_text(self):
#         translated = translate_text("Hello", "es")  # Translate to Spanish
#         self.assertEqual(translated, "Hola")  # Adjust based on the expected output

# if __name__ == "__main__":
#     unittest.main()














import unittest
import warnings
import gc
from utils.translation import translate_text

# Suppress Deprecation and Resource Warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=ResourceWarning)

class TestTranslation(unittest.TestCase):

    def test_translate_text(self):
        translated = translate_text("Hello", "es")  # Translate to Spanish
        self.assertEqual(translated, "Hola")  # Adjust based on the expected output

    def tearDown(self):
        # Force garbage collection to close any open resources
        gc.collect()

if __name__ == "__main__":
    unittest.main()

