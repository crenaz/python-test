import sys
import svgwrite
from graphviz import Digraph
import os
from pathlib import Path

def create_svg(filename='static/example.svg'):
    # Ensure static directory exists
    static_dir = Path('static')
    static_dir.mkdir(exist_ok=True)
    
    # Create a new SVG drawing
    dwg = svgwrite.Drawing(filename, size=('800px', '600px'))

    # Add a light blue background rectangle
    dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='#f0f8ff'))

    # Circle with pulsing and color change animations
    circle = dwg.circle(center=(400, 300), r=100,
                       fill='#ff6b6b', stroke='#c92a2a', stroke_width=3)
    
    # Add animations directly to the circle
    circle.add(dwg.animate(
        attributeName='r',
        values='100;120;100',
        dur='4s',
        repeatCount='indefinite'
    ))
    
    circle.add(dwg.animate(
        attributeName='fill',
        values='#ff6b6b;#ffd43b;#69db7c;#ff6b6b',
        dur='6s',
        repeatCount='indefinite'
    ))
    dwg.add(circle)

    # Rectangle with rotating animation
    rect = dwg.rect(insert=(250, 200), size=(100, 100),
                    rx=20, ry=20,
                    fill='#4dabf7',
                    stroke='#1864ab',
                    stroke_width=2)
    
    # Add rotation animation
    rect.add(dwg.animateTransform(
        type='rotate',
        from_='0 300 250',
        to='360 300 250',
        dur='6s',
        repeatCount='indefinite',
        transform='rotate(0 300 250)'
    ))
    dwg.add(rect)

    # Triangle with bounce effect
    points = [(550, 200), (650, 350), (450, 350)]
    triangle = dwg.polygon(points=points,
                          fill='#51cf66',
                          stroke='#2b8a3e',
                          stroke_width=2)
    
    # Add bounce animation
    triangle.add(dwg.animateTransform(
        type='translate',
        from_='0 0',
        to='0 -30',
        dur='2s',
        repeatCount='indefinite',
        transform='translate(0 0)'
    ))
    dwg.add(triangle)

    # Animated text with fade effect
    text = dwg.text('SVG Example', insert=(320, 100),
                    style='font-size: 24px; font-family: Arial; fill: #1a1a1a')
    text.add(dwg.animate(
        attributeName='opacity',
        values='1;0.3;1',
        dur='3s',
        repeatCount='indefinite'
    ))
    dwg.add(text)

    # Group of circles with wave animation
    g = dwg.g(style='opacity:0.7')
    for x in range(5):
        circle = dwg.circle(center=(100 + x*50, 500), r=15,
                           fill='#be4bdb',
                           stroke='#862e9c',
                           stroke_width=2)
        # Add wave animation with delay based on position
        circle.add(dwg.animate(
            attributeName='cy',
            values='500;480;500;520;500',
            dur='2s',
            begin=f'{x * 0.2}s',
            repeatCount='indefinite'
        ))
        g.add(circle)
    dwg.add(g)

    # Animated path that draws itself
    path = dwg.path(d='M 100,300 C 200,200 300,200 400,300',
                    stroke='#495057',
                    stroke_width=3,
                    fill='none')
    path.add(dwg.animate(
        attributeName='stroke-dasharray',
        values='0,1000;1000,0',
        dur='4s',
        repeatCount='indefinite'
    ))
    dwg.add(path)

    # Add a moving dot along the path
    dot = dwg.circle(r=8, fill='#e64980')
    # Create motion path animation
    motion_path = dwg.animateMotion(
        path='M 100,300 C 200,200 300,200 400,300',
        dur='4s',
        repeatCount='indefinite'
    )
    dot.add(motion_path)
    dwg.add(dot)

    # Save the SVG file
    dwg.save()
    return filename

if __name__ == "__main__":
    svg_file = create_svg()
    print(f"Animated SVG file '{svg_file}' has been created successfully!")