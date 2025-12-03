import os

# Katalogas su KML failais
kml_dir = "kml_files"

# Surenkam visus .kml failus kataloge
kml_files = [f for f in os.listdir(kml_dir) if f.endswith(".kml")]

# Sukuriam index.kml
with open("index.kml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n')
    f.write('<name>Balionų Layeriai</name>\n\n')

    for kml in kml_files:
        url_kml = kml.replace(" ", "%20")  # encode spaces
        f.write(f'  <NetworkLink>\n')
        f.write(f'    <name>{kml}</name>\n')
        f.write(f'    <Link>\n')
        f.write(f'      <href>https://raw.githubusercontent.com/kkcltu/Balionai/refs/heads/main/{kml_dir}/{url_kml}</href>\n')
        f.write(f'      <refreshMode>onInterval</refreshMode>\n')
        f.write(f'      <refreshInterval>300</refreshInterval>\n')
        f.write(f'    </Link>\n')
        f.write(f'  </NetworkLink>\n\n')

    f.write('</Document>\n</kml>')

print("index.kml sugeneruotas sėkmingai!")
