# watchman.flask

A python/flask based monitor service/web app to tell if stuff is behaving

## Getting Started

### Clone the project

### Install Requirements

    pip install -r requirements.txt

### Modify watchlist within runserver.py

    watchlist = [
        {
            'service': 'Service with Authentication',
            'headers': {
                'example-api-key': 'xxxxxxx',
                'example-authtoken': 'xxxxxxx',
            },
            'urls': [
                {'url': 'https://domain.com/endpoint/method1'},
                {'url': 'https://domain.com/endpoint/method2'},
            ]
        }, {
            'service': 'Service without Authentication',
            'urls': [
                {'url': 'http://domain.com/endpoint/method3'},
            ]
        },
    ]

### Run this sucka!
    python runserver.py
