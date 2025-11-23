# Desarrollo y despliegue de una aplicación web para la gestión de citas en una clínica de nutrición

## Información General

<div class="tfg-resources">
<a href="2024-25-ETSII-A-2097-2097058-j.leal.2020-MEMORIA.pdf" class="btn-pdf btn-small">Memoria PDF</a>
<a href="https://github.com/codeurjc-students/2025-ClinicaNutricion" class="btn-github btn-small">GitHub</a>
</div>
**Autor/a:** Jorge Leal Gozalo  
**Grado:** Doble Grado en Ingeniería Informática y Administracion Y Direccion De Empresas  
**Tutor:** Michel Maes Bermejo  
**Fecha de defensa:** julio de 2025

## Resumen

La aplicación de gestión de citas para una clínica de nutrición surge de la
necesidad de modernizar un sistema tradicional de citación basado en llamadas
y mensajes, especialmente en un contexto donde la obesidad en España muestra
una tendencia creciente. Este proyecto propone una solución web que reduce la
carga administrativa del personal de la clínica y otorga autonomía a los pacientes.
El frontend es una single-page application (SPA) desarrollada en React, des-
plegada en un bucket de Amazon Simple Storage Service (S3) y distribuida me-
diante Amazon CloudFront. El backend se implementa con Spring Boot y se
ejecuta en una instancia EC2 (Elastic Compute Cloud) gestionada por Elastic
Beanstalk de Amazon Web Services (AWS). La base de datos relacional MySQL
se aloja en Amazon Relational Database Service (RDS). La autenticación y autorización se gestionan a traves de AWS Cognito, emitiendo tokens que validan
cada petición al backend. Se utilizan funciones AWS Lambda que automatizan el
alta de pacientes en la base de datos y Amazon Simple Email Service (SES) para
el envío de correos electrónicos automáticos con la información de las citas.
La interfaz contempla cuatro roles diferenciados: pacientes, nutricionistas, au-
xiliares y administradores. Los pacientes pueden registrarse de forma autónoma a
través de la aplicación o mediante un alta asistida por un miembro de la clínica,
gestionar sus propias citas (reserva, consulta y cancelación) y recibir notificaciones por correos automatizados. Los auxiliares administran las agendas de todos
los nutricionistas, mientras que estos últimos pueden acceder a su calendario y
reprogramar citas si lo desean.
Para asegurar la calidad del software, el proyecto incorpora análisis estático y
pruebas automatizadas. También se han adoptado principios DevOps mediante
el uso de GitHub Actions para automatizar el proceso de integración y despliegue
continuo.
Este documento detalla todas las etapas del proyecto: desde la introducción
y la motivación inicial, pasando por la definición de objetivos y requisitos, el
análisis de tecnologías y metodologías utilizadas, el diseño e implementación de
la aplicación web, las pruebas y el análisis estático, hasta el despliegue en AWS,
terminando con las conclusiones y propuestas de trabajos futuros.

