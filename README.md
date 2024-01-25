PdfFileMerger
A simple Python script that merges two PDF files using the PyPDF2 library. The script appends the contents of samplePdf2.pdf to the end of samplePdf1.pdf and saves the result as mergedPdf.pdf.

Usage
Make sure you have the PyPDF2 library installed. You can install it using pip:

Copy code
pip install PyPDF2
Place the samplePdf1.pdf and samplePdf2.pdf files in the same directory as the script.

Run the script:

Copy code
python by_appending.py
The merged PDF file will be saved as mergedPdf.pdf in the same directory.

Testing
This script comes with a unit test that checks if the by_appending function is working correctly. To run the test, use the following command:

Copy code
python -m unittest test_by_appending.py
The test checks that the append method of the PdfFileMerger object is called twice, once for each PDF file, and that the write method is called once to save the merged PDF file.

Note
This script is just an example and should be adapted to fit your specific use case. You may want to add error handling, support for more than two PDF files, or other features.

License
This script is released under the MIT License. See the LICENSE file for more information.

Contact
If you have any questions or suggestions, please contact me at Tyrrickndungu@gmail.com
