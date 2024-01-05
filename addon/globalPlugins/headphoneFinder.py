# -*- coding: UTF-8 -*-
# Headphone Finder: """This add-on has two scripts, to beep to the left or the right, this can help you to find your bluetooth headphone.
# Copyright (C) 2023 - 2024 David CM
# Author: David CM <dhf360@gmail.com>
# Released under GPL 2
#globalPlugins/headphoneFinder.py

import globalPluginHandler, tones, addonHandler
from scriptHandler import script

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: script category for headphone finder add-on gestures
	scriptCategory = _("Headphone Finder")
	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.isPlaying = False

	def beep(self, left, right):
		freq = 2000
		duration = 300000
		if self.isPlaying:
			tones.beep(0, 0)
		else:
			tones.beep(freq, duration, left, right)
		self.isPlaying = not self.isPlaying

	@script(
		# Translators: plays a tone at the left.
		_("plays a tone at the left speaker."),
		gesture="kb:control+alt+NVDA+j")
	def script_findLeft(self, gesture):
		self.beep(100, 0)

	@script(
		# Translators: plays a tone at the right.
		_("plays a tone at the right speaker."),
		gesture="kb:control+alt+NVDA+k")
	def script_findRight(self, gesture):
		self.beep(0, 100)
