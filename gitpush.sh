cp -f .gitignore_aws .gitignore
cp -f credentials_aws.py credentials.py
git add credentials.py
git commit -m 'push'
git aws.push
cp -f .gitignore_github .gitignore
git rm credentials.py
git commit -m 'push'
git push origin master
