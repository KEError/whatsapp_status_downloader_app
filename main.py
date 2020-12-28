import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
import os,time,datetime
from kivy.uix.image import Image
timez=datetime.datetime.now()
timez=str(timez)
dst = '/sdcard/keerrorbafus.support/'
dst2 = (dst+timez)
z=os.path.isdir('/sdcard/keerrorbafus.support')
if z==True :
	os.system('cp -rf /sdcard/WhatsApp/Media/.statuses /sdcard/keerrorbafus.support')
	os.rename('/sdcard/keerrorbafus.support/.statuses',dst2)	
else :
	os.mkdir('/sdcard/keerrorbafus.support')
	os.system('cp -rf /sdcard/WhatsApp/Media/.statuses /sdcard/keerrorbafus.support')
	os.rename('/sdcard/keerrorbafus.support/.statuses',dst2)
class mainApp(App):
    sound=SoundLoader.load('/sdcard/kivy/whatsapp_status_downloader_app/data/music.mp3')
    def build(self):
           return Image(source ='/sdcard/kivy/whatsapp_status_downloader_app/data/ok.png')
        
    
    if sound:
        sound.play()
    
        
mainApp().run()

