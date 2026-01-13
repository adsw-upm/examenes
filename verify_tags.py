#!/usr/bin/env python3
"""
Script para verificar el sistema de tags automático.
Escanea todos los archivos de exámenes y muestra estadísticas de tags.
"""

from pathlib import Path
import yaml
from collections import defaultdict

def main():
    docs_root = Path('docs')
    exams_dir = docs_root / 'exams'
    
    # Dictionary to store tags and their associated exercises
    tags_dict = defaultdict(list)
    total_files = 0
    files_with_tags = 0
    
    # Scan all markdown files in exams directory
    for md_file in exams_dir.rglob('*.md'):
        total_files += 1
        try:
            content = md_file.read_text(encoding='utf-8')
            
            # Parse YAML frontmatter
            if content.startswith('---\n') or content.startswith('---\r\n'):
                lines = content.split('\n')
                closing_index = -1
                for i in range(1, len(lines)):
                    if lines[i].strip() == '---':
                        closing_index = i
                        break
                
                if closing_index > 0:
                    frontmatter = '\n'.join(lines[1:closing_index])
                    try:
                        metadata = yaml.safe_load(frontmatter)
                        if metadata and 'tags' in metadata:
                            files_with_tags += 1
                            rel_path = md_file.relative_to(docs_root)
                            
                            # Extract metadata
                            title = metadata.get('id', md_file.stem)
                            year = metadata.get('year', 'N/A')
                            exam = metadata.get('exam', 'N/A')
                            
                            # Get tags
                            tags = metadata['tags']
                            if isinstance(tags, str):
                                tags = [tags]
                            
                            # Add to each tag
                            for tag in tags:
                                tags_dict[tag].append({
                                    'title': title,
                                    'year': year,
                                    'exam': exam,
                                    'path': str(rel_path)
                                })
                    except yaml.YAMLError:
                        pass
        except Exception as e:
            print(f"Error procesando {md_file}: {e}")
            continue
    
    # Print statistics
    print("\n" + "="*60)
    print("ESTADÍSTICAS DEL SISTEMA DE TAGS")
    print("="*60)
    print(f"\nArchivos totales encontrados: {total_files}")
    print(f"Archivos con tags: {files_with_tags}")
    print(f"Tags únicos: {len(tags_dict)}")
    print(f"\n{'Tag':<20} {'Cantidad':<10}")
    print("-"*30)
    
    for tag in sorted(tags_dict.keys()):
        print(f"{tag:<20} {len(tags_dict[tag]):<10}")
    
    print("\n" + "="*60)
    print("Ejemplos de ejercicios por tag:")
    print("="*60)
    
    for tag in sorted(tags_dict.keys()):
        exercises = tags_dict[tag][:3]  # First 3 examples
        print(f"\n{tag.upper()}:")
        for ex in exercises:
            print(f"  - {ex['title']} ({ex['year']}, {ex['exam']})")

if __name__ == '__main__':
    main()
