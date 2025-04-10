from flask import Flask, send_file, request, make_response
import os

app = Flask(__name__)

# Path to your exe file
EXE_FILE_PATH = "readme.exe"  # Replace with your actual exe file path


@app.route('/download_exe', methods=['GET'])
def download_file():
    custom_filename = request.args.get('filename', 'name.exe')

    # Make sure the filename has the .exe extension
    if not custom_filename.lower().endswith('.exe'):
        custom_filename += '.exe'

    # Ensure the file exists
    if not os.path.exists(EXE_FILE_PATH):
        return "File not found", 404

    # Create a response with the file
    response = make_response(send_file(
        EXE_FILE_PATH,
        as_attachment=True,
        download_name=custom_filename
    ))

    # Set appropriate headers for exe file
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = f'attachment; filename="{custom_filename}"'

    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)