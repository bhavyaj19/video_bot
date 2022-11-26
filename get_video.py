from moviepy.editor import *
import os
import random 
# import audio_files

dir_path = 'audio_files'
j=0
# files = len(os.listdir(dir_path))
# print(len(os.listdir(dir_path)))
for i in os.listdir(dir_path):
    audio_clip = AudioFileClip('audio_files/audio{}.mp3'.format(j))
    length = int(audio_clip.duration)
    video_clip = VideoFileClip('bg_video_files\minecraft{}.mp4'.format(random.randint(1,3))).subclip(0,length)
    final = video_clip.set_audio(audio_clip)
    final.write_videofile("final_video\output_video{}.mp4".format(j))

    j+=1