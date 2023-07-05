```python
import unittest
import requests
from LangChain_app.lifecycle_events import handle_lifecycle_event
from LangChain_app.utils import parse_lifecycle_event

class TestLifecycleEvents(unittest.TestCase):
    def setUp(self):
        self.api_endpoint = "http://localhost:5000/api"
        self.lifecycle_event_string = "Lifecycle event string here"
        self.lifecycle_event = parse_lifecycle_event(self.lifecycle_event_string)

    def test_handle_lifecycle_event(self):
        response = handle_lifecycle_event(self.lifecycle_event)
        self.assertIsNotNone(response)

    def test_lifecycle_event_api(self):
        response = requests.post(self.api_endpoint, json=self.lifecycle_event)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```