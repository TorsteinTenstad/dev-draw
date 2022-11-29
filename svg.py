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

    def set_inkscape_path(self, path):
        self.inkscape_path = path

    def add_rect(self, w, h, x=0, y=0, r=0, color='#969696', opacity=1):
        self.xml_body += f""" 
<rect
    style="opacity:{opacity};fill:{color};"
    width="{w}"
    height="{h}"
    x="{x}"
    y="{y}"
    rx="{r}"
    ry="{r}" />"""

    def add_circle(self, r, x=0, y=0, color='#969696', opacity=1):
        self.xml_body += f""" 
<ellipse
    style="opacity:{opacity};fill:{color};"
    rx="{r}"
    ry="{r}"
    cx="{x}"
    cy="{y}"/>"""

    def add_polygon(self, points, color='#969696', opacity=1):
        points = ' '.join([f'{p[0]},{p[1]}' for p in points])
        self.xml_body += f"""
<polygon
    style="opacity:{opacity};fill:{color};"
    points="{points}" />"""

    def save(self, filename):
        xml = self.xml_begin + self.xml_body + self.xml_end
        with open(filename, 'w') as file:
            file.write(xml)

    def export_png(self, filename, output_w, output_h):
        xml = self.xml_begin + self.xml_body + self.xml_end
        subprocess.run([self.inkscape_path, '--export-type=png', f'--export-filename={filename}',
                        f'--export-width={output_w}', f'--export-height={output_h}', '--pipe'], input=xml.encode())
