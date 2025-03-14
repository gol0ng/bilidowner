# 爬取B站的视频 Bilibili
# B站的视频地址是直接存储在源网页中的，因此只需要从源网页中解析即可
import glob
import os
import requests
import json
import re
import os
import time
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from bs4 import BeautifulSoup
from notice import show_notification
def merge_video_and_audio(video_path, audio_path, output_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    merged_clip = video_clip.with_audio(audio_clip)
    merged_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    merged_clip.close()
    video_clip.close()
def get_video(url):
    url = url
    # 设置请求头
    header = {
        "User-Agent": "",
        "Referer": "https://www.bilibili.com/",  # 设置防盗链
        "Cookie":""# 有Cookie可以下载更高质量视频， 没有也可以下载
    }

    resp = requests.get(url=url, headers=header)
    soup = BeautifulSoup(resp.text, 'html.parser')
    tittle = soup.find('meta', attrs={'name': 'title'})
    tittle = tittle['content'][:-14]
    obj = re.compile(r'window.__playinfo__=(.*?)</script>', re.S)
    html_data = obj.findall(resp.text)[0]  # 从列表转换为字符串

    json_data = json.loads(html_data)
    videos = json_data['data']['dash']['video']  # 这里得到的是一个列表
    video_url = videos[0]['baseUrl']  # 视频地址
    audios = json_data['data']['dash']['audio']
    audio_url = audios[0]['baseUrl']
    show_notification('莫小荒','已获取链接，正在下载')
    # 下载视频
    resp1 = requests.get(url=video_url, headers=header)
    with open('output.mp4', mode='wb') as f:
        f.write(resp1.content)
        f.close()
    # 下载音频
    resp2 = requests.get(url=audio_url, headers=header)
    with open('output.mp3', mode='wb') as f:
        f.write(resp2.content)
        f.close()
    time.sleep(0.5)
    merge_video_and_audio('output.mp4', 'output.mp3', "./video/"+tittle+'.mp4')
    time.sleep(0.5)
    show_notification('莫小荒','下载完成!')
    os.remove('output.mp3')
    # 指定要操作的目录路径
    directory = "./"

    # 使用glob模块匹配目录下所有的.mp4文件，并返回一个列表
    mp4_files = glob.glob(os.path.join(directory, "*.mp4"))

    # 遍历找到的所有.mp4文件，并使用os.remove()函数删除它们
    for file in mp4_files:
        os.remove(file)
        print(f"Deleted: {file}")
