class ErrorChecker:
	def __init__(self, cuenta, tipo):
		self.cuenta = cuenta
		self.tipo = tipo
	
	# Private functions ----------------
	def __chequeo_retiro_efectivo(self):
		if self.cuenta.monto > self.cuenta.saldo_en_cuenta:
			return "El monto que se quiere retirar es mayor al que dispone en sus cuentas"
		if self.cuenta.monto > self.tipo.maximo_retiro:
			return f"Su cuenta de cuenta no permite un retiro mayor a ${self.tipo.maximo_retiro}."
		
		return True
	
	def __chequeo_alta_tarjeta(self):
		if self.cuenta.tipo_de_transaccion == "ALTA_TARJETA_CREDITO":
			if self.cuenta.cuenta == "CLASSIC":
				return "No es posible que los clientes Classic cuenten con tarjeta de credito. Por favor, actualicese a Gold o Black."
			if self.cuenta.total_tarjetas_de_credito_actualmente >= self.tipo.limite_tarjetas_credito:
				return f"No es posible crear una tarjeta de credito ya que alcanzo el limite."
			return True
	
	def __chequeo_alta_chequera(self):
		if self.cuenta.cuenta == "CLASSIC":
			return "No es posible que los clientes Classic cuenten con una chequera. Por favor, actualicese a Gold o Black."
		
		if self.cuenta.total_chequeras_actualmente >= self.tipo.limite_chequeras:
			return f"No es posible crear una cheuquera ya que alcanzo el limite."
		
		return True
	
	def __chequeo_comprar_dolar(self):
		if self.cuenta.cuenta == "CLASSIC":
			return "No es posible que los usuarios Classic realicen una compra de dolares. Por favor actualicese a Gold o Black"
		
		return True
	
	def __chequeo_transferencia_enviada(self):
		if self.cuenta.monto + self.cuenta.monto * self.tipo.comision_transferencias > self.cuenta.saldo_en_cuenta:
			return "No es posible realizar la transferencia. Fondos insuficientes."
		return True
	
	def __chequeo_transferencia_recibida(self):
		if self.cuenta.monto >= self.tipo.limite_recibo_transferencias:
			return "No es posible recibir la transferencia ya que excede el limite de transferencias por dia sin aviso."
		return True
	
	# Public functions
	def error_checker(self):
		if self.cuenta.estado == "ACEPTADA": return "No existe un error en la transaccion."
		if self.cuenta.tipo_de_transaccion == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO": self.__chequeo_retiro_efectivo()
		if self.cuenta.tipo_de_transaccion == "ALTA_TARJETA_CREDITO": self.__chequeo_alta_tarjeta()
		if self.cuenta.tipo_de_transaccion == "ALTA_CHEQUERA": self.__chequeo_alta_chequera()
		if self.cuenta.tipo_de_transaccion == "COMPRAR_DOLAR": self.__chequeo_comprar_dolar()
		if self.cuenta.tipo_de_transaccion == "TRANSFERENCIA_ENVIADA": self.__chequeo_transferencia_enviada()
		if self.cuenta.tipo_de_transaccion == "TRANSFERENCIA_RECIBIDA": self.__chequeo_transferencia_recibida()
		else: return "No es posible detectar el error. Por favor comuniquese con nuestra sucursal mas cercana."
