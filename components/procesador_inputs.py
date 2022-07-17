class ProcesadorDeInputs:
	def __init__(self, data_input):
		self.tipo = data_input["cuenta"]
		self.nombre = data_input['nombre']
		self.apellido = data_input['apellido']
		self.numero = data_input['numero']
		self.dni = data_input['dni']
		
		# Direccion
		self.calle = data_input["direccion"]["calle"]
		self.numero = data_input["direccion"]["numero"]
		self.ciudad = data_input['direccion']["ciudad"]
		self.provincia = data_input["direccion"]["provincia"]
		self.pais = data_input["direccion"]["pais"]
		
		# Transacciones
		self.estado = data_input["transacciones"][0]["estado"]
		self.tipo_de_transaccion = data_input["transacciones"][0]["cuenta"]
		self.cuenta_numero = data_input["transacciones"][0]["cuentaNumero"]
		self.cupo_diario_restante = data_input["transacciones"][0]["cupoDiarioRestante"]
		self.cantidad_extracciones_hechas = data_input["transacciones"][0]["cantidadExtraccionesHechas"]
		self.monto = data_input["transacciones"][0]["monto"]
		self.fecha = data_input['transacciones'][0]["fecha"]
		self.numero = data_input['transacciones'][0]["numero"]
		self.saldo_en_cuenta = data_input["transacciones"][0]["saldoEnCuenta"]
		self.total_tarjetas_de_credito_actualmente = data_input["transacciones"][0]["totalTarjetasDeCreditoActualmente"]
		self.total_chequeras_actualmente = data_input["transacciones"][0]["totalChequerasActualmente"]
