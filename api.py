import responder

api = responder.API()


@api.route("/")
def index(req, resp):
    resp.content = api.template('index.html')


@api.route("/generate")
def generate(req, resp):
    resp.content = api.template('signature.html', params=req.params)


if __name__ == "__main__":
    api.run()
