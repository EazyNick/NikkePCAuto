import os
from functools import cached_property
from deploy.config import DeployConfig
from utils import logger


class GitSyncError(Exception):
    """Custom exception for Git synchronization errors."""
    pass


class GitManager(DeployConfig):
    """
    Singleton class to manage GitHub repository synchronization.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GitManager, cls).__new__(cls)
        return cls._instance

    @cached_property
    def git(self):
        return self.filepath("GitExecutable")

    def execute_git_command(self, command):
        """
        Execute a git command.

        Args:
            command (str): The git command to execute.

        Returns:
            bool: True if the command succeeds, False otherwise.
        """
        command = command.replace("\\", "/").replace('"', "'")
        logger.info(f"Executing command: {command}")
        result = os.system(command)
        if result != 0:
            raise GitSyncError(f"Git command failed: {command}")
        return True

    def sync_repository(self):
        """
        Synchronize the local repository with the remote GitHub repository.
        """
        try:
            # Initialize the repository if not already initialized
            logger.hr("Initializing repository", 1)
            if not os.path.exists("./.git"):
                self.execute_git_command(f'"{self.git}" init')

            # Set up remote URL
            logger.hr("Setting up remote URL", 1)
            self.execute_git_command(f'"{self.git}" remote add origin {self.Repository}')

            # Fetch and synchronize
            logger.hr("Fetching and synchronizing", 1)
            self.execute_git_command(f'"{self.git}" fetch origin {self.Branch}')
            self.execute_git_command(f'"{self.git}" reset --hard origin/{self.Branch}')
            logger.hr("Repository synchronized successfully", 1)
        except GitSyncError as e:
            logger.error(f"Git synchronization error: {e}")
            raise


class GitSyncStrategy:
    """
    Strategy class to synchronize Git repositories using different methods.
    """
    def sync(self, manager: GitManager):
        """
        Synchronize the repository.
        """
        raise NotImplementedError


class DefaultGitSyncStrategy(GitSyncStrategy):
    """
    Default strategy to synchronize the Git repository.
    """
    def sync(self, manager: GitManager):
        manager.sync_repository()


# Example Usage
if __name__ == "__main__":
    git_manager = GitManager()
    sync_strategy = DefaultGitSyncStrategy()

    try:
        sync_strategy.sync(git_manager)
    except Exception as e:
        logger.error(f"Failed to synchronize repository: {e}")
