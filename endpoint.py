import requests
from PyPDF2 import PdfWriter

# Replace 'YOUR_ENDPOINT_URL' with the actual endpoint URL
endpoint_url = 'https://api.stackexchange.com/2.3/questions?site=stackoverflow&pagesize=50&sort=votes'

# Send a GET request to the endpoint to fetch the questions
response = requests.get(endpoint_url)

if response.status_code == 200:
    # Assuming the response is in JSON format
    data = response.json()

    if 'questions' in data:
        questions = data['questions'][:50]  # Fetch the first 50 questions

        # Create a PDF writer object
        pdf_writer = PdfWriter()

        # Generate the PDF with numbered questions
        for i, question in enumerate(questions, 1):
            pdf_writer.add_page()
            pdf_writer.drawString(10, 800, f'Question {i}: {question}')

        # Save the PDF to a file
        output_filename = 'questions.pdf'
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f'Successfully saved {len(questions)} questions in "{output_filename}".')
    else:
        print('The API response does not contain a "questions" key.')
else:
    print('Failed to fetch questions. Please check your endpoint URL.')
