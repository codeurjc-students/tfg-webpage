#!/usr/bin/env python3
import json
import os
import sys
import re
from pathlib import Path
import yaml

def slugify(text):
    # Convertir a minúsculas, reemplazar espacios y caracteres no alfanuméricos por guiones
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)  # Remover caracteres especiales excepto espacios y guiones
    text = re.sub(r'\s+', '-', text)  # Reemplazar espacios por guiones
    text = re.sub(r'-+', '-', text)  # Reemplazar múltiples guiones por uno
    return text.strip('-')

def month_to_number(month):
    months = {
        'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
        'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
        'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12'
    }
    return months.get(month.lower(), '01')  # Default to 01 if not found

def capitalize_month(month):
    return month.capitalize()

def main(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    title = data['title']
    resume = data['resume']
    author = data['author']
    tutor = data['tutor']
    degree = data['degree']
    year = int(data['year'])
    month = data['month']
    pdf_link = data['pdf_link']
    github_link = data['github_link']
    keywords = data['keywords']
    
    # Crear slug
    slug = slugify(title)
    
    # Mes en número
    month_num = month_to_number(month)
    
    # Carpeta
    folder_name = f"{month_num}-{slug}"
    folder_path = Path(f"docs/tfgs/{year}/{folder_name}")
    
    if folder_path.exists():
        print(f"Error: La carpeta {folder_path} ya existe.")
        sys.exit(1)
    
    folder_path.mkdir(parents=True, exist_ok=True)
    
    # Crear index.md
    index_content = f"""# {title}

## Información General

<div class="tfg-resources">
<a href="{pdf_link}" class="btn-pdf btn-small">Memoria PDF</a>
<a href="{github_link}" class="btn-github btn-small">GitHub</a>
</div>

**Autor/a:** {author}  
**Grado:** {degree}  
**Tutor:** {tutor}  
**Fecha de defensa:** {capitalize_month(month)} de {year}

## Resumen

{resume}

## Tags

<div class="tfg-tags">
""" + '\n'.join(f'<span class="tag">{kw}</span>' for kw in keywords) + """
</div>
"""
    
    (folder_path / 'index.md').write_text(index_content, encoding='utf-8')
    
    # Añadir a docs/index.md
    index_file = Path('docs/index.md')
    content = index_file.read_text(encoding='utf-8')
    
    # Encontrar <div class="tfg-grid"> y añadir después
    grid_start = content.find('<div class="tfg-grid">')
    if grid_start == -1:
        print("Error: No se encontró <div class=\"tfg-grid\"> en docs/index.md")
        sys.exit(1)
    
    insert_pos = content.find('\n', grid_start) + 1
    
    card_content = f"""

<div class="tfg-card">
<h3><a href="tfgs/{year}/{folder_name}/">{title}</a></h3>
<p class="tfg-student">👨‍🎓 <strong>{author}</strong></p>
<p class="tfg-meta">📚 {degree}</p>
<p class="tfg-meta">📅 {capitalize_month(month)} de {year}</p>
<p class="tfg-tutor">👤 Tutor: {tutor}</p>
<div class="tfg-links">
<a href="tfgs/{year}/{folder_name}/{pdf_link}" class="btn-pdf btn-small">Memoria PDF</a>
<a href="{github_link}" class="btn-github btn-small">GitHub</a>
</div>
<div class="tfg-tags">
""" + '\n'.join(f'<span class="tag">{kw}</span>' for kw in keywords) + """
</div>

</div>
"""
    
    new_content = content[:insert_pos] + card_content + content[insert_pos:]
    index_file.write_text(new_content, encoding='utf-8')
    
    # Actualizar mkdocs.yml
    with open('mkdocs.yml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    tfgs_nav = config['nav'][1]['Trabajos Fin de Grado']
    
    # Path del nuevo TFG
    tfg_path = f"tfgs/{year}/{folder_name}/index.md"
    
    year_found = False
    for year_dict in tfgs_nav:
        if year in year_dict:
            year_dict[year].insert(0, {title: tfg_path})
            year_found = True
            break
    
    if not year_found:
        tfgs_nav.insert(0, {year: [{title: tfg_path}]})
    
    # Ordenar los años en orden descendente
    tfgs_nav.sort(key=lambda d: list(d.keys())[0], reverse=True)
    
    with open('mkdocs.yml', 'w', encoding='utf-8') as f:
        yaml.safe_dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"TFG añadido exitosamente en {folder_path}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python add_tfg.py <json_file>")
        sys.exit(1)
    main(sys.argv[1])