'''
面试题目
'''
import requests
import os

class interface:

    def down_video(url):
        '''
        下载视频到本地
        '''
        tar_folder = 'video'
        filename = 'temp.mp4'
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
