rm -rf ./zzpy.egg-info
rm -rf ./dist
python setup.py sdist
twine upload dist/*
rm -rf ./zzpy.egg-info
rm -rf ./dist
git add *
git commit -m "release"
git push origin master
# pip3 install zzpy --upgrade -i https://pypi.org/simple