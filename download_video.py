from pytube import YouTube

def download_youtube_video(url, save_path="."):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # 选择最高分辨率的视频
        print(f"Downloading: {yt.title}")
        stream.download(save_path)
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=ugkTDx3aCfk"  # 在这里替换成你的 YouTube 链接
    download_youtube_video(youtube_url, save_path="./")  # 保存到当前目录
    # leverage online website to download video
    # https://keepvid.online/zh13/