# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class AddCaps(FilterWithoutDialog):
	
	def addCapToNodeInLayer(self, layer, node, capName):
		# add caps if present in font:
		font = layer.font()
		capGlyph = font.glyphs[capName]
		if font and node and capGlyph:
			cap = GSHint()
			cap.type = CAP
			cap.name = capName
			cap.originNode = node
			cap.setOptions_(3) # fit
			layer.addHint_(cap)
	
	def settings(self):
		self.menuName = "Add Caps"
		self.keyboardShortcut = None # With Cmd+Shift

	def filter(self, layer, inEditView, customParameters):
		if inEditView:
			Message(title="Add Caps Error", message="Filter parameter syntax: AddCaps; cap:_cap.xxx; 100,200; width-100,200", OKButton=None)
		# Apply your filter code here
		
		try:
			capName = customParameters["cap"]
			
			# n = Layer.nodeAtPoint_excludeNode_tollerance_(
			# 	NSPoint(60,0), None, 10
			# )
			
			for i,x in enumerate(customParameters):
				if x != "cap":
					pointInfo = customParameters[x].split(",")
					if len(pointInfo) != 2:
						print u"%s: Invalid point coordinate: '%s'" % (layer.parent.name, pointInfo)
					else:
						xInfo = pointInfo[0].strip().replace("width","%.1f"%layer.width)
						yInfo = pointInfo[1].strip().replace("width","%.1f"%layer.width)
						x=eval(xInfo)
						y=eval(yInfo)
						
						capNodePosition = NSPoint(x,y)
						if capNodePosition:
							node = layer.nodeAtPoint_excludeNode_tollerance_( capNodePosition, None, 10 )
							self.addCapToNodeInLayer(layer, node, capName)
						else:
							print u"%s: Could not find a node close to %i, %i" % (layer.parent.name, x, y)
		except Exception as e:
			import traceback
			print traceback.format_exc()
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	