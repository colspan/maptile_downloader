# maptile_downloader
Map Tile Downloader based on Luigi

## install

```
sudo ./setup.py install
```

## examples

``` bash
# around Sapporo 電子国土基本図（オルソ画像） https://maps.gsi.go.jp/development/ichiran.html#ort
maptile_downloader --baseUrl=http://cyberjapandata.gsi.go.jp/xyz/ort/{z}/{x}/{y}.jpg --baseName=sapporo --west=140.78704833984375 --north=43.18715513581086 --south=42.627896481020855 --east=141.998291015625 --zoom=15 --workers=4

# around Tokachi 電子国土基本図（オルソ画像） https://maps.gsi.go.jp/development/ichiran.html#ort
maptile_downloader --baseUrl=http://cyberjapandata.gsi.go.jp/xyz/ort/{z}/{x}/{y}.jpg --baseName=tokachi --west=142.74810791015625 --north=43.25320494908846 --south=42.21224516288584 --east=143.72589111328125 --zoom=15 --workers=4

# around Tokyo 電子国土基本図（オルソ画像） https://maps.gsi.go.jp/development/ichiran.html#ort
maptile_downloader --baseUrl=http://cyberjapandata.gsi.go.jp/xyz/ort/{z}/{x}/{y}.jpg --baseName=kanto --west=139.559326171875 --north=35.77994251888403 --south=35.36217605914681 --east=140.2569580078125 --zoom=15 --workers=4

# around Sapporo 国土画像情報（第一期：1974～1978年撮影） https://maps.gsi.go.jp/development/ichiran.html#ort
maptile_downloader --baseUrl=http://cyberjapandata.gsi.go.jp/xyz/gazo1/{z}/{x}/{y}.jpg --baseName=1974sapporo --west=140.78704833984375 --north=43.18715513581086 --south=42.627896481020855 --east=141.998291015625 --zoom=15 --workers=4

# around Tokachi 国土画像情報（第一期：1974～1978年撮影） https://maps.gsi.go.jp/development/ichiran.html#ort
maptile_downloader --baseUrl=http://cyberjapandata.gsi.go.jp/xyz/gazo1/{z}/{x}/{y}.jpg --baseName=1974tokachi --west=142.74810791015625 --north=43.25320494908846 --south=42.21224516288584 --east=143.72589111328125 --zoom=15 --workers=4

# around Tokyo 国土画像情報（第一期：1974～1978年撮影） https://maps.gsi.go.jp/development/ichiran.html#ort
maptile_downloader --baseUrl=http://cyberjapandata.gsi.go.jp/xyz/gazo1/{z}/{x}/{y}.jpg --baseName=1974kanto --west=139.559326171875 --north=35.77994251888403 --south=35.36217605914681 --east=140.2569580078125 --zoom=15 --workers=4
```

