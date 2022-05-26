[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPI Version](https://img.shields.io/pypi/v/London-tube-status.svg)](https://pypi.org/project/London-tube-status/)

# London-tube-status
Python module for parsing the London tube data from [TFL](https://api.tfl.gov.uk/line/mode/tube,overground,dlr,tflrail/status) into a dictionary. No API key is required. Install from pypi with `pip install london-tube-status`

Returned data (see `usage.ipynb`): 
```
    {'Bakerloo': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'Central': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'Circle': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'DLR': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'District': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'Elizabeth line': {'Description': 'ELIZABETH LINE: Services between '
                                    'Paddington and Abbey Wood operate on '
                                    'Monday to Saturday only, between 0630 and '
                                    '2300.',
                        'State': 'Part Closure'},
    'Hammersmith & City': {'Description': 'Nothing to report',
                            'State': 'Good Service'},
    'Jubilee': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'London Overground': {'Description': 'Nothing to report',
                        'State': 'Good Service'},
    'Metropolitan': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'Northern': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'Piccadilly': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'TfL Rail': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'Victoria': {'Description': 'Nothing to report', 'State': 'Good Service'},
    'Waterloo & City': {'Description': 'Nothing to report',
                        'State': 'Good Service'}}
```

## Development
* Create venv -> `python3 -m venv venv`
* Use venv -> `source venv/bin/activate`
* `pip3 install -e .` and `pip3 install -r requirements-dev.txt`
* Run tests with `venv/bin/pytest tests/*`
* Black format with `venv/bin/black .`
* To run the jupyter notebook `pip3 install jupyter` and `venv/bin/jupyter lab.` or just run the notebook in vscode