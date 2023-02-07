'''
面试题目
'''
import requests
import os
import ffmpy
from datetime import datetime


class interface:

    dt01 = datetime.today()

    def down_video(self, url):
        '''
        下载视频到本地
        '''
        tar_folder = 'video'
        filename = 'temp'+self.dt01.date()+'-'+self.dt01.second+'.mp4'
        video_path = tar_folder + '/' + filename

        # 建立目标文件夹
        if not os.path.exists(tar_folder):
            os.makedirs(tar_folder, exist_ok=True)

        # 下载
        res = requests.get(url, stream=True)
        with open(video_path, 'wb') as f1:
            for chunk in res.iter_content(chunk_size=102400):
                f1.write(chunk)
        return video_path

    def cut_video(self, filename, start, end):
        '''
        剪辑视频
        '''
        name = self.down_video(filename)
        # 判断文件夹中是否存在这个文件
        if not os.path.exists(name):
            # 如果不存在直接返回null
            return

        outpath = 'video/output'+self.dt01.date()+'-'+self.dt01.second+'.mp4'

        try:
            # 如果存在那么可以进行剪辑
            ff = ffmpy.FFmpeg(
                inputs={'name': None},
                outputs={outpath: [
                    '-ss', start,
                    '-t', end,
                    '-vcodec',
                    'copy',
                    '-acodec',
                    'copy'
                ]}
            )

            ff.run()
        except Exception as e:
            print(e)
        # 剪辑后的文件可以进行返回
        return outpath
