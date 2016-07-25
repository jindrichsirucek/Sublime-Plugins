import sublime, sublime_plugin,re

class OnErrorWhileBuildingProjectViewEventListener(sublime_plugin.EventListener):
	def on_selection_modified(self, view):#def on_activated(self, view): #def on_selection_modified(self, view):

		sublime.status_message("vstup do panelu")

		line = view.substr(view.line(view.sel()[0]))
		sublime.status_message("selected")

		sublime.status_message("line substring: " + str(line))

		match = re.search("(^.*):(\d+):(\d+):.* error: (.*$)", line, 0)
		if match:
			fileName = match.group(1)
			rowError = match.group(2)
			colError = match.group(3)
			errorText = match.group(4)
			(rowError, colError) = (int(rowError)-2, int(colError)-2)
			
			sublime.status_message("matched: " + str(fileName))
			
			errorFileView = view.window().open_file(fileName)
			sublime.status_message("opened file: " + str(errorFileView))

			errorFileView.sel().clear()
			errorFileView.sel().add(sublime.Region(errorFileView.text_point(rowError, colError)))

			errorFileView.show(errorFileView.text_point(rowError, colError))

			sublime.status_message("selected: " + str(rowError))
			groupNumber = errorFileView.window().get_view_index(errorFileView)[0]
			errorFileView.window().focus_group(groupNumber)
			sublime.status_message("Error: Focused: " + str(errorText))			

			# sublime.status_message("Error: end: " + str(errorText))

			













