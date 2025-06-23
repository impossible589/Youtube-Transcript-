from flask import Flask, send_from_directory , request
from flask_cors import CORS
from yt_dlp import YoutubeDL
from youtube_transcript_api import YouTubeTranscriptApi
app = Flask(__name__, static_folder='static')
CORS(app)




@app.route('/')
def serve_index():
    return "server-ready"
@app.route('/tes')
def servt():
     ydl_opts = {
    'skip_download': True,
    'writesubtitles': True,
    'writeautomaticsub': True,
    'quiet': True,
    'sleep_interval': 2,
    'max_sleep_interval': 5,
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
        'Accept-Language': 'en-US,en;q=0.9',
    }
}   
     with YoutubeDL(opts) as ydl:
        data =ydl.download(['https://www.youtube.com/watch?v=cUlharo8sPQ'])


     return data


@app.route('/loaderio-6eb9bf95da20f05ae75ff6a724761fb3.txt')
def servetest():
    return send_from_directory(app.static_folder,'loaderio-6eb9bf95da20f05ae75ff6a724761fb3.txt')
@app.route('/test')
def serve_index2():
    return send_from_directory(app.static_folder, 'test.jpeg')
@app.route("/langq")
def langq():
    fullurl = request.args.get('yurl')
    sl = fullurl.split("e/", 1)
    sl2 = sl[1]
    fs = sl2.split("?", 1)
    print(fs[0])
    video_id = fs[0]  # Replace with your actual YouTube video ID
    langl = YouTubeTranscriptApi.list_transcripts(video_id);
    listforreturn = ""
    for t in langl:
        listforreturn = listforreturn+t.language+"*"+t.language_code +":"

    return listforreturn
@app.route('/api/hello')
def hello():
    return {"message": "Hello from Python backend"}

@app.route("/trans")
def home():
    fullurl =  request.args.get('yurl')
    langcode = request.args.get('lang')
    sl = fullurl.split("e/",1)
    sl2 = sl[1]
    fs = sl2.split("?",1)
    print(fs[0])
    video_id = fs[0]  # Replace with your actual YouTube video ID
    #lang = request.args.get('lang')
    print("language=="+langcode);

    try:
        # Step 2: Fetch the transcript (default language is auto-selected)
       
        #print(avlang)
        transcript = YouTubeTranscriptApi.get_transcript(video_id,languages=[langcode])  # you can also try ['en', 'hi'] for fallback

        # Step 3: Display the transcript line by line
        lines=""
        for entry in transcript:
            lines = lines + (f"{entry['start']:.2f}s - {entry['text']}"+"<br>")

    except Exception as e:
        print("❌ Error fetching transcript:", e)
    return lines








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
