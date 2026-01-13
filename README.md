# Catálogo de Ejercicios de Años Anteriores

Este proyecto contiene un catálogo de ejercicios de exámenes de años anteriores, organizado con MkDocs y Material for MkDocs.

## Características

### Sistema de Tags Automático

La página de tags ([docs/tags.md](docs/tags.md)) se genera automáticamente escaneando todos los archivos de ejercicios en el directorio `docs/exams/`. El sistema:

- **Genera automáticamente** la lista de todos los tags y sus ejercicios asociados
- **Organiza** los ejercicios por tag, mostrando:
  - ID del ejercicio con enlace directo
  - Año del examen
  - Tipo de examen (parcial 1, parcial 2, final, extraordinario, etc.)
- **Es buscable** en la web gracias al plugin de búsqueda de Material for MkDocs
- **Se actualiza** automáticamente al agregar nuevos ejercicios con tags

### Tags Disponibles

- **complejidad**: Ejercicios sobre análisis de complejidad algorítmica
- **ordenación**: Problemas de algoritmos de ordenación
- **concurrencia**: Ejercicios de programación concurrente
- **monitores**: Problemas sobre sincronización con monitores
- **android**: Ejercicios de desarrollo Android
- **actividades**: Ejercicios sobre actividades en Android

## Estructura del Proyecto

```
docs/
├── index.md              # Página principal
├── tags.md              # Página de tags (se genera automáticamente)
└── exams/               # Directorio de exámenes
    ├── 2012/
    ├── 2013/
    ├── 2014/
    ├── 2015/
    └── 2021/
```

## Cómo Agregar un Nuevo Ejercicio

Para agregar un nuevo ejercicio con tags:

1. Crea un archivo markdown en el directorio correspondiente (ej: `docs/exams/2024/p1_ex01.md`)
2. Agrega el frontmatter YAML con la metadata:

```yaml
---
id: ex-2024-01
year: 2024
exam: parcial 1
tags:
 - complejidad
 - ordenación
---
```

3. Escribe el contenido del ejercicio
4. El ejercicio aparecerá automáticamente en la página de tags al regenerar el sitio

## Desarrollo

### Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Servidor de Desarrollo

```bash
mkdocs serve
```

El sitio estará disponible en http://127.0.0.1:8000

### Construir el Sitio

```bash
mkdocs build
```

## Funcionalidades Técnicas

### Macros Personalizadas

El archivo [main.py](main.py) define dos macros para mkdocs-macros-plugin:

- `include(path)`: Incluye el contenido de otro archivo Markdown, eliminando el frontmatter YAML
- `generate_tags_list()`: Genera automáticamente la lista de tags con todos los ejercicios organizados

### Búsqueda Mejorada

La configuración de búsqueda está optimizada para dar mayor peso a los tags (boost: 2), facilitando encontrar ejercicios por tema.

## Problemas Conocidos

- Hay que revisar la publicación de las fórmulas de complejidad. Muchas no tienen el formato correcto.
- Algunas imágenes referenciadas no existen (ej: `p1r_ex1.png` en 2014)

## Licencia

[Especificar la licencia del proyecto]

