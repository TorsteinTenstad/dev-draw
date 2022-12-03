import subprocess

class SVG:
    def __init__(self, w, h):
        self.inkscape_path = ''
        self.xml_begin = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Dev-Draw (https://github.com/TorsteinTenstad/dev-draw) -->

<svg
    width="{w}"
    height="{h}"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:svg="http://www.w3.org/2000/svg">"""
        self.xml_body = ''
        self.xml_end = """
</svg>"""

    def add(self, xml_string):
        self.xml_body += xml_string

    def set_inkscape_path(self, path):
        self.inkscape_path = path

    def save(self, filename):
        xml = self.xml_begin + self.xml_body + self.xml_end
        with open(filename, 'w') as file:
            file.write(xml)

    def export_png(self, filename, output_w, output_h):
        xml = self.xml_begin + self.xml_body + self.xml_end
        subprocess.run([self.inkscape_path, '--export-type=png', f'--export-filename={filename}',
                        f'--export-width={output_w}', f'--export-height={output_h}', '--pipe'], input=xml.encode())
