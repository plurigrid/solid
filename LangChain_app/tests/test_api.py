```python
import unittest
import requests
from LangChain_app.api import api_endpoint

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = api_endpoint

    def test_contract_module_endpoint(self):
        response = requests.get(f"{self.base_url}/contract_module")
        self.assertEqual(response.status_code, 200)

    def test_lifecycle_event_endpoint(self):
        response = requests.get(f"{self.base_url}/lifecycle_event")
        self.assertEqual(response.status_code, 200)

    def test_parse_contract_module(self):
        contract_module_string = "contract module string"
        response = requests.post(f"{self.base_url}/parse_contract_module", data=contract_module_string)
        self.assertEqual(response.status_code, 200)

    def test_parse_lifecycle_event(self):
        lifecycle_event_string = "lifecycle event string"
        response = requests.post(f"{self.base_url}/parse_lifecycle_event", data=lifecycle_event_string)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
```