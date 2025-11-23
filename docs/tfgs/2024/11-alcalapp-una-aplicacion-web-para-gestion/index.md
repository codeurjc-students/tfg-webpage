# Alcalapp: una aplicación web para la gestión de tareas e incidencias en equipos de desarrollo

## Información General

<div class="tfg-resources">
<a href="2024-25-ETSII-A-2059-2059037-es.alcala.2019-MEMORIA.pdf" class="btn-pdf btn-small">Memoria PDF</a>
<a href="https://github.com/elisaalcala/alcalapp" class="btn-github btn-small">GitHub</a>
</div>
**Autor/a:** Elisa Sofía Alcalá Guerrero  
**Grado:** Grado En Ingeniería Informática  
**Tutor:** Michel Maes Bermejo  
**Fecha de defensa:** noviembre de 2024

## Resumen

Este proyecto se centra en el desarrollo de una aplicaci´on web robusta y funcio-
nal dise˜nada para optimizar la gesti´on de tareas y mejorar la din´amica de trabajo
en equipos de desarrollo tecnol´ogico. La herramienta ofrece funcionalidades que
simplifican la visualizaci´on, asignaci´on, seguimiento y resoluci´on de tareas, fo-
mentando la transparencia y la colaboraci´on entre los miembros del equipo. Para
lograr estos objetivos, se implementa un sistema de tickets que centraliza la ges-
ti´on de releases, proyectos e incidencias, facilitando su organizaci´on y trazabilidad
en todo momento.
Se ha implementado una arquitectura de tres capas (Presentaci´on, Aplica-
ci´on y Persistencia) para organizar las responsabilidades del sistema, facilitar su
mantenimiento y optimizar su rendimiento. La capa de Presentaci´on gestiona la
interfaz de usuario con tecnolog´ıas como JavaScript, HTML y CSS; la de Apli-
caci´on coordina la l´ogica de negocio con tecnolog´ıas como Java, Spring Boot,
Maven; y la de Persistencia asegura una comunicaci´on eficiente con la base de
datos MySQL mediante Hibernate y Spring Data JPA.
Se ha implementado un enfoque de pruebas exhaustivo que incluye pruebas
unitarias y de sistema, utilizando herramientas como JUnit 5, Mockito y Sele-
nium. Este enfoque garantiza que la l´ogica de negocio se valide adecuadamente y
que las funcionalidades se comporten como se espera.
La metodolog´ıa Git Flow se ha adoptado para gestionar el flujo de trabajo,
permitiendo una organizaci´on eficiente del desarrollo mediante ramas espec´ıficas
para cada etapa, como desarrollo, producci´on y caracter´ısticas. Tambi´en se han
adoptado principios de DevOps con la automatizaci´on del proceso de integraci´on y
despliegue continuo mediante GitHub Actions. Este ejecuta pruebas autom´aticas,
verifica la cobertura de c´odigo, gestiona el versionado del proyecto y facilita el
despliegue en Microsoft Azure, a trav´es de tecnolog´ıas como Docker y Azure
Container Instances.
Finalmente, se realiza una reflexi´on sobre los resultados obtenidos en el apar-
tado de conclusiones y se exponen algunas mejoras para posibles trabajos futuros
