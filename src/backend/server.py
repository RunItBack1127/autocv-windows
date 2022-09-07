from flask import Flask, request, jsonify
from flask_cors import CORS

from docx import Document
from docx.shared import Pt
from docx2pdf import convert

from github import Github

import comtypes
import comtypes.client
import os
import uuid

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

SOFTWARE_ENGINEER_PATH__GENERATED_COVER_LETTER = "templates/cover_letter/generated/WPG_Software_Engineer.docx"
FRONT_END_ENGINEER_PATH__GENERATED_COVER_LETTER = "templates/cover_letter/generated/WPG_Front_End_Engineer.docx"
FULL_STACK_ENGINEER_PATH__GENERATED_COVER_LETTER = "templates/cover_letter/generated/WPG_Full_Stack_Engineer.docx"

def get_abs_path(filename):
    return os.path.abspath(filename)

# Initialize Flask server
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

github = Github("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")
repo = github.get_user().get_repo("autocv-cover-letters")

"""
    GET endpoint for populating the resume template,
    with options for modifying the languages and
    toggling the bottom skill between microservices
    and databases

    RETURNS the link to the generated resume PDF
    as retrieved from the GitHub REST API
"""
@app.route('/resume', methods=['GET'])
def generate_resume():
    return None

"""
    GET endpoint for populating the cover letter
    template with options for modifying the name of
    the hiring manager, the name of the role, and
    the company name

    RETURNS the link to the generated cover letter
    PDF  as retrieved from the GitHub REST API
"""
@app.route('/cv', methods=['GET'])
def generate_cover_letter():
    input_filename = ""
    output_filename = ""
    
    applicant_role = request.args["applicantRole"]
    if applicant_role == "Software Engineer":
        input_filename = SOFTWARE_ENGINEER_PATH__COVER_LETTER
        output_filename = SOFTWARE_ENGINEER_PATH__GENERATED_COVER_LETTER
    elif applicant_role == "Front End Engineer":
        input_filename = FRONT_END_ENGINEER_PATH__COVER_LETTER
        output_filename = FRONT_END_ENGINEER_PATH__GENERATED_COVER_LETTER
    elif applicant_role == "Full Stack Engineer":
        input_filename = FULL_STACK_ENGINEER_PATH__COVER_LETTER
        output_filename = FULL_STACK_ENGINEER_PATH__GENERATED_COVER_LETTER

    input_doc = Document(input_filename)

    norm_style = input_doc.styles['Normal']
    norm_font = norm_style.font

    norm_font.name = "Radian Book"
    norm_font.size = Pt(12)
    
    p__hiring_manager = input_doc.paragraphs[6]
    p__name_of_role = input_doc.paragraphs[7]
    p__company_name = input_doc.paragraphs[10]

    p__hiring_manager.text = p__hiring_manager.text.replace("{{HIRING_MANAGER}}", request.args["recruiterName"])

    nor_text = p__name_of_role.text.split("{{NAME_OF_ROLE}}")

    p__name_of_role.text = ""
    p__name_of_role.add_run(nor_text[0])
    p__name_of_role.add_run(request.args["nameOfRole"]).bold = True
    p__name_of_role.add_run(nor_text[1])

    p__company_name.text = p__company_name.text.replace("{{COMPANY_NAME}}", request.args["companyName"])

    input_doc.save(output_filename)
    pdf_filename = output_filename.replace(".docx", ".pdf")

    comtypes.CoInitialize()

    word = comtypes.client.CreateObject('Word.Application')
    word.Visible = False

    doc = word.Documents.Open(get_abs_path(output_filename))
    doc.SaveAs(get_abs_path(pdf_filename), FileFormat=PDF_SAVE_MODE)
    doc.Close()

    word.Quit()

    comtypes.CoUninitialize()

    github_pdf_path = f"Weston_P_Greene_Cover_Letter_{uuid.uuid4()}.pdf"
    pdf_contents = open(pdf_filename, "rb").read()
    github_response = repo.create_file(github_pdf_path, "Appending generated cover letter file", pdf_contents, branch="master")

    return jsonify(pdf=github_response['content'].download_url)

if __name__ == '__main__':
    app.run()
