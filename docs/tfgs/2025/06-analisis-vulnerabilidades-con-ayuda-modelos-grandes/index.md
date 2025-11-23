# Análisis de vulnerabilidades con ayuda de modelos grandes de lenguaje

## Información General

<div class="tfg-resources">
<a href="2024-25-ETSII-A-2285-2285040-g.izquierdo.2018-MEMORIA.pdf" class="btn-pdf btn-small">Memoria PDF</a>
<a href="https://github.com/ZAP-TFG/zap_automatice_web" class="btn-github btn-small">GitHub</a>
</div>
**Autor/a:** Gabriel Izquierdo González  
**Grado:** Grado En Ingeniería De La Ciberseguridad  
**Tutores:** Michel Maes Bermejo, Jesús María González Barahoña  
**Fecha de defensa:** junio de 2025

## Resumen

Este Trabajo Final de Grado se centra en el desarrollo y el diseño de una
plataforma web cuyo principal objetivo es analizar y evaluar el comportamiento
de los grandes modelos de lenguaje (LLM) en el ámbito de las auditorías de
seguridad web. La herramienta integra tecnologías, como OWASP ZAP para el
escaneo de vulnerabilidades, junto con un LLM que permite generar resúmenes
y documentos personalizados, comparación de resultados y búsquedas de falsos
positivos.

La plataforma está implementada principalmente en Python y Flask. Permite
al usuario ejecutar y programar escáneres de seguridad, ser notificado una vez ter-
minado el escáner, ver los resultados a través de gráficas y un chatbot inteligente
y recibir explicaciones y recomendaciones sobre las vulnerabilidades detectadas.
Además, se ha desarrollado un motor de generación automática de informes en
formato DOCX, en el que el LLM se encarga de redactar descripciones, evaluar
riesgos y proponer medidas de mitigación de forma contextualizada.
La arquitectura de la plataforma se ha desarrollado de tal manera que pueda
ser modular y escalable. Se usa PostgreSQL para la persistencia de los datos,
Docker para la contenedorización y el despliegue, y APScheduler para la progra-
mación de escáneres. Y además, se ha incluido la generación de informes a partir
de archivos JSON generados por Owasp Zap.

Entre algunos de los logros del proyecto, se encuentran la capacidad del LLM
para traducir información técnica en explicaciones mas sencillas, así como su
papel en la generación documentación, y el análisis de resultados. Sin embargo,
también se han identificado limitaciones en la detección de falsos positivos, lo que
abre la puerta a futuras mejoras y líneas de investigación.

