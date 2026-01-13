from pathlib import Path
import yaml
from collections import defaultdict

def define_env(env):
    """Define custom macros for mkdocs-macros-plugin."""

    @env.macro
    def include(path: str) -> str:
        """
        Include the contents of another Markdown file.
        - If `path` is relative, resolve relative to the current page's directory.
        - Otherwise, resolve from the docs/ root.
        - Strips YAML frontmatter (--- ... ---) from the included content.
        """
        # Determine base dir of current page
        page = env.variables.get('page') if hasattr(env, 'variables') else None
        base_dir = None
        try:
            if page and getattr(page, 'file', None) and getattr(page.file, 'abs_src_path', None):
                base_dir = Path(page.file.abs_src_path).parent
        except Exception:
            base_dir = None

        docs_root = Path(env.project_dir) / 'docs'
        p = Path(path)

        # Try relative to current page directory first
        content = None
        if base_dir is not None:
            candidate = (base_dir / p).resolve()
            if candidate.exists():
                content = candidate.read_text(encoding='utf-8')

        # Fallback to docs/ root
        if content is None:
            candidate = (docs_root / p).resolve()
            if candidate.exists():
                content = candidate.read_text(encoding='utf-8')

        if content is None:
            raise FileNotFoundError(f"include: file not found: {path}")

        # Strip YAML frontmatter (--- ... ---)
        if content.startswith('---\n') or content.startswith('---\r\n'):
            lines = content.splitlines(keepends=True)
            # Find the closing ---
            closing_index = -1
            for i in range(1, len(lines)):
                stripped = lines[i].strip()
                if stripped == '---':
                    closing_index = i
                    break
            
            if closing_index > 0:
                # Skip frontmatter and return content after it
                content = ''.join(lines[closing_index + 1:])
        
        return content

    @env.macro
    def generate_tags_list() -> str:
        """
        Generate an automatic list of all tags with their associated exercises.
        Scans all markdown files in docs/exams/ and groups them by tags.
        """
        docs_root = Path(env.project_dir) / 'docs'
        exams_dir = docs_root / 'exams'
        
        # Dictionary to store tags and their associated exercises
        tags_dict = defaultdict(list)
        
        # Scan all markdown files in exams directory
        for md_file in exams_dir.rglob('*.md'):
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
                                # Get relative path from docs directory
                                rel_path = md_file.relative_to(docs_root)
                                
                                # Extract title (first # heading) from content
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
                                        'path': str(rel_path).replace('\\', '/')
                                    })
                        except yaml.YAMLError:
                            pass
            except Exception:
                continue
        
        # Generate markdown output
        if not tags_dict:
            return "*No se encontraron ejercicios con tags.*"
        
        output = []
        
        # Sort tags alphabetically
        for tag in sorted(tags_dict.keys()):
            exercises = tags_dict[tag]
            output.append(f"\n## :material-tag: {tag.capitalize()}")
            output.append(f"\n*{len(exercises)} ejercicio(s)*\n")
            
            # Sort exercises by year and exam
            exercises.sort(key=lambda x: (x['year'], x['exam']))
            
            # Create table
            output.append("| Ejercicio | Año | Examen |")
            output.append("|-----------|-----|--------|")
            
            for ex in exercises:
                # Create link to exercise
                link = f"[{ex['title']}]({ex['path']})"
                output.append(f"| {link} | {ex['year']} | {ex['exam']} |")
            
            output.append("")  # Empty line between sections
        
        return '\n'.join(output)
