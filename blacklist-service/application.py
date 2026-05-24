import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

from app import create_app

application = newrelic.agent.WSGIApplicationWrapper(create_app())

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
