import unittest
from translator.translator import header, translation_form, past_translation, smallcaps, output, past_translations_timeline, Message

class TestComponents(unittest.TestCase):

    def test_header_rendering(self):
        header_component = header()
        self.assertIn("Translator 🗺", header_component.to_html())

    def test_translation_form_rendering(self):
        translation_form_component = translation_form()
        self.assertIsNotNone(translation_form_component.to_html())

    def test_past_translation_rendering(self):
        message = Message(original_text="Hello", text="Hola", created_at="July 10, 2024 10:00 AM", to_lang="Spanish")
        past_translation_component = past_translation(message)
        self.assertIn("Hello", past_translation_component.to_html())
        self.assertIn("Hola", past_translation_component.to_html())

    def test_smallcaps_text_rendering(self):
        smallcaps_component = smallcaps("Output")
        self.assertIn("Output", smallcaps_component.to_html())

    def test_output_component_rendering(self):
        state = State()
        state.text = "Hello"
        output_component = output()
        self.assertIn(state.output(), output_component.to_html())

    def test_past_translations_timeline_rendering(self):
        state = State()
        form_data = {"text": "Hello"}
        state.post(form_data)
        past_translations_timeline_component = past_translations_timeline()
        self.assertIn("Hello", past_translations_timeline_component.to_html())

if __name__ == '__main__':
    unittest.main()
