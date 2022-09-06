from flask import Flask, request
from flask_cors import CORS

from docx import Document
from docx.shared import Pt
from docx2pdf import convert

import comtypes.client
import os

HEADLESS_WORD_MODE = 1
PDF_SAVE_MODE = 17

RESUME_CV_FONT_NAME = "Radian Book"
RESUME_CV_FONT_SIZE = 12

# Define paths for all application roles
SOFTWARE_ENGINEER_PATH__RESUME = "templates/resume/WPG_Software_Engineer.docx"
FRONT_END_ENGINEER_PATH__RESUME = "templates/resume/WPG_Front_End_Engineer.docx"
FULL_STACK_ENGINEER_PATH__RESUME = "templates/resume/WPG_Full_Stack_Engineer.docx"

SOFTWARE_ENGINEER_PATH__COVER_LETTER = "templates/cover_letter/WPG_Software_Engineer.docx"
FRONT_END_ENGINEER_PATH__COVER_LETTER = "templates/cover_letter/WPG_Front_End_Engineer.docx"
FULL_STACK_ENGINEER_PATH__COVER_LETTER = "templates/cover_letter/WPG_Full_Stack_Engineer.docx"

def get_abs_path(filename):
    return os.path.abspath(filename)

# Initialize Flask server
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

# Initialize Word Application in headless mode
word = comtypes.client.CreateObject('Word.Application')
word.Visible = HEADLESS_WORD_MODE

@app.route('/resume', methods=['GET']):
    return None

@app.route('/cv', methods=['GET'])
def generate_cover_letter():
    return None

if __name__ == '__main__':
    app.run()
