# Article Downloader

This script allows users to input a URL of an article or webpage and download its content as a PDF.

## Details

The script leverages the following Python libraries:
- `pdfkit`: A Python wrapper for converting HTML to PDF using the webkit rendering engine and `wkhtmltopdf`.
- `requests`: To send HTTP requests and validate the given URL.
- `os`: To interact with the operating system.

**Dependencies**:
- `pdfkit`
- `requests`
- Additionally, the `wkhtmltopdf` command line tool must be installed and available in the system's PATH for `pdfkit` to function properly.

## Features
- URL validation to ensure the provided link is accessible.
- Converts a valid webpage or article URL to a downloadable PDF.
- Basic error handling for better user experience.

## Getting Started

1. Clone this repository: git clone https://github.com/Bisalkumar/Article-Downloader.git
2. Navigate to the directory containing the script.
3. Install the necessary Python libraries: pip install pdfkit requests
4. Ensure that `wkhtmltopdf` is installed and available in the system's PATH.

## How to Use

1. Run the script: python Article_Dwonloader.py
2. Enter the URL of the article or webpage when prompted.
3. If the URL is valid, the content will be downloaded as a PDF named `output.pdf` in the current directory.

## Screenshots

![Sample(1).png](Sample%20(1).png) ![Sample(2).png](Sample%20(2).png)

## Contributions

Contributions are welcome! Please fork this repository and create a Pull Request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgements

- Developers of `pdfkit` and `requests` for their amazing libraries.