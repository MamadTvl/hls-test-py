import m3u8
from src.request import RequestsClient
import threading
import re


from src.simulate import Simulate
m3u8Url = 'https://vod.linom.org/media/General-physics-2/10-1VvBCfmp2DS/lq/playlist.m3u8'
playlist = m3u8.load(m3u8Url, http_client=RequestsClient())


threads = []
for i in range(4000):
    simulation = Simulate(segments=playlist.data['segments'], baseUrl=re.sub(
        '/playlist.m3u8', '', m3u8Url), label=f'worker_{i + 1}')
    thread = threading.Thread(target=simulation.run)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()