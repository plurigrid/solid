```python
from solidity import Solidity
from utils import parse_contract_module

def compose_solidity_module(contract_module_string):
    contract_module = parse_contract_module(contract_module_string)
    solidity_code = Solidity().compose(contract_module)
    return solidity_code
```