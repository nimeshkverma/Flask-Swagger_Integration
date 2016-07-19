#!flask/bin/python
from app import app
import connexion

if __name__ == "__main__":
	app = connexion.App(__name__, 9090)
	app.add_api('helloworld-api.yml')
	app.run()
