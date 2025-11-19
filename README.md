# Repositorio de Trabajos Fin de Grado

Este repositorio contiene el sitio web de Trabajos Fin de Grado desarrollado con MkDocs.

## 🚀 Inicio rápido

### Requisitos previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tu-usuario/tfg-webpage.git
cd tfg-webpage
```

2. Instala MkDocs y las dependencias:
```bash
pip install mkdocs
pip install mkdocs-material  # Si usas el tema Material
```

### Desarrollo local

Para ejecutar el servidor de desarrollo:

```bash
mkdocs serve
```

Luego abre tu navegador en `http://localhost:8000`

### Construcción del sitio

Para generar los archivos HTML estáticos:

```bash
mkdocs build
```

Los archivos se generarán en la carpeta `site/`

### Despliegue

Para desplegar en GitHub Pages:

```bash
mkdocs gh-deploy
```

## 📁 Estructura del proyecto

```
tfg-webpage/
├── docs/                      # Contenido del sitio
│   ├── index.md              # Página principal
│   ├── style.css             # Estilos personalizados
│   └── tfgs/                 # Carpeta de TFGs
│       ├── 2024-06-15-sistema-gestion-inventarios/
│       ├── 2024-07-10-app-movil-salud/
│       └── 2024-09-20-chatbot-atencion-cliente/
├── mkdocs.yml                # Configuración de MkDocs
├── Dockerfile                # Docker para despliegue
├── README.md                 # Este archivo
└── COMO_ANADIR_TFG.md       # Guía para añadir TFGs
```

## ➕ Cómo añadir un nuevo TFG

Consulta el archivo [COMO_ANADIR_TFG.md](COMO_ANADIR_TFG.md) para instrucciones detalladas.

Pasos básicos:

1. Crear carpeta en `docs/tfgs/AAAA-MM-DD-nombre-del-tfg/` (fecha de defensa)
2. Añadir archivo `index.md` con la información del TFG
3. Incluir el PDF de la memoria
4. Actualizar `docs/index.md` con la nueva tarjeta
5. Actualizar `mkdocs.yml` en la sección de navegación

## 🎨 Personalización

### Modificar colores

Edita las variables CSS en `docs/style.css`:

```css
:root {
    --md-primary-fg-color: #aa0000;  /* Color principal */
    --md-accent-fg-color: #8a8a8a;   /* Color de acento */
}
```

### Cambiar el título del sitio

Edita `mkdocs.yml`:

```yaml
site_name: Tu Título Aquí
site_description: Tu descripción
```

## 🐳 Docker

### Construir la imagen

```bash
docker build -t tfg-webpage .
```

### Ejecutar el contenedor

```bash
docker run -p 8000:8000 tfg-webpage
```

## 📝 Formato de un TFG

Cada TFG debe incluir:

- **Título**: Nombre descriptivo del proyecto
- **Nombre del alumno**: Nombre completo del estudiante
- **Grado**: Grado universitario al que pertenece
- **Tutor(es)**: Uno o dos tutores
- **Fecha de defensa**: Fecha completa (ej: "15 de junio de 2024")
- **Descripción**: Resumen del proyecto
- **Tags**: Tecnologías utilizadas (web, java, python, etc.)
- **PDF**: Memoria del TFG
- **GitHub**: Enlace al repositorio

**Importante**: El nombre de la carpeta debe seguir el formato `AAAA-MM-DD-titulo-breve` donde la fecha corresponde a la fecha de defensa.

## 🤝 Contribuir

Para contribuir a este proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añade nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 📞 Contacto

Para preguntas o sugerencias, contacta con [tu-email@universidad.es](mailto:tu-email@universidad.es)

## 🔧 Solución de problemas

### El servidor no inicia
- Verifica que MkDocs está instalado: `mkdocs --version`
- Comprueba que estás en el directorio correcto

### Los cambios no se reflejan
- Asegúrate de que el servidor está ejecutándose
- Recarga la página con Ctrl+F5 (forzar recarga)

### Errores de construcción
- Verifica la sintaxis del archivo `mkdocs.yml`
- Comprueba que todos los archivos referenciados existen
- Revisa que no hay errores en el markdown

## 📚 Recursos adicionales

- [Documentación de MkDocs](https://www.mkdocs.org/)
- [MkDocs Material Theme](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
