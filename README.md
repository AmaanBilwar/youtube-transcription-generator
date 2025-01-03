# YouTube Thumbnail & Transcript Generator

A Flask web application that allows users to:
- Download YouTube video thumbnails in multiple qualities
- Get complete video transcription
- Download transcription as text file

## Prerequisites
- Python 3.7+
- pip (Python package installer)
- YouTube API Key
- Internet connection

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/youtube-tools.git
cd youtube-tools
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
4. Click "Get Transcription" button to get the video transcription
5. Click "Download Transcription" button to download the transcription as a text file (work in progress)

## Features
- Support for multiple thumbnail qualities
- Direct download functionality
- Simple and intuitive interface
- Responsive design
- Video transcription and download functionality

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request
