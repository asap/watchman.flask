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
