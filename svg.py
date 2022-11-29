import subprocess

class SVG:
    def __init__(self, w, h):
        self.inkscape_path = ''
        self.xml_begin = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Dev-Draw (https://github.com/TorsteinTenstad/dev-draw) -->

<svg
    width="{w}mm"
    height="{h}mm"
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
     style="opacity:{opacity};fill:{color};stroke-width:0.0"
     width="{w}mm"
     height="{h}mm"
     x="{x}mm"
     y="{y}mm"
     rx="{r}mm"
     ry="{r}mm" />"""

    def add_circle(self, r, x=0, y=0, color='#969696', opacity=1):
        self.xml_body += f""" 
<ellipse
     style="opacity:{opacity};fill:{color};stroke-width:0.0"
     rx="{r}mm"
     ry="{r}mm"
     cx="{x}mm"
     cy="{y}mm"/>"""

    def save(self, filename):
        xml = self.xml_begin + self.xml_body + self.xml_end
        with open(filename, 'w') as file:
            file.write(xml)

    def export_png(self, filename, output_w, output_h):
        xml = self.xml_begin + self.xml_body + self.xml_end
        subprocess.run([self.inkscape_path, '--export-type=png', f'--export-filename={filename}',
                        f'--export-width={output_w}', f'--export-height={output_h}', '--pipe'], input=xml.encode())
