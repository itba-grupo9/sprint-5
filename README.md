# sprint-5
# Proyecto
Realizamos el proyecto de acuerdo a los requisitos de la consigna: utilizando POO, tomando como referencia (pero adaptado a nuestro proyecto) el diagrama de 
clases.
Tambien utilizamos el microframework Flask para generar el HTML en solo unas pocas lineas de codigo. Tambien utilizamos el sistema de plantillas Jinja2 para
mostrar al usuario la informacion requerida de manera estilizada.   



## App
La aplicacion genera un usuario con la informacion brindada por la API, generando un tipo de cuenta para ese usuario de acuerdo al tipo de cliente que sea y 
controlando si existe un error en la transaccion. En caso de que el error exista, informa al usuario la razon por la que se produce ese error a traves de HTML.

### Procesador de inputs
Se encarga de  obtener toda la informacion del cliente y sus transacciones del JSON.

### Error Checker
Una vez obtenida la informacion del usuario y sus transacciones, chequea que tipo de error existe para devolverlo al usuario (si existe uno).

### Flask y Templates
Renderiza el HTML con la informacion brindada por la App de forma estilizada para ser amigable al usuario.