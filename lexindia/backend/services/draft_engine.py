from jinja2 import Environment, FileSystemLoader
import os

class DraftingEngine:
    """
    LexIndia Document Factory.
    """
    def __init__(self):
        # Path updated to point to the new 'db/templates' directory
        template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'templates'))
        self.env = Environment(loader=FileSystemLoader(template_dir))

    async def generate_document(self, template_name: str, data: dict) -> str:
        template = self.env.get_template(f"{template_name}.jinja2")
        return template.render(**data)

drafting_engine = DraftingEngine()
