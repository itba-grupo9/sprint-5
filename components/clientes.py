class Clientes:
	@staticmethod
	def crear_tipo_de_cuenta(usuario):
		if usuario.tipo == "BLACK":
			return Black()
		
		if usuario.tipo == "GOLD":
			return Gold()
		
		if usuario.tipo == "CLASSIC":
			return Classic()
	
	# TODO Revisar las funciones
	def puede_crear_chequera(self):
		return True if self.limite_chequeras > 0 else False
	
	def puede_crear_tarjeta_credito(self):
		return True if self.limite_tarjetas_credito > 0 else False
	
	def puede_comprar_dolares(self):
		return True if self.caja_de_ahorro_dolares else False
	
	def retiro_efectivo_cajero_automatico(self, cantidad_a_retirar):
		"""Revisa si el user dispone saldo en cuenta corriente y caja de ahorro y realiza los retiros por cajero"""
		
		# Condiciones
		# No supere el monto permitido de extraccion
		if cantidad_a_retirar > self.limite_extraccion:
			return f"El monto de retiro no puede superar el limite de extraccion. Su limite de extraccion es de ${self.limite_extraccion} y esta intentando " \
			       f"retirar ${cantidad_a_retirar}."
		# No supere el giro descubierto
		if (self.caja_de_ahorro_en_pesos - cantidad_a_retirar) < -self.cuenta_corriente_descubierto:
			return f"No es posible realizar el retiro, ya que su giro en descubierto tiene un limite de {self.cuenta_corriente_descubierto}."
		
		# Funcion a ejecutar
		self.caja_de_ahorro_en_pesos -= cantidad_a_retirar
		print(f"La cantidad reditarda es de {cantidad_a_retirar}, el saldo de la caja de ahorro es de {self.caja_de_ahorro_en_pesos}")
	
	def alta_tarjeta_credito(self):
		"""Revisa si el user puede dar de alta una tarjeta de credito y si cumple con los requisitos la crea"""
		
		if not self.limite_tarjetas_credito: return f"No es posible asignarle una tarjeta de credito."
		
		self.limite_tarjetas_credito -= 1
		return f"La tarjeta de credito fue creada perfectamente. Tarjetas restantes: {self.limite_tarjetas_credito}."
	
	def alta_chequera(self):
		"""Revisa si el user puede crear una chequera y si cumple los requisitos la crea"""
		
		if not self.puede_crear_chequera(): return f"No es posible asignarle una chequera."
		
		self.limite_chequeras -= 1
		return f"La chequera fue creada correctamente. Chequeras restantes: {self.limite_chequeras}."


class Classic(Clientes):
	def __init__(self):
		super().__init__()
		self.caja_de_ahorro_en_pesos = True
		self.caja_de_ahorro_en_dolares = False
		self.cuenta_corriente = False
		self.maximo_retiro = 10000
		self.limite_tarjetas_debito = 1
		self.limite_tarjetas_credito = 0
		self.limite_chequeras = 0
		self.limite_recibo_transferencia = 150000
		self.comision_transferencias = 0.01
		self.giro_descubierto = 0


class Gold(Clientes):
	def __init__(self):
		super().__init__()
		self.caja_de_ahorro_en_pesos = True
		self.caja_de_ahorro_en_dolares = True
		self.cuenta_corriente = True
		self.maximo_retiro = 20000
		self.limite_tarjetas_debito = 1
		self.limite_tarjetas_credito = 1
		self.limite_chequeras = 1
		self.limite_recibo_transferencias = 500000
		self.comision_transferencias = 0.005
		self.giro_descubierto = 10000


class Black(Clientes):
	def __init__(self):
		super().__init__()
		self.caja_de_ahorro_en_pesos = True
		self.caja_de_ahorro_en_dolares = True
		self.cuenta_corriente = True
		self.maximo_retiro = 100000
		self.limite_tarjetas_debito = 1
		self.limite_tarjetas_credito = 5
		self.limite_chequeras = 2
		self.limite_recibo_transferencias = float('inf')
		self.comision_transferencias = 0
		self.giro_descubierto = 10000
