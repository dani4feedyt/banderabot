from pytubefix import YouTube
from pytubefix.cli import on_progress

from moviepy.editor import *
import os
import shutil

import discord
import asyncio
from discord.ext import commands


class Player:
    def __init__(self, url=None):
        if url == None:
            self.url = url
        else:
            self.url = url

    url = ""
    audio_path = ""
    base_path = ""
    filename = ""
    root_folder = 'downloads'
    proxies = {
        "http": "106.75.211.112:1080" #####cвой айпи как прокси
    }

    async def download(self):
        yt = YouTube(self.url, proxies=self.proxies, allow_oauth_cache=True, on_progress_callback=on_progress, use_po_token=True, token_file = "verifier.json")
        t = yt.streams.filter().first()
        file = t.download("downloads")

        self.basePath, extension = os.path.splitext(file)

        video_f = VideoFileClip(os.path.join(self.basePath + ".mp4"))
        video_f.audio.write_audiofile(os.path.join(self.basePath + ".mp3"), verbose=False, logger=None)
        self.audio_path = os.path.abspath(f"{self.basePath}.mp3")

        self.filename = os.path.basename(self.audio_path)
        video_f.close()

    def flush_mp4(self):
        os.remove(os.path.join(self.basePath + ".mp4"))

    def flush_mp3(self):
        os.remove(os.path.join(self.basePath + ".mp3"))

    def flush_all(self):
        shutil.rmtree(self.root_folder)

    def get_audio_path(self):
        return self.audio_path

    def get_base_path(self):
        return self.base_path

    def get_filename(self):
        return self.filename

    def set_url(self, url):
        self.url = url

    async def stop(self, voice):
        voice.stop()
        await voice.disconnect()

    def length(self):
        import cv2
        v_path = os.path.join(self.basePath + ".mp4")
        print(v_path)
        video = cv2.VideoCapture(v_path)
        frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        fps = video.get(cv2.CAP_PROP_FPS)
        print(frames)
        print(fps)
        print(frames/fps)
        video.release()
        self.flush_mp4()

        return frames/fps
