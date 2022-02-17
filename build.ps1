# 删除旧的构建文件
$TargetFolder = ".\dist" 
$Files = get-childitem $TargetFolder -force
Foreach ($File in $Files){
    $FilePath=$File.FullName
    Remove-Item -LiteralPath $FilePath -Recurse -Force
}
# 构建
python setup.py sdist bdist_wheel
# 上传Pypi
twine upload dist/*