import unittest
from io import BytesIO
from PyPDF2 import PdfFileMerger, PdfFileReader
from your_module import by_appending

class TestPdfMerger(unittest.TestCase):
    def test_by_appending(self):
        # Create a mock PdfFileMerger object
        merger_mock = self.create_autospec(PdfFileMerger)

        # Replace the real PdfFileMerger with the mock object
        PdfFileMerger = merger_mock

        # Call the function being tested
        by_appending()

        # Check that the append method was called twice
        merger_mock.append.assert_has_calls([
            call(PdfFileReader(BytesIO(b"content of samplePdf1"))),
            call("samplePdf2.pdf")
        ])

        # Check that the write method was called once
        merger_mock.write.assert_called_once_with("mergedPdf.pdf")

if __name__ == '__main__':
    unittest.main()