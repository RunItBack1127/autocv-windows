# AutoCV
The backend of the app is built using [Flask](https://flask.palletsprojects.com), a lightweight microframework for standing up backends quickly.

## Implementation
Since the app is built specifically for the Windows platform, the backend depends extensively on WinAPI libraries and modules, specifically `comtypes`, for leveraging Microsoft Word headlessly for generating the resume and cover letter PDFs.

Although a more platform agnostic library (barring Linux) for doing so would have made the app more extensible and overall more portable, such as [docx2pdf](https://pypi.org/project/docx2pdf), it would have been impossible to configure Word to run without the UI - running Word with these resources would slow down the app significantly, especially for slower CPUs. For performance reasons, targeting Windows specifically for the first-class Word support, automation and otherwise, was determined to be overall the best option.

## Limitations
As mentioned previously, the app is configured specifically to run on Windows. However, the following operations are possible on the following operating systems:
| Platform | Initialization     | Invoke `GET /resume` | Invoke `GET /cv`   | Invoke `/copy`     |
| -------- | ------------------ | -------------------- | ------------------ | ------------------ |
| Windows  | :heavy_check_mark: | :heavy_check_mark:   | :heavy_check_mark: | :heavy_check_mark: |
| MacOS    | :heavy_check_mark: |                      |                    | :heavy_check_mark: |
| Linux    | :heavy_check_mark: |                      |                    | :heavy_check_mark: |

## Installation
Run the following commands in the `src/backend` directory:
### Windows
```
pip install virtualenv
virtualenv ENV_NAME
ENV_NAME\Scripts\activate
pip install -r requirements
python server.py
```

### OSX/Linux
```
pip install virtualenv
virtualenv ENV_NAME
source ENV_NAME/bin/activate
pip install -r requirements
python server.py
```
