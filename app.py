from flask import Flask, request, jsonify, render_template,send_file, session
import requests
import io
from youtube_transcript_api import YouTubeTranscriptApi
import os
from dotenv import load_dotenv
load_dotenv()


PORT = os.getenv('PORT', 5000)
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
if not YOUTUBE_API_KEY:
    raise ValueError("No YOUTUBE_API_KEY set for Flask application")


app = Flask(__name__)
app.secret_key = os.urandom(24)



@app.route('/download/<quality>')
def download_image(quality):
    url = session.get(f"thumbnail_{quality}")
    if url:
        response = requests.get(url)
        return send_file(
            io.BytesIO(response.content),
            mimetype='image/jpeg',
            as_attachment=True,
            download_name=f'youtube-thumbnail-{quality}.jpg'
        )

@app.route('/', methods=['GET', 'POST'])
def link():
    if request.method == 'POST':
        link = request.form['link']
        video_id = link.split('v=')[1]
        response = requests.get(
            f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={YOUTUBE_API_KEY}')
        
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        data = response.json()
        thumbnails = data['items'][0]['snippet']['thumbnails']
        thumbnail_urls = {
            'default': thumbnails['default']['url'],
            'high': thumbnails['high']['url'],
            'maxres': thumbnails['maxres']['url'],
        }
        session['thumbnail_default'] = thumbnails['default']['url']
        session['thumbnail_high'] = thumbnails['high']['url']
        session['transcript'] = transcript
        session['thumbnail_maxres'] = thumbnails['maxres']['url']
        session['transcript'] = transcript


        
        
        transcript = [
            {
                'text': item['text'],
                'start': round(item['start'], 2),
                'duration': round(item['duration'], 2)
            }
            for item in transcript
        ]
        
        # Store transcript in session
        session['transcript'] = transcript
        
        return render_template('index.html', thumbnails=thumbnail_urls, transcript=transcript)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
