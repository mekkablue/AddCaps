# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
# Filter without dialog Plugin
#
# Read the docs:
# https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

import objc
from GlyphsApp import Glyphs, GSHint, CAP, Message
from GlyphsApp.plugins import FilterWithoutDialog
from AppKit import NSPoint


class AddCaps(FilterWithoutDialog):

	@objc.python_method
	def addCapToNodeInLayer(self, layer, node, capName):
		# add caps if present in font:
		font = layer.font()
		capGlyph = font.glyphs[capName]
		if font and node and capGlyph:
			cap = GSHint()
			cap.type = CAP
			cap.name = capName
			cap.originNode = node
			cap.setOptions_(3)  # fit
			layer.addHint_(cap)

	@objc.python_method
	def settings(self):
		self.menuName = "Add Caps"
		self.keyboardShortcut = None  # With Cmd+Shift

	@objc.python_method
	def filter(self, layer, inEditView, customParameters):
		if inEditView:
			Message(
				title="Add Caps cannot run in Edit view",
				message="In Font Info > %s, add a ‘Filter’ parameter, and as value, enter a string with the following syntax:\nAddCaps; cap:_cap.xxx; 100,200; width-100,200\nSee GitHub Readme for more details." % (
					"Styles" if Glyphs.versionNumber >= 3.0 else "Instances",
				),
				OKButton=None,
			)
			return
		try:
			capName = customParameters["cap"]
			for i, x in enumerate(customParameters):
				if x == "cap":
					continue

				pointInfo = customParameters[x].split(",")
				if len(pointInfo) != 2:
					print(u"%s: Invalid point coordinate: '%s'" % (layer.parent.name, pointInfo))
					continue

				xInfo = pointInfo[0].strip().replace("width", "%.1f" % layer.width)
				yInfo = pointInfo[1].strip().replace("width", "%.1f" % layer.width)
				x = eval(xInfo)
				y = eval(yInfo)

				capNodePosition = NSPoint(x, y)
				if capNodePosition:
					try:
						# GLYPHS 3
						node = layer.nodeAtPoint_excludeNode_ignoreLocked_tolerance_(
							capNodePosition,
							None,
							True,
							10,
						)
					except:
						# GLYPHS 2
						node = layer.nodeAtPoint_excludeNode_tollerance_(
							capNodePosition,
							None,
							10,
						)
					self.addCapToNodeInLayer(layer, node, capName)
				else:
					print(u"%s: Could not find a node close to %i, %i" % (layer.parent.name, x, y))
		except Exception as e:
			import traceback
			print(traceback.format_exc())

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
