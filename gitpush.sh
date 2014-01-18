cp -f .gitignore_aws .gitignore
git add credentials.py
git commit -m 'push'
git aws.push
cp -f .gitignore_github .gitignore
git rm credentials.py
git commit -m 'push'
git push origin master
