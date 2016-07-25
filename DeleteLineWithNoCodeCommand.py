#########################
import sublime, sublime_plugin
import re

class DeleteLineWithNoCodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sublime.status_message("JindraDelete: Started")					
		flags = 0
		for region in self.view.sel():  
			if not region.empty():
				self.view.replace(edit, region, "")
				sublime.status_message("JindraDelete: Deleted selection")		
			else:
				line = self.view.substr(self.view.line(region))
				match = re.search("(.*?)(\s+$)", line, flags)
				cursorPosition = self.view.sel()[0]
				wholeLineWithCursor = self.view.line(self.view.sel()[0])

				if match and cursorPosition.a != wholeLineWithCursor.a:
					self.view.replace(edit, wholeLineWithCursor, match.group(1))
					sublime.status_message("JindraDelete: Deleted Empty space at and of line!!")
				else:
					match = re.search("^\s*$", line, flags)
					if match:			
						sublime.status_message("JindraDelete: matched empty line")			
						region.a = region.a-1
						self.view.replace(edit, region, "")
						sublime.status_message("JindraDelete: Deleted Empty Line!!")
					else:
						sublime.status_message("JindraDelete: No match 2 - deleting one character")
						region.a = region.b - 1
						self.view.replace(edit, region, "")


   
						
						# 123456789
						# 123456789
						# 123456789
						# 123456789
						# 123456789





						# // { "keys": ["backspace"], "command": "delete_line_with_no_code", "context":
						# // 	[
						# // 		{ "key": "selection_empty", "operator": "equal", "operand": true, "match_all": true },
						# // 	]
						# // },