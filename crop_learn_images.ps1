Add-Type -AssemblyName System.Drawing

$srcPath = "C:\Users\pathu\.gemini\antigravity-ide\brain\5c46c672-9c61-43e0-963e-05d5e9a987f5\.user_uploaded\media_1788801950803.png"
$src = [System.Drawing.Bitmap]::FromFile($srcPath)

function CropAndSave($name, $x, $y, $w, $h) {
    $rect = New-Object System.Drawing.Rectangle($x, $y, $w, $h)
    $crop = $src.Clone($rect, $src.PixelFormat)
    $crop.Save("site\public\images\$name", [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $crop.Save(".stitch\designs\images\$name", [System.Drawing.Imaging.ImageFormat]::Jpeg)
    $crop.Dispose()
    Write-Host "Saved $name ($w x $h)"
}

# 1. Landscape (Col 1 bottom - tight inside border)
CropAndSave "learn-mission.jpg" 50 274 202 114

# 2. Petunia Owner (Col 2 top - tight inside border)
CropAndSave "learn-owner.jpg" 294 84 200 114

# 3. Kiwis (Col 3 bottom - tight inside border)
CropAndSave "learn-mood.jpg" 536 284 200 114

# 4. Farm Fresh (Col 4 top - tight inside border)
CropAndSave "learn-farm.jpg" 778 94 200 126

$src.Dispose()
