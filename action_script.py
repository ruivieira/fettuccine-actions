import os
import fettuccine
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Read the inputs from the environment variables
sub_action = os.environ.get('INPUT_SUB-ACTION')
pattern = os.environ.get('INPUT_PATTERN')

def cut_branch():
    project = fettuccine.git.Git()
    project.branches.create_minor_branch(pattern)
    

# Dispatch to the correct sub-action
if sub_action == 'cut-branch':
    cut_branch()
else:
    logging.error(f"Unknown sub-action: {sub_action}")
    sys.exit(1)
