[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPI Version](https://img.shields.io/pypi/v/London-tube-status.svg)](https://pypi.org/project/London-tube-status/)

# London-tube-status
Python module for parsing the London tube data from [TFL](https://api.tfl.gov.uk/line/mode/tube,overground,dlr,elizabeth-line/status) into a dictionary. No API key is required. Install from pypi with `pip install london-tube-status`

Returned data (see `usage.ipynb`): 
```
'2022-05-26 04:09:58'
{'Bakerloo': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Central': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Circle': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'DLR': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'District': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Elizabeth line': {'Description': 'Minor delays between Hayes & Harlington '
                                   'and Reading due to an earlier trespasser '
                                   'at Slough. GOOD SERVICE on the rest of the '
                                   'line. ',
                    'State': 'Minor Delays'},
 'Hammersmith & City': {'Description': 'Nothing to report',
                        'State': 'Good Service'},
 'Jubilee': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Liberty': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Lioness': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Metropolitan': {'Description': 'Metropolitan Line: Minor delays due to an '
                                 'earlier faulty train at Finchley road. ',
                  'State': 'Minor Delays'},
 'Mildmay': {'Description': 'London Overground: Severe delays between '
                            'Willesden Junction and Clapham Junction due to an '
                            'earlier points failure at Shepherds Bush. GOOD '
                            'SERVICE on the rest of the line. ',
             'State': 'Severe Delays'},
 'Northern': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Piccadilly': {'Description': 'PICCADILLY LINE: No service between Rayners '
                               'Lane and Uxbridge due to poor rail conditions '
                               'caused by significant leaf fall. *** '
                               'Piccadilly Line: No service between Rayners '
                               'Lane and Uxbridge due to difficult track '
                               'conditions caused by significant leaf fall. '
                               'MINOR DELAYS between Acton town and Rayners '
                               'Lane due to shortage of trains GOOD SERVICE on '
                               'the rest of the line ',
                'State': 'Minor Delays + Part Closure'},
 'Suffragette': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Victoria': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Waterloo & City': {'Description': 'Nothing to report',
                     'State': 'Good Service'},
 'Weaver': {'Description': 'Nothing to report', 'State': 'Good Service'},
 'Windrush': {'Description': 'Nothing to report', 'State': 'Good Service'}}
```

## Development
* Create venv -> `python3 -m venv venv`
* Use venv -> `source venv/bin/activate`
* `pip3 install -e .` and `pip3 install -r requirements-dev.txt`
* Run tests with `venv/bin/pytest tests/*`
* Black format with `venv/bin/black .`
* To run the jupyter notebook `pip3 install jupyter` and `venv/bin/jupyter lab.` or just run the notebook in vscode
