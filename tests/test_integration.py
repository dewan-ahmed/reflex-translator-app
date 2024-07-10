import unittest
from translator.translator import State, Message

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_translation_integration(self):
        self.state.text = "Hello"
        self.state.lang = "French"
        translated_output = self.state.output()
        self.assertIsNotNone(translated_output)

    def test_message_posting_integration(self):
        form_data = {"text": "Hello"}
        self.state.post(form_data)
        self.assertEqual(len(self.state.messages), 1)
        self.assertEqual(self.state.messages[0].original_text, "Hello")

if __name__ == '__main__':
    unittest.main()
