# For saving game data
import os
from util.terminaloutput.symbols import INFO_SYMBOL, ERROR_SYMBOL, info, error
from util.terminaloutput.erasing import erase_previous_lines

SAVE_DIR_PATH = "saved_games/"


def path_to_save_file(filename):
	"""Returns the path to the corresponding save file"""
	return f"{SAVE_DIR_PATH}{filename}"


def allow_save(filepath: str):
	"""Returns whether we can save at the specified location"""
	if not filepath.startswith(SAVE_DIR_PATH):
		error(f"Save file must be in {SAVE_DIR_PATH}")
		return False
	if os.path.exists(filepath):
		with open(filepath, 'r') as saveFile:
			try:
				time_of_previous_save = saveFile.readlines()[3].strip()
				overwrite = input(f"{INFO_SYMBOL} A save state already exists from {time_of_previous_save}.\nIs it okay to overwrite it? (y/n)\t").strip().lower()
				erase_previous_lines(1)
				while overwrite not in ['y', 'n']:
					erase_previous_lines(1)
					overwrite = input(f"{ERROR_SYMBOL} Invalid input. Is it okay to overwrite the existing save state? (y/n)\t").strip().lower()
				erase_previous_lines(1)
				if overwrite == 'n':
					info("The current game state will not be saved.")
					return False
			except IndexError:
				return True
	return True
