from dataclasses import dataclass
from typing import List, Dict, Any

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
    
    
@dataclass
class MetadataConfig:
    root_dir: str
    pptx_file_name: str
    pdf_file_prefix: str

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]):
        return cls(
            root_dir=config_dict['root_dir'],
            pptx_file_name=config_dict['pptx_file_name'],
            pdf_file_prefix=config_dict['pdf_file_prefix']
        )

@dataclass
class ChunkingConfig:
    root_dir: str
    chunk_size: int
    pptx_chunk_filename: str
    pptx_metadata_filename: str
    pdf_chunk_filename_prefix: str
    pdf_metadata_filename_prefix: str

    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]):
        return cls(
            root_dir=config_dict['root_dir'],
            chunk_size=config_dict['chunk_size'],
            pptx_chunk_filename=config_dict['pptx_chunk_filename'],
            pptx_metadata_filename=config_dict['pptx_metadata_filename'],
            pdf_chunk_filename_prefix=config_dict['pdf_chunk_filename_prefix'],
            pdf_metadata_filename_prefix=config_dict['pdf_metadata_filename_prefix']
        )
