from components.clientes import *

data = {
	"numero": 100001,
	"nombre": "Nicolas",
	"apellido": "Gaston",
	"dni": "29494777",
	"tipo": "BLACK",
	"direccion": {
		"calle": "Rivadavia",
		"numero": "7900",
		"ciudad": "Capital Federal",
		"provincia": "Buenos Aires",
		"pais": "Argentina"
		},
	"transacciones": [{
		"estado": "ACEPTADA",
		"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
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
#
# def crear_tipo_cliente():
# 	if cuenta.tipo == "BLACK":
# 			return Black()
#
# 	if cuenta.tipo == "GOLD":
# 			return Gold()
#
# 	if cuenta.tipo == "CLASSIC":
# 			return Classic()
#
#
# class ErrorChecker:
# 	def __init__(self, cuenta):
# 		self.cuenta = cuenta
# 		self.chequeo_a_ejecutar()
#
# 	def chequeo_a_ejecutar(self):
# 		if cuenta.tipo_de_transaccion == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO": self.__chequeo_retiro_efectivo()
# 		if cuenta.tipo_de_transaccion == "ALTA_TARJETA_CREDITO": self.__chequeo_alta_tarjeta_credito()
# 		if cuenta.tipo_de_transaccion == "ALTA_CHEQUERA": self.__chequeo_alta_chequera()
# 		if cuenta.tipo_de_transaccion == "COMPRAR_DOLAR": self.__chequeo_compra_dolares()
# 		if cuenta.tipo_de_transaccion == "TRANSFERENCIA_ENVIADA": self.__chequeo_transferencia_enviada()
# 		if cuenta.tipo_de_transaccion == "TRANSFERENCIA_RECIBIDA": self.__chequeo_transferencia_recibida()
#
# 	# Errores posibles
#
# 	def __chequeo_retiro_efectivo(self):
# 		"""- Chequea que el monto a retirar no sea mayor al disponible.
# 		- Chequea que el monto a retirar no supere el limite de extraccion.
# 		"""
# 		if cuenta.monto > cuenta.saldo_en_cuenta:
# 			return "El monto que se quiere retirar es mayor al que dispone en sus cuentas"
# 		if cuenta.monto > tipo_de_cuenta.limite_extraccion:
# 			return f"Su tipo de cuenta no permite un retiro mayor a ${tipo_de_cuenta.limite_extraccion}."
#
# 		return True
#
# 	def __chequeo_alta_tarjeta_credito(self):
# 		"""- Chequea si el usuario puede crear una tarjeta de credito"""
# 		if cuenta.tipo == "CLASSIC":
# 			return "No es posible que los clientes Classic cuenten con tarjeta de credito. Por favor, actualicese a Gold o Black."
#
# 		if cuenta.total_tarjetas_de_credito_actualmente >= tipo_de_cuenta.limite_cantidad_tc:
# 			return f"No es posible crear una tarjeta de credito ya que alcanzo el limite."
#
# 		return True
#
# 	def __chequeo_alta_chequera(self):
# 		"""- Chequea si el usuario puede crear una chequera"""
# 		if cuenta.tipo == "CLASSIC":
# 			return "No es posible que los clientes Classic cuenten con una chequera. Por favor, actualicese a Gold o Black."
#
# 		if cuenta.total_tarjetas_de_credito_actualmente >= tipo_de_cuenta.limite_chequeras:
# 			return f"No es posible crear una cheuquera ya que alcanzo el limite."
#
# 		return True
#
# 	def __chequeo_compra_dolares(self):
# 		if cuenta.tipo == "Classic":
# 			return "No es posible que los usuarios Classic realicen una compra de dolares. Por favor actualicese a Gold o Black"
#
# 		return True
#
# 	def __chequeo_transferencia_enviada(self):
# 		if cuenta.monto + cuenta.monto * tipo_de_cuenta.comision_transferencias > cuenta.saldo_en_cuenta:
# 			return "No es posible realizar la transferencia. Fondos insuficientes."
#
# 	def __chequeo_transferencia_recibida(self):
# 		if cuenta.monto >= tipo_de_cuenta.limite_transf_sin_aviso:
# 			return "No es posible recibir la transferencia ya que excede el limite de transferencias por dia sin aviso."
#
#
# class ProcesadorDeInputs:
# 	def __init__(self, data_input):
# 		self.cliente = None
# 		self.tipo = data_input["tipo"]
# 		self.nombre = data_input['nombre']
# 		self.apellido = data_input['apellido']
# 		self.numero = data_input['numero']
# 		self.dni = data_input['dni']
#
# 		# Direccion
# 		self.calle = data_input["direccion"]["calle"]
# 		self.numero = data_input["direccion"]["numero"]
# 		self.ciudad = data_input['direccion']["ciudad"]
# 		self.provincia = data_input["direccion"]["provincia"]
# 		self.pais = data_input["direccion"]["pais"]
#
# 		# Transacciones
# 		self.estado = data_input["transacciones"][0]["estado"]
# 		self.tipo_de_transaccion = data_input["transacciones"][0]["tipo"]
# 		self.cuenta_numero = data_input["transacciones"][0]["cuentaNumero"]
# 		self.cupo_diario_restante = data_input["transacciones"][0]["cupoDiarioRestante"]
# 		self.cantidad_extracciones_hechas = data_input["transacciones"][0]["cantidadExtraccionesHechas"]
# 		self.monto = data_input["transacciones"][0]["monto"]
# 		self.fecha = data_input['transacciones'][0]["fecha"]
# 		self.numero = data_input['transacciones'][0]["numero"]
# 		self.saldo_en_cuenta = data_input["transacciones"][0]["saldoEnCuenta"]
# 		self.total_tarjetas_de_credito_actualmente = data_input["transacciones"][0]["totalTarjetasDeCreditoActualmente"]
# 		self.total_chequeras_actualmente = data_input["transacciones"][0]["totalChequerasActualmente"]
#

# # 1. Procesamos los datos del tipo_de_cuenta
# cuenta = ProcesadorDeInputs(data)
#
#
#
# # 2. Creamos el tipo de tipo_de_cuenta predefinido basado en los inputs de la cuenta
# tipo_de_cuenta = crear_tipo_cliente()
#
# print(tipo_de_cuenta.caja_de_ahorro_pesos)


# # 3. Chequeamos errores
# error_checker = ErrorChecker(cuenta)
# print(error_checker.chequeo_a_ejecutar())


# TODO Revisar giro en descubierto


cliente = Black()

print(cliente.puede_crear_chequera())
