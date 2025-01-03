# YouTube Thumbnail Downloader

A simple web application built with Flask that allows users to download thumbnails from YouTube videos in different qualities.

**Try the application out here**

(Youtube Thumbnail Downloader)[]


## Prerequisites
- Python 3.7+
- pip (Python package installer)
- YouTube API Key

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/youtube-thumbnail-downloader.git
cd youtube-thumbnail-downloader
```
2. Install required packages
```
pip install -r requirements.txt
```

3. Create an `.env` file in the root directory and add your Youtube API Key:
`YOUTUBE_API_KEY=your_api_key_here`

## Running the application

1. Start the Flask server: 
```
python app.py
```
2. Open your web browser and navigate to:
`http://localhost:5000`

## Usage

1. Paste a YouTube video URL into the input field
2. Click "Get Thumbnails" button
3. Three thumbnail qualities will be displayed:
    - Default (120x90)
    - High Quality (480x360)
    - Maximum Resolution (1280x720)
## Features
- Support upport for multiple thumbnail qualities
- Direct download functionality
- Simple and intuitive interface
- Responsive design


## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
