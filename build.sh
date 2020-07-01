python setup.py sdist
twine upload dist/*
rm -rf ./zzpy.egg-info
rm -rf ./dist