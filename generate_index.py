import os
import urllib.parse

# katalogas su KML failais
kml_dir = "kml_files"
# kelias, kur bus sukurtas index.kml
index_file = "index.kml"

# jūsų GitHub repo informacija
github_user = "kkcltu"
github_repo = "Balionai"
github_branch = "main"  # arba kita šaka, jei reikia

# patikriname, ar katalogas egzistuoja
if not os.path.exists(kml_dir):
    print(f"Katalogas {kml_dir} neegzistuoja!")
    exit(1)

# surenkame visus KML failus kataloge
kml_files = [f for f in os.listdir(kml_dir) if f.endswith(".kml")]

# pradinis KML turinys
kml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Index of KML files</name>
'''

# pridedame NetworkLink kiekvienam KML failui
for kml in kml_files:
    # suformuojame GitHub raw URL
    href = f"https://raw.githubusercontent.com/{github_user}/{github_repo}/{github_branch}/{kml_dir}/{urllib.parse.quote(kml)}"
    kml_content += f'''    <NetworkLink>
      <name>{kml}</name>
      <Link>
        <href>{href}</href>
        <refreshMode>onInterval</refreshMode>
        <refreshInterval>3600</refreshInterval>
      </Link>
    </NetworkLink>
'''

# uždaryti Document ir KML
kml_content += '''  </Document>
</kml>'''

# įrašome index.kml
with open(index_file, "w", encoding="utf-8") as f:
    f.write(kml_content)

print(f"{index_file} sėkmingai sukurtas su {len(kml_files)} KML failais.")
