$TargetFolder = ".\dist" 
$Files = get-childitem $TargetFolder -force
Foreach ($File in $Files){
    $FilePath=$File.FullName
    Remove-Item -LiteralPath $FilePath -Recurse -Force
}
python setup.py sdist bdist_wheel
twine upload dist/*