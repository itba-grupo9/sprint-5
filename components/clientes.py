# TODO Chequear objetos creados en las clases hijas
# TODO Chequear si el dolar blue esta bien elegir para la compra


class Clientes:
	def __init__(self, nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais):
		
		# Datos del usuario
		self.nombre = nombre
		self.apellido = apellido
		self.numero = numero
		self.dni = dni
		
		# Direccion del cliente
		self.direccion = f"{calle} {numero_calle}, {ciudad}, {provincia}, {pais}."
		self.calle = calle
		self.numero_calle = numero_calle
		self.ciudad = ciudad
		self.provincia = provincia
		self.pais = pais
		
		# Propiedades de la cuenta
		self.tarjeta_debito = None
		self.cuenta_corriente = None
		self.cuenta_corriente_descubierto = None
		self.caja_de_ahorro_pesos = None
		self.caja_de_ahorro_dolares = None
		self.tarjeta_credito = None
		self.limite_cantidad_tc = None
		self.limite_extraccion = None
		self.limite_transf_sin_aviso = None
		self.limite_chequeras = None
		self.comision_transferencias = None
	
	
	@staticmethod
	def __cotizar_dolar():
		"""Devuelve el valor del dolar blue traido de una API """
		import requests
		try:
			return float(requests.get("https://api.bluelytics.com.ar/v2/latest").json()['blue']['value_buy'])
		
		except requests.exceptions.ConnectionError as err:
			raise f"Hubo un error en la conexion: \n{err}"
		
		except requests.exceptions.HTTPError as err:
			raise f"Hubo un error en la peticion: \n{err}"
		
		except requests.exceptions.Timeout as err:
			raise f"Hubo un error en el tiempo de respuesta: \n{err}"
		
		except requests.exceptions.TooManyRedirects as err:
			raise f"Hubo un error en la cantidad de redirecciones. Espere unos momentos por favor. \n{err}"
	# TODO revisar metodo cotizacion
	def puede_crear_chequera(self):
		return True if self.limite_chequeras else False
	
	def puede_crear_tarjeta_credito(self):
		return True if self.tarjeta_credito else False
	
	def puede_comprar_dolares(self):
		return True if self.caja_de_ahorro_dolares == 0 else False
	
	def retiro_efectivo_cajero_automatico(self, cantidad_a_retirar):
		"""Revisa si el usuario dispone saldo en cuenta corriente y caja de ahorro y realiza los retiros por cajero"""
	
		# Condiciones
		# No supere el monto permitido de extraccion
		if cantidad_a_retirar > self.limite_extraccion:
			return f"El monto de retiro no puede superar el limite de extraccion. Su limite de extraccion es de ${self.limite_extraccion} y esta intentando " \
			       f"retirar ${cantidad_a_retirar}."
		# No supere el giro descubierto
		if (self.caja_de_ahorro_pesos - cantidad_a_retirar) < -self.cuenta_corriente_descubierto:
			return f"No es posible realizar el retiro, ya que su giro en descubierto tiene un limite de {self.cuenta_corriente_descubierto}."
		
		# Funcion a ejecutar
		self.caja_de_ahorro_pesos -= cantidad_a_retirar
		print(f"La cantidad reditarda es de {cantidad_a_retirar}, el saldo de la caja de ahorro es de {self.caja_de_ahorro_pesos}")
	
	def alta_tarjeta_credito(self):
		"""Revisa si el usuario puede dar de alta una tarjeta de credito y si cumple con los requisitos la crea"""
		
		if not self.limite_cantidad_tc: return f"No es posible asignarle una tarjeta de credito a {self.apellido}"
		
		self.limite_cantidad_tc -= 1
		return f"La tarjeta de credito de {self.nombre} {self.apellido} fue creada perfectamente. Tarjetas restantes: {self.limite_cantidad_tc}."
	
	def alta_chequera(self):
		"""Revisa si el usuario puede crear una chequera y si cumple los requisitos la crea"""
		
		if not self.puede_crear_chequera(): return f"No es posible asignarle una chequera a {self.apellido}."
		
		self.limite_chequeras -= 1
		return f"La chequera de {self.nombre} {self.apellido} fue creada correctamente. Chequeras restantes: {self.limite_chequeras}."
	
	def comprar_dolar(self, cantidad_dolar):
		"""Revisa si el usuario tiene saldo disponible y realiza la compra de dolares"""
		
		if not self.puede_comprar_dolares(): return f"No es posible que el usuario {self.nombre} realice una compra de dolares."
		
		# Cotizo el dolar y calculo si puedo hacer el pago
		valor_dolar = (self.__cotizar_dolar())
		total_a_pagar_pesos = valor_dolar * cantidad_dolar
		
		if total_a_pagar_pesos > self.caja_de_ahorro_pesos:
			return f"No hay saldo suficiente para comprar esa cantidad de dolares. Su saldo actual es de {self.caja_de_ahorro_pesos}"
		
		# Realizo la compra
		self.caja_de_ahorro_pesos -= total_a_pagar_pesos
		self.caja_de_ahorro_dolares += cantidad_dolar
	
	# TODO chequear si se puede girar en descubierto para comprar dolares
	# TODO consultar si se puede comprar solo desde la caja de ahorro o tambien si se puede cuenta corriente
	
	def transferencia_enviada(self, cantidad, usuario):
		from django.core.exceptions import ObjectDoesNotExist
		
		costo_de_transferencia = cantidad + cantidad * self.comision_transferencias
		# Chequeo
		# Saldo disponible
		if costo_de_transferencia > (self.caja_de_ahorro_pesos + self.cuenta_corriente):
			return "No cuenta con el saldo disponible para hacer la transaccion en su caja de ahorro"
		
		# TODO chequear maximo a transferir
		
		try:
			usuario.cuenta_corriente += cantidad
			self.caja_de_ahorro_pesos -= costo_de_transferencia
		except ObjectDoesNotExist: # TODO Revisar excepciones
			raise "El usuario al que le quieres transferir no se encuentra registrado."
		
		# TODO realizar calculos para eliminar el saldo de la cuenta indicada
		# TODO revisar como hacer que el usuario elija si el pago lo hace con caja de ahorro o cuenta corriente.
		

	def transferencia_recibida(self, cantidad, usuario):
		pass # TODO crear metodo

