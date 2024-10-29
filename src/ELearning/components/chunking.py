import os
import json
import datetime
from src.ELearning.entity.config_entity import ChunkingConfig

class DataChunking:
    def __init__(self, config: ChunkingConfig):
        self.config = config
        os.makedirs(self.config.root_dir, exist_ok=True)

    def load_json_data(self, json_path):
        with open(json_path, 'r') as json_file:
            return json.load(json_file)

    def create_chunks(self, text, chunk_size):
        return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    def create_chunk_metadata(self, source_file, chunked_data):
        metadata = {
            "source_file": source_file,
            "chunking_date": str(datetime.datetime.now()),
            "number_of_chunks": len(chunked_data),
            "details": [{"chunk_index": idx, "chunk_length": len(chunk)} for idx, chunk in enumerate(chunked_data)]
        }
        return metadata

    def save_chunks_and_metadata(self, source_file, text, chunk_filename, metadata_filename):
        chunks = self.create_chunks(text, self.config.chunk_size)
        
        chunked_path = os.path.join(self.config.root_dir, chunk_filename)
        with open(chunked_path, 'w') as chunked_file:
            json.dump(chunks, chunked_file, indent=4)
        
        metadata = self.create_chunk_metadata(source_file, chunks)
        metadata_path = os.path.join(self.config.root_dir, metadata_filename)
        with open(metadata_path, 'w') as metadata_file:
            json.dump(metadata, metadata_file, indent=4)
        
        return chunked_path, metadata_path
