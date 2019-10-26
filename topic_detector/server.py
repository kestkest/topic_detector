from argparse import ArgumentParser
from sanic import Sanic

from topic_detector.handlers import get_topic


def create_app():
    app = Sanic(__name__)
    app.add_route(get_topic, '/get_topic', methods=['GET'])

    return app


def main():
    parser = ArgumentParser()
    parser.add_argument('--port', type=int, help='specify arbitrary port')
    port = parser.parse_args().port or 8000

    app = create_app()
    app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == "__main__":
    main()
