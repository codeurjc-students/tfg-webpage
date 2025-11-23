# Healthcarer: una aplicación web orientada a la gestión y seguimiento de los tratamientos médicos

## Información General

<div class="tfg-resources">
<a href="2025-26-ETSII-A-2113-2113042-eva.ruiz-MEMORIA.pdf" class="btn-pdf btn-small">Memoria PDF</a>
<a href="https://github.com/codeurjc-students/HealthCarer" class="btn-github btn-small">GitHub</a>
</div>

**Autor/a:** Eva Ruiz Aguado  
**Grado:** Doble Grado en Ingeniería Informática e Ingeniería de Computadores  
**Tutor:** Michel Maes Bermejo  
**Fecha de defensa:** Septiembre de 2025

## Resumen

La aplicación web diseñada para la gestión y el seguimiento de tratamientos médicos surge de la necesidad de mejorar la adherencia a los tratamientos farmacológicos. La aplicación incorpora y fusiona funcionalidades de plataformas líderes como MyTherapy y Medisafe, destacando su sistema de notificaciones y la claridad del historial de tomas.

La arquitectura de la aplicación se basa en un modelo de tres capas (frontend, backend y base de datos) y sigue el patrón de diseño Modelo-Vista-Controlador (MVC). En el backend, se utilizan Java y Spring Boot, con Spring Security para la seguridad y JPA/Spring Data para la persistencia. El frontend está construido con HTML, CSS, JavaScript y Mustache. En cuanto a las bases de datos, se emplea MySQL en producción y H2 para el desarrollo. El proyecto implementa pruebas unitarias, de integración y End-to-End (E2E) con JUnit, Mockito y Selenium. El desarrollo sigue la metodología de Trunk Based Development para facilitar la integración y entrega continuas, automatizadas con GitHub Actions. Finalmente, el despliegue se realiza mediante contenedores Docker y utilizando Docker Compose.

El trabajo detalla las distintas fases del proyecto, comenzando por la motivación inicial y la definición de los objetivos, pasando por el análisis de tecnologías y metodologías, y el diseño e implementación de la aplicación. También se incluyen las pruebas y su automatización, el empaquetado con Docker, y el despliegue final. El documento concluye con un análisis de los resultados y propuestas para futuros trabajos.
