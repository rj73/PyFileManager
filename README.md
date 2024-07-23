PyFileManager
PyFileManager is a simple file organizer script written in Python. It automatically categorizes and moves files from a specified directory into subdirectories based on their file types. This script is useful for organizing files in a cluttered directory into neatly categorized folders.

Features
Automatically sorts files into predefined categories:
Audio (.mp3, .wma, .aac)
Video (.mp4)
Document (.docx, .pdf)
Software (.exe, .apk)
Images (.jpg, .png)
Unknown file types
Handles files in both flat directories and nested subdirectories.
Prerequisites
Python 3.x
No external libraries required beyond Python's standard library.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/rj73/pyfilemanager.git
Navigate to the project directory:

bash
Copy code
cd pyfilemanager
No additional installation is needed since this script uses Python’s built-in libraries.

Usage
Modify the path variable in the script to the directory you want to organize.

Run the script:

bash
Copy code
python pyfilemanager.py
The script will:

Create folders for each file type category if they do not exist.
Move files from the specified directory into the corresponding folders based on their file extensions.
Example
If you have a directory with mixed files like audio files, videos, documents, etc., this script will organize them into respective folders (audio, video, document, software, images, unknown).

Important Notes
If you run the script multiple times, it will attempt to recreate folders and may raise an error if the folders already exist. Handle this by ensuring the script is only run when needed or add error handling for existing directories.
The script currently does not handle errors beyond basic file operations. Enhance it as needed for production use.
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve functionality or add features.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For questions or feedback, open an issue on GitHub or contact rajechmkumar73@gmail.com.
