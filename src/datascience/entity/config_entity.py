from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass
class DataIngestionConfig:
    """
    Configuration for data ingestion process.
    
    Attributes:
        root_dir (Path): Path to store the raw data file.
        processed_data_path (Path): Path to store the processed data file.
        source_url (str): URL of the data source.
    """
    root_dir: Path
    local_data_file: Path
    source_URL: str
    unzip_dir: Path