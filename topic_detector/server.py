from sanic import Sanic

from topic_detector.handlers import get_topic


def create_app():
    app = Sanic(__name__)
    app.add_route(get_topic, '/get_topic', methods=['GET'])

    return app


def main():
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)


if __name__ == "__main__":
    main()
