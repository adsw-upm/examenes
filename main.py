from pathlib import Path

def define_env(env):
    """Define custom macros for mkdocs-macros-plugin."""

    @env.macro
    def include(path: str) -> str:
        """
        Include the contents of another Markdown file.
        - If `path` is relative, resolve relative to the current page's directory.
        - Otherwise, resolve from the docs/ root.
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
        if base_dir is not None:
            candidate = (base_dir / p).resolve()
            if candidate.exists():
                return candidate.read_text(encoding='utf-8')

        # Fallback to docs/ root
        candidate = (docs_root / p).resolve()
        if candidate.exists():
            return candidate.read_text(encoding='utf-8')

        # If still not found, raise a helpful error
        raise FileNotFoundError(f"include: file not found: {path}")
