from config.api_keys import YOUTUBE_API_KEY
from app.utils.downloader import download_video
from app.utils.logger import logger
import requests

class YouTubeService:
    @staticmethod
    def fetch_shorts_video_url(link):
        try:
            # Make an API request to fetch the YouTube video details
            video_id = extract_video_id_from_link(link)
            api_url = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={YOUTUBE_API_KEY}&part=snippet'
            response = requests.get(api_url)
            if response.status_code == 200:
                # Extract the video URL from the response JSON
                video_url = extract_video_url_from_response(response.json())
                return video_url
            else:
                logger.error(f'Failed to fetch YouTube Shorts video URL. Status Code: {response.status_code}')
        except requests.exceptions.RequestException as e:
            logger.error(f'Error occurred while fetching YouTube Shorts video URL: {str(e)}')

        return None

    @staticmethod
    def download_shorts_video(url):
        try:
            # Specify the output directory where the video will be downloaded
            output_dir = 'downloads/youtube'
            # Download the video using the downloader utility
            file_path = download_video(url, output_dir)
            return file_path
        except Exception as e:
            logger.error(f'Error occurred while downloading YouTube Shorts video: {str(e)}')

        return None

def extract_video_id_from_link(link):
    if 'youtu.be' in link:
        # Extract the video ID from the shortened YouTube link
        video_id = link.split('/')[-1]
    else:
        # Extract the video ID from the regular YouTube link
        video_id = link.split('v=')[-1].split('&')[0]
    return video_id

def extract_video_url_from_response(response_json):
    try:
        # Extract the video URL from the response JSON
        video_url = response_json['items'][0]['snippet']['thumbnails']['maxres']['url']
        return video_url
    except KeyError:
        logger.error('Failed to extract video URL from YouTube API response JSON')
    return None
