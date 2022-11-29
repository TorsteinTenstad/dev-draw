from svg import SVG

if __name__ == "__main__":
    white = '#ffffff'
    purple = '#880088'
    cyan = '#008888'
    yellow = '#AAAA00'

    svg = SVG(30, 30)
    svg.add_rect(30, 30, color=white)
    svg.add_rect(28, 28, 1, 1)
    svg.add_circle(8, 15, 15, color=purple)
    svg.add_circle(5, 7, 7, color=cyan)
    svg.add_rect(5, 5, 23, 23, 1, yellow)
    svg.set_inkscape_path('C:\\Program Files\\Inkscape\\bin\\inkscape.exe')
    svg.save('example.svg')
    svg.export_png('example_export.png', 120, 120)