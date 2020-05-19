import time
from subprocess import Popen as p
import sys
from subprocess import PIPE
def interactivity(DoIt):
    """
    An interactive wrapper for pyGit
    """
    if not DoIt:
        print("Ok, you aren't doing it.")
    else:
        print("Interactivity is not programmed yet :'/")
def pyGit():
    """
    Small infotext
    """
    print("This is pyGit v.0.2-stable. It is currently unfinished.\nThanks for your interest! Check back later, it will probably have received some updates.")
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
    hi = p(["git", "commit", "-m", " pyGit Commit: %s" % msg], shell=False, stdout=sys.stdout, stderr=sys.stdout)
    print("Attempted to commit message %s. Look above to see if it was successful, it will show you info just as it would show you without pyGit." % msg)
def add(files):
    """
    Stages files to be commited.
    Syntax: add("files")
    Use as many files as you want, separated by a space.
    Please make it a string.
    If you want to add all files, use "."
    """
    print("Staging files...")
    ih = p(["git", "add", "%s" % files], shell=False, stdout=sys.stdout, stderr=sys.stdout)
    print("Attempted to stage files %s. Look below to see if it was successful, if it failed it would show you details." % files)
def stage(files):
    """
    Same as add()
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
    yolo = p(["git", "push", remote, branch], shell=False, stdout=sys.stdout, stderr=sys.stdout)
    print("Attempted to push. Look to see if it was successful.")
def pull(remote, branch):
    """
    Pulls from remote server.
    Syntax: pull("remote", "branch")
    It will pull from the remote repository.
    Currently other args are not supported.
    """
    print("Pulling commits from remote %s, branch %s..." % (remote, branch))
    ih = p(["git", "pull", remote, branch], shell=False, stdout=sys.stdout, stderr=sys.stdout)
    print("Attempted to pull from remote %s, branch %s. Look below to see if it was successful, if it failed it would show you details." % (remote, branch))
def allInOne(message, remote, branch):
    """
    Adds all files -- with add(".") --, commits with user-given message, pulls from remote, pushes to remote.
    Basically an allinone. Really useful.
    Syntax: allInOne("commit message", "remote name", "remote branch name")
    Currently args are not supported.
    """
    add(".")
    commit(message)
    time.sleep(5)
    pull(remote=remote, branch=branch)
    push(remote=remote, branch=branch)
    print("All in One has completed. Check to see if it worked.")
if __name__ == "__main__":
    interactivity(True)
