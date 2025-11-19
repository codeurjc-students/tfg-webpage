# Cómo añadir un nuevo Trabajo Fin de Grado

Este documento explica cómo añadir un nuevo TFG al sitio web.

## Pasos para añadir un nuevo TFG

### 1. Crear la estructura de carpetas

Crea una nueva carpeta dentro de `docs/tfgs/` siguiendo el formato `año-mes-día-breve-título`:

```bash
mkdir docs/tfgs/2024-06-15-nombre-del-tfg
```

**Formato del nombre:**
- `AAAA-MM-DD`: Fecha de defensa del TFG
- Seguido de un título breve en minúsculas y con guiones
- Ejemplo: `2024-06-15-sistema-gestion-inventarios`

### 2. Crear el archivo index.md

Dentro de la carpeta del TFG, crea un archivo `index.md` con la siguiente estructura:

```markdown
# Título del TFG

## Información General

**Autor:** Nombre del Estudiante  
**Grado:** Nombre del Grado  
**Tutor(es):** Nombre del/los Tutor(es)  
**Fecha de defensa:** DD de mes de AAAA  

## Resumen

Descripción breve del proyecto...

## Objetivos

- Objetivo 1
- Objetivo 2
- ...

## Tecnologías Utilizadas

### Categoría 1
- **Tecnología 1** - Descripción
- **Tecnología 2** - Descripción

### Categoría 2
- ...

## Funcionalidades Principales

1. **Funcionalidad 1**
   - Detalle...

## Recursos

- 📄 [Descargar Memoria PDF](memoria.pdf)
- 💻 [Repositorio GitHub](https://github.com/usuario/repo)

## Tecnologías

<div class="tfg-tags">
<span class="tag">tag1</span>
<span class="tag">tag2</span>
<span class="tag">tag3</span>
</div>
```

### 3. Añadir el PDF de la memoria

Coloca el archivo PDF de la memoria en la misma carpeta con el nombre `memoria.pdf`:

```bash
cp ruta/al/archivo.pdf docs/tfgs/2024-06-15-nombre-del-tfg/memoria.pdf
```

### 4. Actualizar el archivo index.md principal

Edita `docs/index.md` y añade una nueva tarjeta en el grid:

```html
<div class="tfg-card">
<h3><a href="tfgs/2024-06-15-nombre-del-tfg/">Título del TFG</a></h3>
<p class="tfg-student">👨‍🎓 <strong>Nombre del Alumno</strong></p>
<p class="tfg-meta">📚 Nombre del Grado | 📅 DD de mes de AAAA</p>
<p class="tfg-tutor">👤 Tutor: Nombre del Tutor</p>
<p class="tfg-description">Descripción breve del proyecto...</p>
<div class="tfg-tags">
<span class="tag">tecnologia1</span>
<span class="tag">tecnologia2</span>
</div>
<div class="tfg-links">
<a href="tfgs/2024-06-15-nombre-del-tfg/memoria.pdf" class="btn-pdf">📄 Memoria PDF</a>
<a href="https://github.com/usuario/repo" class="btn-github">⚙️ GitHub</a>
</div>
</div>
```

### 5. Actualizar la navegación

Edita `mkdocs.yml` y añade el nuevo TFG en la sección `nav`:

```yaml
nav:
  - Inicio: index.md
  - Trabajos Fin de Grado:
    - Sistema de Gestión de Inventarios: tfgs/2024-06-15-sistema-gestion-inventarios/index.md
    - Chatbot Inteligente: tfgs/2024-09-20-chatbot-atencion-cliente/index.md
    - App Móvil de Salud: tfgs/2024-07-10-app-movil-salud/index.md
    - Nuevo TFG: tfgs/2024-06-15-nombre-del-tfg/index.md  # <-- Añadir aquí
```

### 6. Previsualizar los cambios

Ejecuta el servidor de desarrollo de MkDocs:

```bash
mkdocs serve
```

Abre tu navegador en `http://localhost:8000` para ver los cambios.

### 7. Desplegar

Si todo se ve correctamente, despliega los cambios:

```bash
mkdocs build
# o
mkdocs gh-deploy  # si usas GitHub Pages
```

## Campos de información del TFG

### Información obligatoria
- Título
- Nombre del alumno
- Grado al que pertenece
- Tutor(es)
- Fecha de defensa (formato: DD de mes de AAAA)
- Descripción
- Tags de tecnologías
- Link al repositorio de GitHub

### Información opcional
- PDF de la memoria
- Curso académico
- Fecha de defensa
- Presentación
- Vídeo demostración
- Imágenes/capturas

## Tags de tecnologías más comunes

- `web` - Aplicaciones web
- `mobile` - Aplicaciones móviles
- `java` - Lenguaje Java
- `python` - Lenguaje Python
- `javascript` - JavaScript
- `typescript` - TypeScript
- `angular` - Framework Angular
- `react` - Framework React
- `vue` - Framework Vue.js
- `spring-boot` - Spring Boot
- `django` - Django
- `flask` - Flask
- `nodejs` - Node.js
- `docker` - Docker
- `kubernetes` - Kubernetes
- `aws` - Amazon Web Services
- `azure` - Microsoft Azure
- `machine-learning` - Machine Learning
- `deep-learning` - Deep Learning
- `nlp` - Natural Language Processing
- `blockchain` - Blockchain
- `iot` - Internet of Things
- `android` - Android nativo
- `ios` - iOS nativo
- `flutter` - Flutter
- `react-native` - React Native

## Estructura de carpetas recomendada

```
docs/tfgs/2024-06-15-nombre-del-tfg/
├── index.md              # Página principal del TFG
├── memoria.pdf           # Memoria del TFG
├── presentacion.pdf      # (Opcional) Presentación
├── demo.mp4             # (Opcional) Vídeo demostración
└── images/              # (Opcional) Imágenes adicionales
    ├── screenshot1.png
    └── screenshot2.png
```

**Nota importante sobre el nombre de la carpeta:**
- Debe seguir el formato: `AAAA-MM-DD-titulo-breve`
- La fecha debe corresponder a la fecha de defensa del TFG
- El título debe ser breve, descriptivo, en minúsculas y con guiones
- Ejemplos válidos:
  - `2024-06-15-sistema-gestion-inventarios`
  - `2024-09-20-chatbot-atencion-cliente`
  - `2025-01-10-plataforma-educativa`

## Consejos

1. **Usa el formato correcto para nombres de carpetas**: `AAAA-MM-DD-titulo-breve` (la fecha debe ser la de defensa)
2. **Optimiza el PDF** antes de subirlo para reducir el tamaño
3. **Añade capturas de pantalla** si el proyecto tiene interfaz visual
4. **Escribe descripciones claras** que destaquen el valor del proyecto
5. **Mantén los links actualizados** (especialmente el de GitHub)
6. **Revisa la ortografía** antes de publicar
7. **Usa fechas completas** en el formato "DD de mes de AAAA" (ej: "15 de junio de 2024")

## Problemas comunes

### El PDF no se descarga
- Verifica que el archivo existe en la ruta correcta
- Comprueba que el nombre del archivo es correcto (sensible a mayúsculas)

### Los estilos no se aplican
- Asegúrate de que `style.css` está referenciado en `mkdocs.yml`
- Limpia la caché del navegador

### Las imágenes no se muestran
- Usa rutas relativas desde el archivo markdown
- Verifica que las imágenes existen en la ubicación especificada
