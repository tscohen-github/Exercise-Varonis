from pathlib import Path
from github import Github
import os
from dotenv import load_dotenv

ENV_PATH = os.path.join(Path(__file__).parent, ".env")

load_dotenv(ENV_PATH)


def is_private_repositories(token, repo_name):
    if not token:
        print("Error: Personal Access Token not found. Please set GITHUB_TOKEN environment variable.")
        exit()
    account = Github(token)
    repo = account.get_repo("tsofia-git/Exercise-Varonis-New")
    if not repo.private:
        print(f"The repository '{repo_name}' is currently PUBLIC. Changing to PRIVATE...")
        # repo.edit(private=True)
        print(f"The repository '{repo_name}' has been successfully changed to PRIVATE.")
    else:
        print(f"The repository '{repo_name}' is already PRIVATE.")


g_token = os.getenv('GITHUB_TOKEN')
g_repo_name = os.getenv('REPO_NAME')
is_private_repositories(g_token, g_repo_name)
