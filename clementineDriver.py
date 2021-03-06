# -*- coding: utf-8 -*-

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pydbus as dbus
import sys

class Clementine:
  
	def __init__(self):
		self.bus = dbus.SessionBus()
		#try:
			#self.server = self.bus.get_object('org.mpris.clementine', '/Player')
			#self.tracklist = self.bus.get_object('org.mpris.clementine', '/TrackList')
			##qdbus org.mpris.clementine /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Pause 
			#self.mpris2 = self.bus.get_object('org.mpris.clementine', '/org/mpris/MediaPlayer2')
			#self.mpris2player = dbus.Interface(self.mpris2, dbus_interface='org.mpris.MediaPlayer2.Player')
		#except:
			#print "Clementine is not running? Exiting..."
			#sys.exit(-1)
		
		# Handle exception in http.py
		self.mpris = self.bus.get('org.mpris.MediaPlayer2.clementine', '/org/mpris/MediaPlayer2')
		#self.player = dbus.Interface(self.mpris, dbus_interface='org.mpris.MediaPlayer2.Player')
		#self.tracklist = dbus.Interface(self.mpris, dbus_interface='org.mpris.MediaPlayer2.TrackList')
		#self.propertiesManager = dbus.Interface(self.mpris, 'org.freedesktop.DBus.Properties')
	
	def Next(self):
		self.mpris.Next()
		return True
  
	def Prev(self):
		self.mpris.Previous()
		return True
    
	def Play(self):
		self.mpris.Play()
		return True
	
	def Stop(self):
		self.mpris.Stop()
		return True
		
	def Pause(self):
		self.mpris.Pause()
		return True
	
	def GetInfo(self):
		return self.mpris.Metadata
		#return self.propertiesManager.Get('org.mpris.MediaPlayer2.Player', 'Metadata')
	
	def GetCover(self):
		metadata = self.mpris.Metadata
		if 'arturl' not in metadata:
			return 0
		else:
			return metadata['arturl']
	
	def VolumeUp(self):
		self.mpris.Volume = min(100, self.mpris.Volume + 10)
		return True
	
	def VolumeDown(self):
		self.mpris.Volume = max(0, self.mpris.Volume - 10)
		return True
	
	def GetTrackNum(self):
		metadata = self.mpris.Metadata
		if 'trackid' not in metadata:
			return 0
		else:
			return metadata['trackid']
	
	def GetListLength(self):
		return len(self.mpris.Tracks)
	
	def GetTrackData(self,trackNumber):
		return ""
		#return self.tracklist.GetTracksMetadata([trackNumber])[0]
	
	def setNewTrack(self,trackNumber):
		self.mpris.GoTo(trackNumber)
	
	def removeTrack(self,trackNumber):
		self.mpris.RemoveTrack(trackNumber)
	
	def loadTrackList(self,url):
		self.mpris.OpenUri(url)
		
	def setShuffle(self,mode):
		self.mpris.Shuffle = mode
		
	def getShuffle(self):
		return self.mpris.Shuffle
		
	def setRepeat(self,mode):
		self.mpris.LoopStatus = mode
		
	def getRepeat(self):
		return self.mpris.LoopStatus
		
		
		
		
		
	
	#@dbus.service.method(dbus.PROPERTIES_IFACE, in_signature='ss', out_signature='v')
#def Get(self, interface, prop):
    #...
#@dbus.service.method(dbus.PROPERTIES_IFACE, in_signature='ssv')
#def Set(self, interface, prop, value):
    #...
#@dbus.service.method(dbus.PROPERTIES_IFACE, in_signature='s', out_signature='a{sv}')
#def GetAll(self, interface):
    #...
    
    
    
    #- -----------------
    
    #proxy = bus.get_object('org.mpris.MediaPlayer2.rhythmbox','/org/mpris/MediaPlayer2')
#properties_manager = dbus.Interface(proxy, 'org.freedesktop.DBus.Properties')
#properties_manager.Set('org.mpris.MediaPlayer2.Player', 'Volume', 100.0)
#curr_volume = properties_manager.Get('org.mpris.MediaPlayer2.Player', 'Volume')