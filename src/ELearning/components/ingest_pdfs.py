import os
import gdown
import fitz
import json

class DataIngestionPDF:
    def __init__(self, config):
        self.config = config
        os.makedirs(self.config.root_dir, exist_ok=True)

    def download_pdf(self, file_id):
        pdf_file_path = os.path.join(self.config.root_dir, f'downloaded_{file_id}.pdf')
        gdown.download(f'https://drive.google.com/uc?id={file_id}', pdf_file_path, quiet=False)
        return pdf_file_path

    def extract_text_and_images(self, pdf_file):
        extracted_data = []
        doc = fitz.open(pdf_file)
        images_folder = os.path.join(self.config.root_dir, 'extracted_images')
        os.makedirs(images_folder, exist_ok=True)

        for page_number in range(len(doc)):
            page = doc[page_number]
            text = page.get_text()
            if text.strip():
                extracted_data.append({"page_number": page_number + 1, "text": text.strip(), "images": []})
                for img_index, img in enumerate(page.get_images(full=True)):
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_filename = f"page_{page_number + 1}_img_{img_index + 1}.png"
                    image_path = os.path.join(images_folder, image_filename)
                    with open(image_path, "wb") as img_file:
                        img_file.write(base_image["image"])
                    extracted_data[page_number]["images"].append(image_filename)
        doc.close()
        return extracted_data

    def initiate_data_ingestion(self):
        for file_id in self.config.pdf_links:
            pdf_path = self.download_pdf(file_id)
            extracted_data = self.extract_text_and_images(pdf_path)
            json_output_path = os.path.join(self.config.root_dir, f"extracted_data_{file_id}.json")
            with open(json_output_path, "w") as json_file:
                json.dump(extracted_data, json_file, indent=4)
            print(f"Extracted data for {file_id} saved to {json_output_path}")