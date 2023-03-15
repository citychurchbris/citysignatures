import responder

api = responder.API()

themes = {
    'Purple': {
        'hex1': '#5A2D72',
        'hex2': '#000000',
        'logo': 'https://assets.citychurch.org.uk/signatures/cc_siglogo_purple.png',
    },
    'Blue': {
        'hex1': '#2158A8',
        'hex2': '#000000',
        'logo': 'https://assets.citychurch.org.uk/signatures/cc_siglogo_blue.png',
    },
    'Teal': {
        'hex1': '#4BBEAD',
        'hex2': '#000000',
        'logo': 'https://assets.citychurch.org.uk/signatures/cc_siglogo_teal.png',
    },
    'Red': {
        'hex1': '#E5264A',
        'hex2': '#000000',
        'logo': 'https://assets.citychurch.org.uk/signatures/cc_siglogo_red.png',
    },
    'Black': {
        'hex1': '#000000',
        'hex2': '#555555',
        'logo': 'https://assets.citychurch.org.uk/signatures/cc_siglogo_darkgrey.png',
    },
}


@api.route("/")
def index(req, resp):
    resp.content = api.template('index.html', themes=themes)


@api.route("/generate")
def generate(req, resp):
    theme = themes.get(req.params['theme'])
    resp.content = api.template(
        'signature.html', params=req.params, theme=theme)


if __name__ == "__main__":
    api.run(port=8080)
