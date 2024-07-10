import unittest
from translator.translator import State

class TestValidation(unittest.TestCase):

    def test_input_validation_missing_text(self):
        state = State()
        state.text = ""
        self.assertTrue(state.input_missing)

    def test_input_validation_text_present(self):
        state = State()
        state.text = "Hello"
        self.assertFalse(state.input_missing)

if __name__ == '__main__':
    unittest.main()
