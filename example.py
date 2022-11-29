from svg import SVG

if __name__ == "__main__":
    white = '#ffffff'
    purple = '#5F0F40'
    cyan = '#0F4C5C'
    orange = '#E36414'

    svg = SVG(30, 30)
    svg.add_rect(w=30, h=30, color=purple)
    svg.add_rect(w=18, h=30, color=orange)
    svg.add_circle(r=6, x=15, y=15, color=cyan)
    svg.add_rect(w=10, h=5, x=1, y=1, r=1, color=purple)
    svg.add_polygon([[1, 20],[1, 29],[10, 29]], color=purple)
    svg.set_inkscape_path('C:\\Program Files\\Inkscape\\bin\\inkscape.exe')
    svg.save('example.svg')
    svg.export_png('example_export.png', 120, 120)
