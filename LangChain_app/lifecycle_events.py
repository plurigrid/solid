```python
from utils import parse_lifecycle_event

def handle_lifecycle_event(event_string):
    event = parse_lifecycle_event(event_string)
    
    if event['type'] == 'creation':
        return handle_creation_event(event)
    elif event['type'] == 'transaction':
        return handle_transaction_event(event)
    elif event['type'] == 'termination':
        return handle_termination_event(event)
    else:
        raise ValueError(f"Unsupported lifecycle event type: {event['type']}")

def handle_creation_event(event):
    # Handle creation event here
    pass

def handle_transaction_event(event):
    # Handle transaction event here
    pass

def handle_termination_event(event):
    # Handle termination event here
    pass
```