# Get Unlocked Courses

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python must be installed on your system.  
  👉 [Download Python here](https://www.python.org/downloads/)

### Installation

1. **Download the project**  
   Click the green **"Code"** button, download the ZIP file, and extract it to any folder.

2. **Install dependencies**  
   Open a terminal in the extracted folder and run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download your grade report**  
   Go to your student portal, navigate to **Grade Reports → By Curriculum**, and click **Print** to download the PDF file.

4. **Move the PDF file**  
   Copy the downloaded PDF to the same folder where the script is located.

5. **Update the file path in `main.py`**  
   Open `main.py` and set the file path to the name of your downloaded PDF:
   ```python
   # Path to your PDF file
   pdf_path = "your_file_name.pdf"
   ```
   For example:
   ```python
   # Path to your PDF file
   pdf_path = "GradeReportByCurriculumXX-XXXXX-X.pdf"
   ```

6. **Run the application**  
   In the terminal, start the app by running:
   ```bash
   python main.py
   ```
   Or, if needed:
   ```bash
   python3 main.py
   ```
