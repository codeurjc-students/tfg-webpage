# OpenVPN4All: suite para la creación y gestión de un servidor VPN

## Información General

<div class="tfg-resources">
<a href="2022-23-ETSII-A-2059-2059037-a.berdote.2019-MEMORIA.pdf" class="btn-pdf btn-small">Memoria PDF</a>
<a href="https://github.com/SeXde/OVPN4ALL" class="btn-github btn-small">GitHub</a>
</div>
**Autor/a:** Álvaro Berdote Jiménez  
**Grado:** Grado En Ingeniería Informática  
**Tutor:** Michel Maes Bermejo  
**Fecha de defensa:** junio de 2023

## Resumen

OPENVPN4ALL es una aplicación web que permite crear un servidor VPN
de forma sencilla y sin tener conocimientos avanzados de networking ni de informática.
La idea inicial es hacer uso de openvpn y gestionar la configuración de
ficheros y certificados de forma automática mediante scripts, haciendo uso de
una interfaz gráfica facilitando así enormemente la tarea de crear un servidor
VPN a un usuario inexperto.
Esta herramienta puede ser muy útil para que usuarios no profesionales así
como pequeñas y medianas empresas que no se pueden permitir un router con
VPN incorporada o software de pago puedan disponer de un servidor totalmente
funcional y fácil de gestionar.
Para ello nuestro objetivo es construir una interfaz que permita crear un usua-
rio, poder generar un fichero de conexión para dicho usuario y poder eliminarlo.
También se quiere permitir editar y poder cambiar fácilmente la configuración
del servidor VPN así como disponer de un panel con información actualizada del
servidor.
La solución propuesta incluye, tras un análisis de las tecnologías disponibles,
las siguientes funcionalidades:
- Información en tiempo real del estado de la VPN y conexiones de usuarios.
- Lectura de logs del servidor en tiempo real.
- Gestión de usuarios con posibilidad de enviar el fichero de conexión por
email.
- Configuración del servidor VPN con auto relleno en algunos campos.
- Configuración del cliente de correo interno del servidor VPN para enviar
las conexiones de cliente.
- Desconexión y/o eliminación en tiempo real de usuarios.
- Descarga de logs del servidor.