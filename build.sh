rm -rf ./zzpy.egg-info
rm -rf ./dist
python setup.py sdist
twine upload dist/*
rm -rf ./zzpy.egg-info
rm -rf ./dist
pip3 install zzpy --upgrade -i https://pypi.org/simple
