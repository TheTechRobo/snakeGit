import time
from subprocess import Popen as p
import sys
from subprocess import PIPE
import os
    
def interactivity():
    """
    An interactive wrapper for pyGit
    """
    
    print("Interactivity is not programmed yet :'/")
def pyGit():
    """
    Small infotext
    """
    
    print("This is pyGit v.0.2.4-stable. It is currently unfinished.\nThanks for your interest! Check back later, it will probably have received some updates.")
    print("If you need syntax documentation, it is either at github.com/thetechrobo/PyGit/wiki OR you can just type help(pygit) into the console (after you have imported it).")
def commit(msg):
    """
    Commits with a message.
    Syntax: commit("message")
    Currently pyGit does not support Authoring and other Weird Git Stuff.
    pyGit assumes that YOU are the author.
    If you want to add this functionality, either add it yourself and Pull Request your changes, or request it in the Issues section.
    """
    
    print("Commiting message...")
    hi = p(["git", "commit", "-m", " pyGit Commit: %s" % msg], shell=False, stdout=PIPE, stderr=PIPE)
    ih = str(hi.communicate())
    print(''.join(ih)) 
def add(files):
    """
    Stages files to be commited.
    Syntax: add("files")
    Use as many files as you want, separated by a space.
    Please make it a string.
    If you want to add all files, use "."
    """
    
    print("Staging files...")
    ih = p(["git", "add", "%s" % files], shell=False, stdout=PIPE, stderr=PIPE)
    hi = str(ih.communicate())
    print(''.join(hi))
def stage(files):
    """
    Same as add()
    Syntax: stage("files")
    See add() documentation for more details.
    """
    
    add(files)
def push(remote, branch):
    """
    Pushes local commits to remote server.
    Syntax: push("branch", "remote")
    It will push all commits.
    Currently other args are not supported.
    """
    
    print("Pushing to branch %s, remote %s" % (branch, remote))
    yolo = p(["git", "push", remote, branch], shell=False, stdout=PIPE, stderr=PIPE)
    yol = str(str(str(yolo.communicate())))
    print(''.join(yol))
def pull(remote, branch):
    """
    Pulls from remote server.
    Syntax: pull("remote", "branch")
    It will pull from the remote repository.
    Currently other args are not supported.
    """
    
    print("Pulling commits from remote %s, branch %s..." % (remote, branch))
    ih = p(["git", "pull", remote, branch], shell=False, stdout=sys.stdout, stderr=sys.stdout)
    hi = str(ih.communicate())
    print(''.join(hi))
def allInOne(message, remote, branch):
    """
    Adds all files -- with add(".") --, commits with user-given message, pulls from remote, pushes to remote.
    Basically an allinone. Really useful.
    Syntax: allInOne("commit message", "remote name", "remote branch name")
    Currently args are not supported.
    """
    
    add(".")
    try:
        os.remove(".git/index.lock")
    except:
        pass
    commit(message)
    pull(remote=remote, branch=branch)
    push(remote=remote, branch=branch)
if __name__ == "__main__":
    
    interactivity()
