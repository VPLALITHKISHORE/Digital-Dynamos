import os

def convert_to_html(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<title>MCQ Quiz</title>\n</head>\n<body>\n<form id='quiz-form'>"

    question_number = 1
    answers = {}
    for line in lines:
        line = line.strip()
        if line:
            if line.startswith("Q"):
                html_content += f"<p><strong>{line}</strong></p>\n"
            elif line.startswith("(a)"):
                html_content += f"<input type='radio' name='question_{question_number}' value='a'>{line}</input><br>\n"
            elif line.startswith("(b)"):
                html_content += f"<input type='radio' name='question_{question_number}' value='b'>{line}</input><br>\n"
            elif line.startswith("(c)"):
                html_content += f"<input type='radio' name='question_{question_number}' value='c'>{line}</input><br>\n"
            elif line.startswith("(d)"):
                html_content += f"<input type='radio' name='question_{question_number}' value='d'>{line}</input><br>\n"
            elif line.startswith("Correct Answer:"):
                correct_answer = line.split(":")[1].strip().lower()
                answers[f"question_{question_number}"] = correct_answer
                html_content += f"<input type='hidden' name='answer_{question_number}' value='{correct_answer}'>\n"
                html_content += "<hr>\n"
                question_number += 1
            elif line.startswith("(") and line.endswith(")"):
                question_number += 1

    html_content += "<input type='submit' value='Submit' id='submit-btn' style='display:none;'></form>\n"
    html_content += "<script>"
    html_content += "function checkAllAnswered() {"
    for i in range(1, question_number):
        html_content += f"if (!document.querySelector('input[name=\"question_{i}\"]:checked')) {{return false;}}"
    html_content += "return true;"
    html_content += "}"
    html_content += "document.getElementById('quiz-form').addEventListener('change', function() {"
    html_content += "if (checkAllAnswered()) {document.getElementById('submit-btn').style.display = 'block';}"
    html_content += "else {document.getElementById('submit-btn').style.display = 'none';}"
    html_content += "});"
    html_content += "</script>"
    html_content += "</body>\n</html>"

    with open(output_file, 'w') as f:
        f.write(html_content)

    return answers

# Paths
input_file = r"C:\Users\balag\OneDrive\Documents\StudentpdfOutput\extracted_text.txt"
output_file = r"D:\webpages\quiz.html"

# Create the output directory if it doesn't exist
output_dir = os.path.dirname(output_file)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Convert to HTML and get answers
answers = convert_to_html(input_file, output_file)
print(f"HTML file '{output_file}' generated successfully.")

# Print answers for debugging
print("Answers:")
for key, value in answers.items():
    print(f"{key}: {value}")