class Classic(Clientes):
	def __init__(self, nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais):
		super().__init__(nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais)
		self.tarjeta_debito = True
		self.cuenta_corriente = 0
		self.cuenta_corriente_descubierto = 0
		self.caja_de_ahorro_pesos = 0
		self.caja_de_ahorro_dolares = None
		self.tarjeta_credito = None
		self.limite_cantidad_tc = 0
		self.limite_extraccion = 10000
		self.limite_transf_sin_aviso = 150000
		self.limite_chequeras = None
		self.comision_transferencias = 0.01


class Gold(Clientes):
	def __init__(self, nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais):
		super().__init__(nombre, apellido, numero, dni, calle, numero_calle, ciudad, provincia, pais)
		self.tarjeta_debito = True
		self.cuenta_corriente = 0
		self.cuenta_corriente_descubierto = -10000
		self.caja_de_ahorro_pesos = 0
		self.caja_de_ahorro_dolares = 0
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
		self.cuenta_corriente = 0
		self.cuenta_corriente_descubierto = -10000
		self.caja_de_ahorro_pesos = 0
		self.caja_de_ahorro_dolares = 0
		self.tarjeta_credito = True
		self.limite_cantidad_tc = 5
		self.limite_extraccion = 100000
		# self.limite_transf_sin_aviso = // TODO revisar como hacerlo infinito
		self.limite_chequeras = 2
		self.comision_transferencias = 0
