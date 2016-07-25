import sublime, sublime_plugin

class FindUnderInAllFiles(sublime_plugin.WindowCommand):
	def run(self):
		self.window.run_command("find_under_expand")
		self.window.run_command("slurp_find_string")
		self.window.run_command("slurp_replace_string")
		self.window.run_command('show_panel', {'panel': 'find_in_files'})

