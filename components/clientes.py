class Clientes:
	def __init__(self, nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais):
		self.nombre = nombre
		self.apellido = apellido
		self.numero = numero
		self.dni = dni
		
		# Direccion del cliente
		self.calle = calle
		self.numero_calle = numero_calle
		self.ciudad = ciudad
		self.provincia = provincia
		self.pais = pais
	
	def puede_crear_chequera(self):
		return True if self.limite_chequeras else False
	
	def puede_crear_tarjeta_credito(self):
		return True if self.tarjeta_credito else False


class Classic(Clientes):
	def __init__(self, nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais):
		super().__init__(nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais)
		self.tarjeta_debito = True
		self.cuenta_corriente = None
		self.cuenta_corriente_descubierto = None
		self.caja_de_ahorro_dolares = None
		self.tarjeta_credito = None
		self.limite_tarjeta_credito = None
		self.limite_extraccion = 10000
		self.limite_transf_sin_aviso = 150000
		self.limite_chequeras = None
		self.comision_transferencias = 0.01


class Gold(Clientes):
	def __init__(self, nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais):
		super().__init__(nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais)
		self.tarjeta_debito = True
		self.cuenta_corriente = True
		self.cuenta_corriente_descubierto = -10000
		self.caja_de_ahorro_dolares = True
		self.tarjeta_credito = True
		self.limite_cantidad_tc = 1
		self.limite_extraccion = 20000
		self.limite_transf_sin_aviso = 500000
		self.limite_chequeras = 1
		self.comision_transferencias = 0.005


class Black(Clientes):
	def __init__(self, nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais):
		super().__init__(nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais)
		self.tarjeta_debito = True
		self.cuenta_corriente = True
		self.cuenta_corriente_descubierto = -10000
		self.caja_de_ahorro_dolares = True
		self.tarjeta_credito = True
		self.limite_cantidad_tc = 5
		self.limite_extraccion = 100000
		# self.limite_transf_sin_aviso =
		self.limite_chequeras = 2
		self.comision_transferencias = 0
