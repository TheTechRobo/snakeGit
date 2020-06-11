import time
from subprocess import Popen as p
import sys
from subprocess import PIPE
import os
import functools
import operator

class interactivity:
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
    Commits staged changes.
    - The message argument is completely optional (it commits with the --allow-empty-message flag).
    Syntax: commit("message")
    Currently pyGit does not support Authoring and other Weird Git Stuff.
    pyGit assumes that YOU are the author.
    If you want to add this functionality, either add it yourself and Pull Request your changes, or request it in the Issues section.
    """
    if msg == "":
        print("Commiting...")
        hi = p(["git", "commit", "-m" "pyGit Commit"], shell=False, stdout=PIPE, stderr=PIPE)
    else:
        print("Commiting with message %s..." % msg)
        hi = p(["git", "commit", "-m" "pyGit Commit: %s" % msg], shell=False, stdout=PIPE, stderr=PIPE)
    ih = hi.communicate()
    hi, _ = ih
    ih = hi.decode('UTF-8') #https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
    print(ih)
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
    hi = ih.communicate()
    _, ih = hi
    hi = ih.decode("UTF-8")
    try:
        print(functools.reduce(operator.add, (hi)))
    except: #if there was no output
        pass
def stage(files):
    """
    Same as add()
    Syntax: stage("files")
    See add() documentation for more details.
    """
    add(files)
def push(remote="", branch=""):
    """
    Pushes local commits to remote server.
    Syntax:
    - If you have set the default upstream for the current branch already, just push() will be sufficient.
    - But, if you choose where to push commits (or the default has not been set), use push("remote", "branch").
    Currently other args are not supported.
    """
    if remote == "":
        print("Pushing to upstream default.")
        yolo = p(["git", "push"], shell=False, stdout=PIPE, stderr=PIPE)
    elif branch == "":
        print("Pushing to upstream default.")
        yolo = p(["git", "push"], shell=False, stdout=PIPE, stderr=PIPE)
    else:
        print("Pushing to branch %s, remote %s" % (branch, remote))
        yolo = p(["git", "push", remote, branch], shell=False, stdout=PIPE, stderr=PIPE)
    yol = yolo.communicate()
    _, ih = yol
    yol = ih.decode("UTF-8")
    print(''.join(yol))
def pull(remote, branch):
    """
    Pulls from remote server.
    Syntax: pull("remote", "branch")
    It will pull from the remote repository.
    Currently other args are not supported.
    """
    if remote == "":
        print("Pulling commits from upstream default.")
        ih = p(["git", "pull"], shell=False, stdout=PIPE, stderr=PIPE)
    elif remote == "":
        print("Pulling commits from upstream default.")
        ih = p(["git", "pull"], shell=False, stdout=PIPE, stderr=PIPE)
    else:
        print("Pulling commits from remote %s, branch %s..." % (remote, branch))
        ih = p(["git", "pull", remote, branch], shell=False, stdout=sys.stdout, stderr=sys.stdout)
    hi = ih.communicate()
    ih, _ = hi
    hi = ih.decode("UTF-8")
    print(''.join(hi))
def allInOne(message="", remote="", branch=""):
    """
    Adds all files -- with add(".") --, commits with user-given message, pulls from remote, pushes to remote.
    Basically an allinone. Really useful.
    - If the default upstream has not been set or you want to use a different one, you must specify branch name and remote name, e.g. allInOne(remote="origin", branch="master")
    - The commit message is optional, and as long as you are OK with the upstream branch (if it is set) you don't need to specify branch name and remote name.
    - All in all: allInOne("commit message (optional)", remote="remote name (optional)", branch="remote branch name (optional)")
    Currently args are not supported.
    """
    add(".")
    try:
        os.remove(".git/index.lock")
    except:
        time.sleep(2)
        try:
            os.remove(".git/index.lock")
        except:
            pass
    commit(message)
    pull(remote=remote, branch=branch)
    push(remote=remote, branch=branch)
if __name__ == "__main__":
    interactivity()
