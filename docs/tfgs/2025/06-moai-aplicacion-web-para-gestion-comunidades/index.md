# Moai: aplicación web para la gestión de comunidades de vecinos

## Información General

<div class="tfg-resources">
<a href="2024-25-ETSII-A-2033-2033037-m.delgado.2019-MEMORIA.pdf" class="btn-pdf btn-small">Memoria PDF</a>
<a href="https://github.com/migueld7/gestor_de_comunidades" class="btn-github btn-small">GitHub</a>
</div>
**Autor/a:** Miguel Delgado Amador  
**Grado:** Grado En Ingeniería Informática  
**Tutor:** Michel Maes Bermejo  
**Fecha de defensa:** junio de 2025

## Resumen

Este proyecto consiste en el desarrollo de una aplicación web práctica y robusta diseñada para mejorar y simplificar la gestión de comunidades de propietarios, tanto para los vecinos como para los administradores. La herramienta ofrece funcionalidades que simplifican para el administrador la gestión de elementos tales como inmuebles, vecinos o recibos. Además, facilita a los propietarios la visualización y la actualización de toda la información de su interés.
La aplicación se ha desarrollado siguiendo una arquitectura de tres capas bien
definidas: Presentación, Aplicación y Persistencia. Esta estructura modular per-
mite una separación clara de responsabilidades, lo que facilita el mantenimiento
del sistema y mejora su rendimiento. La capa de Presentación se encarga de la
interacción con el usuario a través de una interfaz web construida con tecnologías
como Vue.js, HTML y CSS. Por su parte, la capa de Aplicación implementa la
lógica de negocio utilizando Java y el framework Spring Boot, gestionando la
coordinación entre los distintos componentes del sistema. Finalmente, la capa
de Persistencia se ocupa del acceso a los datos almacenados en una base de da-
tos MySQL, apoyándose en Hibernate y Spring Data JPA para garantizar una
comunicación eficiente y segura con el sistema de almacenamiento.
El proyecto incorpora una estrategia de pruebas completa, que abarca tanto
pruebas unitarias como pruebas de sistema. Para ello, se han utilizado herra-
mientas como JUnit 5 y REST Assured en la validación de la lógica de negocio,
asegurando que los componentes individuales funcionen correctamente. Además,
se han empleado pruebas de sistema con Selenium para verificar que las funcio-
nalidades de la aplicación se comportan adecuadamente en escenarios reales.
Para gestionar el desarrollo del proyecto se ha seguido un flujo de trabajo
basado en una variante simplificada de la metodología Git Flow. Además, se han
integrado prácticas de DevOps mediante la automatización del proceso de integración y entrega continua con GitHub Actions. Este sistema automatizado se
encarga de ejecutar pruebas, generar versiones del proyecto con etiquetas temporales y realizar el despliegue en Microsoft Azure, utilizando para ello contenedores
Docker desplegados en Instancias de Contenedor de Azure.
Por último, se reflexiona acerca de los resultados en las conclusiones, y se
exponen algunas ideas de mejora de cara a posibles trabajos futuros.
