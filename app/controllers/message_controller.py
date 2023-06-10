from app.services.instagram_service import InstagramService
from app.services.youtube_service import YouTubeService

class MessageController:
    @staticmethod
    def process_message(message):
        link = message.get('link')
        if link:
            if 'instagram.com/reel/' in link:
                video_url = InstagramService.fetch_reels_video_url(link)
                if video_url:
                    file_path = InstagramService.download_reels_video(video_url)
                    if file_path:
                        return {'status': 'success', 'message': 'Video downloaded successfully', 'file_path': file_path}
            elif 'youtube.com/shorts/' in link:
                video_url = YouTubeService.fetch_shorts_video_url(link)
                if video_url:
                    file_path = YouTubeService.download_shorts_video(video_url)
                    if file_path:
                        return {'status': 'success', 'message': 'Video downloaded successfully', 'file_path': file_path}

        return {'status': 'error', 'message': 'Invalid link or unsupported platform'}
