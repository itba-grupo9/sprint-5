from components.clientes import Classic, Gold, Black




caruso_lombardi = Classic("Ricardo", "Caruso Lomabardi", 100, 23382734, "Hipoito Yrigoyen","1235", "Avellaneda", "Buenos Aires", "Argentina")

pachano = Gold("Anibal", "Pachano", 101, 19284293, "Alem", "1433", "Recoleta", "Buenos Aires", "Argentina")

ricardo_fort = Black("Ricardo", "Fort", 102, 29283927, "Ocean Drive", "1549", "Miami", "Florida", "USA")



#
#
#
# cliente.caja_de_ahorro_pesos = 5000
#
#
# print(cliente.retiro_efectivo_cajero_automatico(5001))



# Dando de alta tarjeta

# print(pachano.alta_tarjeta_credito())
# print(caruso_lombardi.alta_tarjeta_credito())


import requests
# Probando chequeras
# print(pachano.alta_chequera())
# print(pachano.alta_chequera())
# print(pachano.alta_chequera())
# print(caruso_lombardi.alta_chequera())


# Probando compra de dolares
pachano.caja_de_ahorro_pesos = 100000

pachano.comprar_dolar(200)

print(pachano.caja_de_ahorro_pesos)
print(pachano.caja_de_ahorro_dolares)



caruso_lombardi.caja_de_ahorro_pesos = 100000

print(caruso_lombardi.comprar_dolar(200))

print(caruso_lombardi.caja_de_ahorro_pesos)
print(caruso_lombardi.caja_de_ahorro_dolares)


# Probando transferencias

# pachano.caja_de_ahorro_pesos = 100000
#
# print(pachano.caja_de_ahorro_pesos)
#
# pachano.transferencia_enviada(20000, caruso_lombardi)
#
#
# print(caruso_lombardi.cuenta_corriente)
# print(pachano.caja_de_ahorro_pesos)





