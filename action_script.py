import os
import fettuccine
import sys
import logging
import pygit2

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
print("Command-line arguments:", sys.argv)
# Read the inputs from the environment variables
sub_action = sys.argv[1]
pattern = sys.argv[2]

def cut_branch():
    project = fettuccine.git.Git()
    new_branch_name = project.branches.create_minor_branch(pattern)
    remote = project._repo.remotes["origin"]
    github_token = os.environ['GITHUB_TOKEN']
    callbacks = pygit2.RemoteCallbacks(pygit2.UserPass(github_token, ''))
        
    # Set the credentials
    remote.credentials = callbacks

    # Push the branch
    refspec = f'refs/heads/{new_branch_name}'
    remote.push([refspec], callbacks=callbacks)
    logging.info(f"Branch {new_branch_name} pushed successfully!")

# Dispatch to the correct sub-action
if sub_action == 'cut-branch':
    cut_branch()
else:
    logging.error(f"Unknown sub-action: {sub_action}")
    sys.exit(1)
