import unittest
from unittest.mock import MagicMock
from translator.translator import header, translation_form, past_translation, smallcaps, output, past_translations_timeline, Message, State

class TestComponents(unittest.TestCase):

    def test_header_rendering(self):
        header_component = header()
        self.assertIn("Translator 🗺", str(header_component))

    def test_past_translation_rendering(self):
        message = Message(original_text="Hello", text="Hola", created_at="July 10, 2024 10:00 AM", to_lang="Spanish")
        past_translation_component = past_translation(message)
        self.assertIn("Hello", str(past_translation_component))
        self.assertIn("Hola", str(past_translation_component))

    def test_smallcaps_text_rendering(self):
        smallcaps_component = smallcaps("Output")
        self.assertIn("Output", str(smallcaps_component))

if __name__ == '__main__':
    unittest.main()
