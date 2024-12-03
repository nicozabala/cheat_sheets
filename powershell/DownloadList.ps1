# List of URLs to download
$urls = @(
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2633-1102/swisssurface3d-raster_2021_2633-1102_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2633-1103/swisssurface3d-raster_2021_2633-1103_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2633-1104/swisssurface3d-raster_2021_2633-1104_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2633-1105/swisssurface3d-raster_2021_2633-1105_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2633-1106/swisssurface3d-raster_2021_2633-1106_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2634-1102/swisssurface3d-raster_2021_2634-1102_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2634-1103/swisssurface3d-raster_2021_2634-1103_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2634-1104/swisssurface3d-raster_2021_2634-1104_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2634-1105/swisssurface3d-raster_2021_2634-1105_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2634-1106/swisssurface3d-raster_2021_2634-1106_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2635-1102/swisssurface3d-raster_2021_2635-1102_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2635-1103/swisssurface3d-raster_2021_2635-1103_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2635-1104/swisssurface3d-raster_2021_2635-1104_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2635-1105/swisssurface3d-raster_2021_2635-1105_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2635-1106/swisssurface3d-raster_2021_2635-1106_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2636-1102/swisssurface3d-raster_2021_2636-1102_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2636-1103/swisssurface3d-raster_2021_2636-1103_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2636-1104/swisssurface3d-raster_2021_2636-1104_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2636-1105/swisssurface3d-raster_2021_2636-1105_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2636-1106/swisssurface3d-raster_2021_2636-1106_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2637-1102/swisssurface3d-raster_2021_2637-1102_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2637-1103/swisssurface3d-raster_2021_2637-1103_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2637-1104/swisssurface3d-raster_2021_2637-1104_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2637-1105/swisssurface3d-raster_2021_2637-1105_0.5_2056_5728.tif",
    "https://data.geo.admin.ch/ch.swisstopo.swisssurface3d-raster/swisssurface3d-raster_2021_2637-1106/swisssurface3d-raster_2021_2637-1106_0.5_2056_5728.tif"
)

# Destination folder for the downloaded files
$destinationFolder = "C:\Downloads"

# Ensure the destination folder exists
if (!(Test-Path -Path $destinationFolder)) {
    New-Item -ItemType Directory -Path $destinationFolder
}

# Loop through each URL and download the file
foreach ($url in $urls) {
    $fileName = Split-Path -Leaf $url
    $destinationPath = Join-Path -Path $destinationFolder -ChildPath $fileName
    Write-Host "Downloading $fileName..."
    Invoke-WebRequest -Uri $url -OutFile $destinationPath
    Write-Host "Saved to $destinationPath"
}

Write-Host "All downloads complete!"
