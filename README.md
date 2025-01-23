## Still a work in progress btw (im not a frontend guy)

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
git clone https://github.com/AmaanBilwar/youtube-transcription-generator
cd youtube-transcription-generator
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

Thumbnail:
1. Start the application:
Open browser and go to: `http://localhost:5000`

2. Paste YouTube URL

Transcription:

Automatically generates complete video transcript
View timestamp-synchronized text
Download full transcript as text file

## Features

1. Thumbnails:

    - Paste YouTube URL
    - View thumbnails in high resolution
    - Download with one click
2. Transcription:
    - Automatically generates complete video transcript
    - View timestamp-synchronized text
    - Download full transcript as text file(work in progress)


## Technologies
- Flask
- YouTube Data API
- YouTube Transcript API
- Python Requests
