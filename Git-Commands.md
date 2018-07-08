### When there is an error
```xcode-select --install```

### Connect to Github
```git clone https://github.com/vamshi-indla/AV-Big-Mart-Sales.git```

### Adding a file
```git add file.r```

### Shows comparison with github
```git status```

### Pushes code from desktop to github
```git push```

### to save the change in github
```git commit -m "Add comments"```

### Copies from github to Desktop
```git pull```

## Contribute to Other's repo 
1. Fork a repo
2. clone my repo to local 
```git clone https://github.com/vamshi-indla/image_to_text.git```

3. Go to repo
```cd image_to_text/```

**Keeping Your Fork Up to Date**
4. establish link with source repo, Add 'upstream' repo to list of remotes
```git remote add upstream https://github.com/UPSTREAM-USER/ORIGINAL-PROJECT.git```

__Verify the new remote named 'upstream'__
git remote -v

**Way to update my fork**
5. Fetch from upstream remote
```git fetch upstream```

View all branches, including those from upstream
```git branch -va```

6. Now, checkout your own master branch and merge the upstream repo's master branch:
# Checkout your master branch and merge upstream::
git checkout master
git merge upstream/master

**Create a branch to enhance or apply fix**
7. Checkout the master branch - you want your new branch to come from master
```git checkout master```

Create a new branch named newfeature (give your branch its own simple informative name)
```git branch newfeature```

Switch to your new branch
```git checkout newfeature```


**Fetch upstream master and merge with your repo's master branch**::
git fetch upstream
git checkout master
git merge upstream/master

**If there were any new commits, rebase your development branch**
git checkout newfeature
git rebase master

8. Publish your changes
git commit  -m "message" app.py
git push

9. Then go to github and do "pull request", provide comments.

## References: 
https://www.youtube.com/watch?v=0fKg7e37bQE
https://gist.github.com/Chaser324/ce0505fbed06b947d962


#----------------------------------------------------
## Creating Web Applications
- Refer Flask, Django
- [Example](https://github.com/rishab-sharma/ocr_on_android)


- Refer pyramid package
pkg_resources.get_distribution("construct").version
#----------------------------------------------------
