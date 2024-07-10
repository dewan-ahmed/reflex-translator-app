import unittest
from datetime import datetime
from translator.translator import State

class TestDateFormat(unittest.TestCase):

    def test_message_date_format(self):
        state = State()
        form_data = {"text": "Hello"}
        state.post(form_data)
        message_date = state.messages[0].created_at
        self.assertTrue(datetime.strptime(message_date, "%B %d, %Y %I:%M %p"))

if __name__ == '__main__':
    unittest.main()
