import sublime, sublime_plugin

class CopyWordUnderCursor(sublime_plugin.WindowCommand):
	def run(self):       
		self.window.run_command("find_under_expand")          
		self.window.run_command("copy")
		

