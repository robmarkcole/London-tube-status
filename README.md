[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![PyPI Version](https://img.shields.io/pypi/v/London-tube-status.svg)](https://pypi.org/project/London-tube-status/)


# London-tube-status
Python module for parsing the London tube data from [TFL](https://api.tfl.gov.uk/line/mode/tube,overground,dlr,tflrail/status) into a dictionary. No API key is required. Install from pypi with `pip install london-tube-status`

## Usage
```python
from london_tube_status import TubeData

tube_data = TubeData()

tube_data.update()

tube_data.data


    {'Bakerloo': {'Description': 'Nothing to report', 'State': 'Good Service'},
     'Central': {'Description': 'Nothing to report', 'State': 'Good Service'},
     'Circle': {'Description': 'Nothing to report', 'State': 'Good Service'},
     'DLR': {'Description': "DLR: New Year's Eve, Monday 31 December. A special "
                            'all-night service will operate. Trains will run every '
                            '15 minutes on all routes from 00:30 until 08:00 on '
                            "New Year's Day",
             'State': 'Special Service'},
     'District': {'Description': 'DISTRICT LINE: Monday 31 December, and New '
                                 "Year's Day 1 January, no service between Earls "
                                 'Court and Kensington Olympia',
                  'State': 'Part Closure'},
     'Hammersmith & City': {'Description': 'Nothing to report',
                            'State': 'Good Service'},
     'Jubilee': {'Description': 'Nothing to report', 'State': 'Good Service'},
     'London Overground': {'Description': 'LONDON OVERGROUND: Thursday 27 December '
                                          'to Tuesday 1 January, amended service '
                                          'between Liverpool Street and Chingford, '
                                          'trains will run every 20 minutes, not '
                                          'stopping at Bethnal Green, Hackney '
                                          'Downs or Clapton. *** LONDON '
                                          'OVERGROUND: Friday 28 December to '
                                          'Tuesday 1 January, no service between '
                                          'Edmonton Green and Cheshunt, please use '
                                          'local bus services or services from '
                                          'Ponders End, Brimsdown, Enfield Lock or '
                                          'Waltham Cross, or Greater Anglia '
                                          'services between Liverpool Street and '
                                          'Waltham Cross/Cheshunt via Tottenham '
                                          'Hale, instead. *** LONDON OVERGROUND: '
                                          'Thursday 27 December to Tuesday 1 '
                                          'January, amended service between '
                                          'Liverpool Street and Enfield Town - '
                                          'trains will run every 20 minutes, not '
                                          'stopping at Bethnal Green, Cambridge '
                                          'Heath, London Fields or Hackney Downs. '
                                          '*** LONDON OVERGROUND: Sunday 23 '
                                          'December to Tuesday 1 January, no '
                                          'service between Romford and Upminster. '
                                          'Use local London Buses routes 165 248 '
                                          'and 370 instead. *** LONDON OVERGROUND: '
                                          'Saturday 29 December to Tuesday 1 '
                                          'January, no service between South '
                                          'Tottenham and Barking. Replacement '
                                          'buses operate between Walthamstow '
                                          'Central and Barking. Supplementary '
                                          'buses will operate between Gospel Oak '
                                          'and South Tottenham on Saturday and '
                                          'Sunday.',
                           'State': 'Part Closure'},
     'Metropolitan': {'Description': 'Nothing to report', 'State': 'Good Service'},
     'Northern': {'Description': 'Nothing to report', 'State': 'Good Service'},
     'Piccadilly': {'Description': 'PICCADILLY LINE: Monday 31 December, no '
                                   'service between Rayners Lane and Uxbridge. '
                                   'Please use the Metropolitan line instead.',
                    'State': 'Part Closure'},
     'TfL Rail': {'Description': 'TFL RAIL: Monday 31 December, a reduced 30 '
                                 'minute service will operate between Paddington '
                                 'and Hayes & Harlington. Train will not stop at '
                                 'Acton Main Line, West Ealing or Hanwell. *** TFL '
                                 'RAIL: Friday 28, Saturday 29, Sunday 30, Monday '
                                 '31 December and Tuesday 1 January, no service '
                                 'between Liverpool Street and Romford. '
                                 'Replacement buses operate between Stratford / '
                                 'Newbury Park and Romford.',
                  'State': 'Part Closure + Reduced Service'},
     'Victoria': {'Description': 'Nothing to report', 'State': 'Good Service'},
     'Waterloo & City': {'Description': 'Nothing to report',
                         'State': 'Good Service'}}


tube_data.last_updated

    '2018-12-31 08:40:04'
```

