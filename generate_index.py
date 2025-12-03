import os

# Katalogas, kuriame laikomi KML failai
kml_dir = "kml_files"

# Surenkam visus .kml failus kataloge
kml_files = [f for f in os.listdir(kml_dir) if f.endswith(".kml")]

# Pradedam kurti index.kml
with open("index.kml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n')
    f.write('<name>Balionų Layeriai</name>\n\n')

    for kml in kml_files:
        # Encode spaces ir specialius simbolius URL
        url_kml = kml.replace(" ", "%20")
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
