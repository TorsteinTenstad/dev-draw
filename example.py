import devdraw

if __name__ == "__main__":
    purple = '#5F0F40'
    cyan = '#0F4C5C'
    orange = '#E36414'

    svg = devdraw.SVG(30, 30)
    svg.add(devdraw.eliments.rect(w=30, h=30, color=purple))
    svg.add(devdraw.eliments.rect(w=18, h=30, color=orange))
    svg.add(devdraw.eliments.rect(w=10, h=5, x=1, y=1, r=1, color=purple))
    svg.add(devdraw.eliments.polygon([[1, 20],[1, 29],[10, 29]], color=purple))
    c1 = devdraw.eliments.circle(r=6, x=17, y=15, color=cyan)
    cut_shape = devdraw.eliments.circle(r=3, x=17, y=15, color = "#000000")
    white_base = devdraw.eliments.rect(w=30, h=30)
    donut = devdraw.mask(c1, white_base+cut_shape)
    svg.add(donut)
    svg.set_inkscape_path('C:\\Program Files\\Inkscape\\bin\\inkscape.exe')
    svg.save('example.svg')
    svg.export_png('example_export.png', 120, 120)
