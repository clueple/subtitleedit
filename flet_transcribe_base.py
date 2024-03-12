import flet as ft 
from flet import TextField, GridView, Page, Column, Row, ElevatedButton, Container, Markdown, Dropdown, TextStyle, FilePicker, Text
from deep_translator import GoogleTranslator as gt
from nltk.tokenize import word_tokenize as wt 
import nltk
import re
from pathlib import Path

"""backend stuff"""

"""element style"""
"""main app"""
def main(page:Page):

	"""theme settings"""
	page.title = f"Warren's Markdown"
	page.vertical_alignment = 'center'
	page.window_height = 108*6
	page.window_width = 135*6
	page.horizontal_alignment = "stretch"
	page.vertical_alignment = "center" 
	page.theme_mode = 'dark'

	"""events"""
	def pick_files_result(e: ft.FilePickerResultEvent):
		""" when the button, 'upoad_btn' is clicked, the text object, 'selected_fle' will show a string of certain values'  """
		# result path of FilePicker object, type = string
		rpath = str(e.files[0].path)
		# result size of FilePicker object, type = string
		rsize = str(e.files[0].size)
		# result name of FilePicker object, type = string
		rname = str(e.files[0].name)
		# show either, 'name', 'path', or 'size' of the FilePicker object in the text field, 'selected_file'
		selected_file.value = rpath
		# update the 'selected_file' text field 
		selected_file.update()
		# display the content of the selected file in a text field, 'preview_txt' based on the ressult path, 'rpath' of the selected file
		preview_txt.value = Path(rpath).read_text(encoding='utf-8')
		# update the preview text content
		preview_txt.update()

	
	"""elements"""
	# Define the file dialog (a FilePicker object), 'pick_files_dialog' with click event set to 'pick_files_result''
	pick_files_dialog = FilePicker(on_result= pick_files_result) 
	# add the dialog object to page.overlay
	page.overlay.append(pick_files_dialog)
	# define the text field, 'selected_file'
	selected_file = Text(selectable=True)
	# define the Text input field, 'preview_txt' to show the content of the selected file
	preview_txt = TextField(label='Preview Uploaded Content',hint_text='Your preview content' ,multiline=True, expand=True, border_color=ft.colors.BLUE,max_lines=10)

	
	# define the button (an ElevatedButton object) that restricts to upload '.txt' file, with the click event being set to utilize the pick_files_dialog's 'pick_files' method
	upload_btn = ElevatedButton(
		'Upload', 
		on_click= lambda _: pick_files_dialog.pick_files(
			allowed_extensions= ['srt', 'txt'],
			)
		)
	
	"""layout"""
	page.add(
		upload_btn,
		selected_file,
		preview_txt
		)
	page.update()


"""run the flet app"""
if __name__ == '__main__':
    ft.app(target=main)
