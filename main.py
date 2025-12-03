from pathlib import Path

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
