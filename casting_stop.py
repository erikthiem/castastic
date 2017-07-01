from __future__ import print_function
import time
import pychromecast

chromecasts = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if cc.device.friendly_name == "KLB")
cast.wait()

mc = cast.media_controller
mc.stop()
