from subprocess import Popen as p
import sys
from subprocess import PIPE
def commit(msg):
    """
    Syntax: commit("message")
    Currently pyGit does not support Authoring and other Weird Git Stuff.
    pyGit assumes that YOU are the author.
    If you want to add this functionality, either add it yourself and Pull Request your changes, or request it in the Issues section.
    """
    print("Commiting message...")
    hi = p(["git", "commit", "-m", " pyGit Commit: %s" % msg], shell=False, stdout=PIPE, stderr=PIPE)
    ih = hi.communicate()
    print(ih)
    print("Attempted to commit message %s. Look above to see if it was successful, it will show you info just as it would show you without pyGit." % msg)
def add(files):
    """
    Syntax: add("files")
    Use as many files as you want, separated by a space.
    Please make it a string.
    If you want to add all files, use "."
    """
    print("Staging files...")
    ih = p(["git", "add", "%s" % files], shell=False, stdout=PIPE, stderr=PIPE)
    hi = ih.communicate()
    print(hi)
    print("Attempted to stage files %s. Look above to see if it was successful, if it failed it would show you details." % files)
def push(branch, remote):
    """
    Syntax: push(branch, remote)
    It will push all commits.
    Currently other args are not supported.
    """
    print("Pushing to branch %s, remote %s" % (branch, remote))
    yolo = p(["git", "push", branch, remote], shell=False, stdout=PIPE, stderr=PIPE)
    theCommunication = yolo.communicate()
    print(theCommunication)
if __name__ == "__main__":
    print("Interactivity is not yet supported.")