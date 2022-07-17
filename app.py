from components.clientes import *
from components.procesador_inputs import *
from components.error_checker import ErrorChecker

data = {
	"numero": 100001,
	"nombre": "Nicolas",
	"apellido": "Gaston",
	"dni": "29494777",
	"cuenta": "BLACK",
	"direccion": {
		"calle": "Rivadavia",
		"numero": "7900",
		"ciudad": "Capital Federal",
		"provincia": "Buenos Aires",
		"pais": "Argentina"
		},
	"transacciones": [{
		"estado": "RECHAZADA",
		"cuenta": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
		"cuentaNumero": 190,
		"cupoDiarioRestante": 9000,
		"cantidadExtraccionesHechas": 1,
		"monto": 100000000,
		"fecha": "06/06/2022 10:00:55",
		"numero": 1,
		"saldoEnCuenta": 100000,
		"totalTarjetasDeCreditoActualmente": 5,
		"totalChequerasActualmente": 2
		}]
	}


class App:
	def __init__(self, data_a_procesar):
		self.usuario = ProcesadorDeInputs(data_a_procesar)
		self.tipo_de_cuenta = Clientes.crear_tipo_de_cuenta(self.usuario)
		self.error_checker = ErrorChecker(self.usuario, self.tipo_de_cuenta).error_checker()
	
	def __str__(self):
		return f"""
		<p>La cuenta del usuario {self.usuario.nombre} {self.usuario.apellido} fue {self.usuario.estado}.</p>
		<p>{self.error_checker}</p>"""


app = App(data)

print(app)
