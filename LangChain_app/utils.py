```python
import json

def parse_contract_module(contract_module_string):
    try:
        contract_module = json.loads(contract_module_string)
        return contract_module
    except json.JSONDecodeError:
        return None

def parse_lifecycle_event(lifecycle_event_string):
    try:
        lifecycle_event = json.loads(lifecycle_event_string)
        return lifecycle_event
    except json.JSONDecodeError:
        return None
```