from dataclasses import dataclass
from typing import Dict, Any
from typing import List

@dataclass
class DataIngestionConfig:
    root_dir: str
    file_id: str
    output_filename: str

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]):
        """Create DataIngestionConfig from a dictionary."""
        return cls(
            root_dir=config_dict['root_dir'],
            file_id=config_dict['file_id'],
            output_filename=config_dict['output_filename']
        )

@dataclass
class DataIngestionPdfConfig:
    root_dir: str
    pdf_links: List[str]