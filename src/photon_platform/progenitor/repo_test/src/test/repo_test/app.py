"""
run the main app
"""
from .repo_test import Repo_test


def run() -> None:
    reply = Repo_test().run()
    print(reply)
