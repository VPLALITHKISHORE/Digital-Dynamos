# Digital-Dynamos

## Prototype Drive Link
      -- https://drive.google.com/file/d/1zcsOL9arxRbZaUpUnsy_TpshNiMcTb7J/view?usp=sharing

1. **Files:**
   - `index.html`: This is the HTML file where users can upload either a PDF or an image file.
   - `server.js`: This file is executed using Node.js (`node server`) to start the server.
   - `pharse.py`: Python script containing OCR (Optical Character Recognition) code to extract text from PDF or image files.
   - `pytohtml.py`: Python script to convert text extracted from PDF or image into HTML.
   
2. **Server Setup:**
   - Start the server by running `node server` in the terminal.
   
3. **User Interaction:**
   - Open `index.html` in a web browser.
   - The webpage allows users to upload a PDF or image file.

4. **File Storage:**
   - When the user submits the file, it gets stored on the server's local filesystem at a specified location.

5. **Text Extraction:**
   - Once the file is saved, the path to the saved file is passed to `pharse.py`.
   - `pharse.py` utilizes OCR to extract text from the uploaded PDF or image.
   - The extracted text is then saved to a text file in a different location on the system.

6. **HTML Conversion:**
   - The path to the text file containing extracted text is passed to `pytohtml.py`.
   - `pytohtml.py` converts the extracted text into HTML format, possibly with additional formatting or structure.
   - The resulting HTML file is named `quiz.html`.

7. **Quiz Generation:**
   - `quiz.html` now represents a simple MCQ (Multiple Choice Questions) based test website.
   - Upon running `quiz.html` in a browser, users can take the generated quiz.

8. **Further Improvements:**
   - Additional features or improvements can be made to the generated quiz website, such as styling, interactivity, or backend functionalities.
