import git
import sys
import os
from os.path import isfile, join
from os import listdir
import base64

############################


repo_path = str(sys.argv[1])
repo_url = str(sys.argv[2])
inputtag = str(sys.argv[3])

print(repo_path)
print(repo_url)
repo = git.Repo.clone_from(repo_url, repo_path)
print(repo)


def find_tag():
    print("Our input tag name",inputtag)
    taglist = repo.tags
    print(taglist)

    for i in range(len(taglist)):
        
        print(taglist[i])
        tagref = str(taglist[i])
        if inputtag == tagref:
            print("OK, tag match")
            print("Commit id related to tag ",taglist[i].commit)
            return taglist[i].commit
        else:
            print("Tag not found")

   
commitidfromtag = find_tag()
print (commitidfromtag)