rm -rf ./zzpy.egg-info
rm -rf ./dist
python setup.py sdist
twine upload dist/* --repository pypi
twine upload dist/* --repository private
rm -rf ./zzpy.egg-info
rm -rf ./dist
git add *
git commit -m "release"
git push origin master