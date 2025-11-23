# Diseño e implementación de una arquitectura para la orquestación de modelos de inteligencia artificial en entornos cloud

## Información General

<div class="tfg-resources">
<a href="memoria.pdf" class="btn-pdf btn-small">Memoria PDF</a>
<a href="https://github.com/codeurjc-students/aws-ai-orchestrator" class="btn-github btn-small">GitHub</a>
</div>

**Autor/a:** Manuel Gonzalo Ramírez Tirado  
**Grado:** Doble Grado en Ingeniería Informática y Matemáticas  
**Tutor:** Michel Maes Bermejo  
**Fecha de defensa:** octubre de 2025

## Resumen

Este Trabajo Fin de Grado presenta el diseño e implementación de una arquitectura en la nube orientada a la gestión y orquestación eficiente de modelos de inteligencia artificial (IA). Toda la solución se ha desplegado íntegramente en el
ecosistema de Amazon Web Services (AWS), aprovechando su amplio conjunto
de servicios para garantizar escalabilidad, mantenibilidad y seguridad.

Con el objetivo de validar la arquitectura propuesta, se ha desarrollado un
caso de uso práctico centrado en la restauración de imágenes, en el que se integran distintos modelos de IA capaces de realizar tareas de eliminación de ruido,
aumento de resolución y eliminación de texto superpuesto (inpainting). Cada
modelo se ha desplegado como un microservicio independiente desarrollado en
FastAPI, mediante imágenes de Docker y orquestado a través de Amazon ECS.
Además, se ha automatizado el proceso de despliegue utilizando Terraform bajo
el enfoque de Infraestructura como Código (IaC).

Los resultados obtenidos demuestran la viabilidad y robustez de la arquitectura propuesta, que destaca por su modularidad, tolerancia a fallos y capacidad de adaptación. Además, la implementación confirma el potencial de AWS como
entorno completo y flexible para el despliegue de aplicaciones basadas en inteligencia artificial. Como líneas futuras de trabajo, se plantea, entre otras, el uso de
servicios con GPU, como Amazon SageMaker o Amazon EC2, la mejora de la capa de persistencia de datos con Amazon RDS y la ampliación de los mecanismos
de autenticación, para una gestión más segura de los usuarios.

