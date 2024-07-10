import unittest
from datetime import datetime
from translator.translator import State, Message

class TestState(unittest.TestCase):

    def test_input_missing(self):
        state = State()
        state.text = ""
        self.assertTrue(state.input_missing)

    def test_output_translation(self):
        state = State()
        state.text = "Hello"
        state.lang = "Spanish"
        translated_output = state.output()
        self.assertEqual(translated_output, "Hola")

    def test_message_posting(self):
        state = State()
        form_data = {"text": "Hello"}
        state.post(form_data)
        self.assertEqual(len(state.messages), 1)
        self.assertEqual(state.messages[0].original_text, "Hello")

    def test_message_date_format(self):
        state = State()
        form_data = {"text": "Hello"}
        state.post(form_data)
        message_date = state.messages[0].created_at
        self.assertTrue(datetime.strptime(message_date, "%B %d, %Y %I:%M %p"))

if __name__ == '__main__':
    unittest.main()
