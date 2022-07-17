from components.clientes import *
from components.procesador_inputs import *
from components.error_checker import ErrorChecker
from flask import Flask, render_template
import requests
import json

# ----------------- API ----------------
url = "https://learn-us-east-1-prod-fleet01-xythos.content.blackboardcdn.com/blackboard.learn.xythos.prod/5a31a0302d72d/6789219?X-Blackboard-Expiration=1658102400000&X-Blackboard-Signature=r2Ew0wr12pq1LTLs1lQnMYX4NeaM2r04PlfLGI0BSFg%3D&X-Blackboard-Client-Id=525986&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27eventos_classic.json&response-content-type=application%2Fjson&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQC3kbB0gT2GXqdfaT6x%2FMtnsxf1rUJtpIDxuWjLrGN1%2FQIgWyMyPnIjH%2FmMB%2B%2FPB591Z9WyDFqvwA6SpPyqoAmYf7oq3AQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw1NTY5MDM4NjEzNjEiDF2Vf%2B2z6BeClzqZGSqwBGHxjln9R%2FZqXG3HodGXfwS8AvJpJSW5miRpjAN01OWZtoP2s8pqrva1%2BzjJQH%2F5uhCw4H%2BxLE7nJTJWya3yhgGdYf6%2FPTkTqLJqWMJcvqT%2FRQRdnKNX8qnoCBlcVrXuAesw2yS%2BSe9IP8Jye6sSCsw4uEZAjQrqBA%2BDvsnrXe%2BJxVnNdTDT%2BkXXH4qeIwmY7p9pAtXU1fcTnNs%2BU5ckP070%2B9Z4cRDVHC%2F7E4l3FI7oDcwuKPDt2JUUdQbYr4psx2ga8WBwuPuS%2FfuT%2Bj3lxrCpaIMucTgzN9Qf6dmD6kF5R9dtuhQzTp4Cg5dBT9lkw%2BInh2sY0RIMVqte4r7%2Fll28ZCfcYdOYrzLQKPJg6%2BG5UE8FYCWrb9I9lzuZCV2qy6yXEIj6%2BQpsElXynednOu8nkMCHCVietJwqLkqyr6CWvBUGtg2jVNtheeaQ5EFZOy3LgB8zYdstg0W5QU4AEvAI1nSXJ%2BC06Hd%2F2Dmd8Mu1RdURN%2FNQZBTVI2A1J7wO61Xz0NFIn4r7fDqscPoWUJ8ULFe57NmXKR9rcOPJkpg3ekgMdm7SLbjrl%2BiZbPsnEgztgAu4m9W79dOWjrHQmmrHTzyEWvm0q5AnBCzuC3vzHWALifJ8WsN4cijb31%2BuZw80ySVO4gbRbk3Ofa7%2Fi2nOeOz%2FDjCaswWME1aeZWnnOO6kerX4fA8vWXwnci%2BKyVIN218tITnJowEECP2%2FiQFUDqJSu4yaIL%2FQ239O21LLMNnE0ZYGOqkBW1ordoUjtBtvAzmsJ1izFGp6ROiWoaQW8WfyVrUmCPfo8Zmp8qMT2KYWppazP%2BxifsLiSkGQic8WTnrpHqU00y%2B97MKbiz%2B8D4VGAxiUNz5ea3BQ0Z%2FJ44kybZ7WYNvfEipf4n%2Fc6w8RPQ0uHECpJ7it8eIWftOXbl%2B3%2BeHaCSc%2FT%2B%2Bj7MW7tFYK1X8ZLgmSGCk0kbTInJ%2B3jdmGiSDScdOwKtXEhjPYRA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220717T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIAYDKQORRYUZWV2OHI%2F20220717%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=93f0a7c0af16e127b59abc5c888279be9ca78bf1fa96c092c5966832356ca710"
resp = requests.get(url)
data = resp.json()


class App:
	def __init__(self, data_a_procesar):
		self.usuario = ProcesadorDeInputs(data_a_procesar)
		self.tipo_de_cuenta = Clientes.crear_tipo_de_cuenta(self.usuario)
		self.error_checker = ErrorChecker(self.usuario, self.tipo_de_cuenta).error_checker()
	
	def __str__(self):
		return self.error_checker


# ----------------------------------------- FLASK -------------------------------------------------------------------------
app = App(data)
flask = Flask(__name__)


@flask.route('/')
def hello():
	return render_template('index.html', app=app)


if __name__ == "__main__":
	flask.run(debug=True)
