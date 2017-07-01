from __future__ import print_function
import time
import pychromecast

chromecasts = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if cc.device.friendly_name == "KLB")
cast.wait()

mc = cast.media_controller
mc.play_media('http://192.168.0.7:8000/BigBuckBunny.mp4', 'video/mp4')
mc.block_until_active()
time.sleep(20)
mc.stop()
