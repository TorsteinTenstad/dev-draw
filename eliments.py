def rect(w, h, x=0, y=0, r=0, color='#ffffff', opacity=1):
    return f""" 
<rect
    style="opacity:{opacity};fill:{color};"
    width="{w}"
    height="{h}"
    x="{x}"
    y="{y}"
    rx="{r}"
    ry="{r}" />"""

def circle(r, x=0, y=0, color='#ffffff', opacity=1):
    return f""" 
<ellipse
    style="opacity:{opacity};fill:{color};"
    rx="{r}"
    ry="{r}"
    cx="{x}"
    cy="{y}"/>"""

def polygon(points, color='#ffffff', opacity=1):
    points = ' '.join([f'{p[0]},{p[1]}' for p in points])
    return f"""
<polygon
    style="opacity:{opacity};fill:{color};"
    points="{points}" />"""
