import os
import requests
from app.utils.logger import logger

def download_video(url, output_dir):
    try:
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Extract the filename from the URL
        filename = url.split("/")[-1]
        file_path = os.path.join(output_dir, filename)

        # Download the video
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        logger.info(f"Video downloaded successfully. File path: {file_path}")
        return file_path

    except Exception as e:
        logger.error(f"Error occurred while downloading video: {str(e)}")
        return None
