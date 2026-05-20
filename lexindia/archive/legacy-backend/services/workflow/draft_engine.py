from jinja2 import Environment, FileSystemLoader
import os

class DraftingEngine:
    """
    Stage 3: Document Factory.
    Generates structured legal documents from templates and AI data.
    """
    
    def __init__(self):
        # Look for templates in the new 'db/templates' directory
        template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'db', 'templates'))
        self.env = Environment(loader=FileSystemLoader(template_dir))

    async def generate_document(self, template_name: str, data: dict) -> str:
        """
        Renders a legal document based on a template and user data.
        """
        try:
            template = self.env.get_template(f"{template_name}.jinja2")
            rendered_doc = template.render(**data)
            return rendered_doc
        except Exception as e:
            return f"Error generating document: {str(e)}"

drafting_engine = DraftingEngine()
