from abc import ABC, abstractmethod
from ..entities.decoy import Decoy


class IDecoyGenerator(ABC):
    """
    Interface that defines how decoys should be generated
    Any class that generates decoys must implement these methods.
    """

    @abstractmethod
    def create_credential_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake credential file (password, keys, etc.)

        Args:
            file_path: Where to place the decoy file.

        Returns:
            Decoy object with fake credential content.
        """
        pass

    @abstractmethod
    def create_document_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake document file (reports, notes, etc.)

        Args:
            file_path: Where to place the decoy file.

        Returns:
            Decoy object with fake document content.
        """
        pass

    @abstractmethod
    def create_config_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake config file (database config, API, etc.)

        Args:
            file_path: Where to place the decoy file.

        Returns:
            Decoy object with fake config content.
        """
        pass
        
