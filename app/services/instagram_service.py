from config.api_keys import INSTAGRAM_API_KEY
from app.utils.downloader import download_video
from app.utils.logger import logger
import requests

class InstagramService:
    @staticmethod
    def fetch_reels_video_url(link):
        headers = {'Authorization': f'Bearer {INSTAGRAM_API_KEY}'}
        try:
            response = requests.get(link, headers=headers)
            if response.status_code == 200:
                # Extract the video URL from the response content
                video_url = extract_video_url_from_response(response.content)
                return video_url
            else:
                logger.error(f'Failed to fetch Instagram Reels video URL. Status Code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            logger.error(f'Error occurred while fetching Instagram Reels video URL: {str(e)}')

        return None

    @staticmethod
    def download_reels_video(url):
        try:
            # Specify the output directory where the video will be downloaded
            output_dir = 'downloads/instagram'
            # Download the video using the downloader utility
            file_path = download_video(url, output_dir)
            return file_path
        except Exception as e:
            logger.error(f'Error occurred while downloading Instagram Reels video: {str(e)}')

        return None

def extract_video_url_from_response(response_content):
    start_marker = '<meta property="og:video" content="'
    end_marker = '" />'
    start_index = response_content.find(start_marker)
    if start_index != -1:
        start_index += len(start_marker)
        end_index = response_content.find(end_marker, start_index)
        if end_index != -1:
            video_url = response_content[start_index:end_index]
            return video_url
    return None