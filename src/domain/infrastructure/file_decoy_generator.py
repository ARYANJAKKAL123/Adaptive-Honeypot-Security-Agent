# src/infrastructure/file_decoy_generator.py
from faker import Faker
from datetime import datetime
import os
from ..interfaces.decoy_generator import IDecoyGenerator
from ..entities.decoy import Decoy

class FileDecoyGenerator(IDecoyGenerator):
    """
    Implements IDecoyGenerator using Faker library
    Creates realistic fake files and writes them to the file system
    """
    
    def __init__(self):
        """Initialize the file decoy generator with Faker"""
        self.faker = Faker()
    
    def create_credential_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake credential file with realistic passwords and usernames
        
        Args:
            file_path: Where to place the decoy file
            
        Returns:
            Decoy object with fake credential content
        """
        # Generate fake credentials using Faker
        content = f"""# Credentials File
# DO NOT SHARE - CONFIDENTIAL

Username: {self.faker.user_name()}
Password: {self.faker.password(length=12, special_chars=True)}

Admin Username: {self.faker.user_name()}
Admin Password: {self.faker.password(length=16, special_chars=True)}

Database User: {self.faker.user_name()}
Database Password: {self.faker.password(length=20, special_chars=True)}

API Key: {self.faker.uuid4()}
Secret Token: {self.faker.sha256()}
"""
        
        # Write to file system
        self._write_to_file(file_path, content)
        
        # Return Decoy object
        return Decoy(
            decoy_type="credential",
            file_path=file_path,
            content=content,
            created_at=datetime.now()
        )
    
    def create_document_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake document file with realistic text
        
        Args:
            file_path: Where to place the decoy file
            
        Returns:
            Decoy object with fake document content
        """
        # Generate fake document using Faker
        content = f"""CONFIDENTIAL REPORT
Date: {self.faker.date()}
Author: {self.faker.name()}
Department: {self.faker.job()}

SUMMARY:
{self.faker.paragraph(nb_sentences=5)}

DETAILS:
{self.faker.text(max_nb_chars=500)}

FINANCIAL DATA:
Revenue: ${self.faker.random_number(digits=7)}
Expenses: ${self.faker.random_number(digits=6)}
Profit Margin: {self.faker.random_int(min=10, max=40)}%

CONTACT INFORMATION:
Email: {self.faker.email()}
Phone: {self.faker.phone_number()}
Address: {self.faker.address()}
"""
        
        # Write to file system
        self._write_to_file(file_path, content)
        
        # Return Decoy object
        return Decoy(
            decoy_type="document",
            file_path=file_path,
            content=content,
            created_at=datetime.now()
        )
    
    def create_config_decoy(self, file_path: str) -> Decoy:
        """
        Generate a fake configuration file with database/API settings
        
        Args:
            file_path: Where to place the decoy file
            
        Returns:
            Decoy object with fake config content
        """
        # Generate fake config using Faker
        content = f"""# Database Configuration
# PRODUCTION SETTINGS - DO NOT MODIFY

database:
  host: {self.faker.ipv4()}
  port: {self.faker.random_int(min=3000, max=9999)}
  username: {self.faker.user_name()}
  password: {self.faker.password(length=16)}
  database_name: {self.faker.word()}_production

api:
  endpoint: https://{self.faker.domain_name()}/api/v1
  api_key: {self.faker.uuid4()}
  secret_key: {self.faker.sha256()}
  
security:
  encryption_key: {self.faker.sha256()}
  jwt_secret: {self.faker.uuid4()}
  
admin:
  email: {self.faker.email()}
  backup_email: {self.faker.email()}
"""
        
        # Write to file system
        self._write_to_file(file_path, content)
        
        # Return Decoy object
        return Decoy(
            decoy_type="config",
            file_path=file_path,
            content=content,
            created_at=datetime.now()
        )
    
    def _write_to_file(self, file_path: str, content: str):
        """
        Write content to file system
        
        Args:
            file_path: Path to write to
            content: Content to write
        """
        # Create directory if it doesn't exist
        directory = os.path.dirname(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        # Write content to file
        with open(file_path, 'w') as f:
            f.write(content)
