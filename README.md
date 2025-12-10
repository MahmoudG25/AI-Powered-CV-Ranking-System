# AI CV Screening Application

An intelligent candidate evaluation system powered by OpenAI that analyzes CVs, ranks candidates, and generates professional emails for top candidates.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-5.2.8-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-orange)

## Features

- 🤖 **AI-Powered Evaluation**: Uses OpenAI GPT-4o-mini to analyze candidate CVs
- 📊 **Intelligent Ranking**: Automatically ranks candidates based on job requirements
- 📧 **Email Generation**: Creates personalized congratulatory emails for top candidates
- 🎨 **Modern UI**: Beautiful glassmorphism design with smooth animations
- 📄 **PDF Support**: Extracts text from PDF CVs automatically
- 💯 **Fit Scoring**: Provides 0-100 fit scores with detailed analysis
- ✅ **Strengths & Gaps**: Identifies candidate strengths and skill gaps

## Screenshots

### Upload Page
Modern file upload interface with drag-and-drop support

### Results Page
Candidate rankings with color-coded scores and detailed analysis

## Tech Stack

- **Backend**: Django 5.2.8
- **AI**: OpenAI GPT-4o-mini
- **PDF Processing**: PyPDF2
- **Frontend**: Bootstrap 5, Vanilla JavaScript
- **Styling**: Custom CSS with glassmorphism effects

## Installation

### Prerequisites

- Python 3.13+
- OpenAI API Key

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/MahmoudG25/AI-Powered-CV-Ranking-System.git
   cd AI-Powered-CV-Ranking-System            
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   
   Open your browser and navigate to: `http://localhost:8000/`

## Usage

1. **Enter Job Details**
   - Fill in the job title
   - Describe the job requirements and qualifications

2. **Upload CVs**
   - Upload 1-5 PDF files containing candidate CVs
   - Drag and drop or click to browse

3. **Analyze**
   - Click "Analyze with AI"
   - Wait for the AI to process the CVs

4. **Review Results**
   - View ranked candidates with fit scores
   - Review strengths and gaps for each candidate
   - See the generated email for the top candidate

## Project Structure

```
AI-Powered-CV-Ranking-System/
├── core/                      # Django project settings
│   ├── settings.py           # Main settings
│   └── urls.py               # Root URL configuration
├── recruiter/                 # Main application
│   ├── ai/
│   │   └── evaluator.py      # AI evaluation logic
│   ├── models.py             # Database models
│   ├── views.py              # View logic
│   ├── urls.py               # App URL configuration
│   ├── static/
│   │   └── css/              # Static CSS files
│   │       ├── base.css      # Base styles
│   │       ├── upload.css    # Upload page styles
│   │       └── results.css   # Results page styles
│   └── templates/
│       └── recruiter/        # HTML templates
│           ├── base.html     # Base template
│           ├── upload.html   # Upload page
│           └── results.html  # Results page
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Configuration

### OpenAI Settings

The application uses GPT-4o-mini by default. You can modify the model in `recruiter/ai/evaluator.py`:

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Change model here
    messages=[...]
)
```

### File Upload Limits

Modify upload limits in `recruiter/views.py`:

```python
if len(files) < 1 or len(files) > 5:  # Change max files here
    return render(request, "recruiter/upload.html", {
        "error": "Please upload between 1 and 5 CVs."
    })
```

## API Key Setup

1. Get your OpenAI API key from: https://platform.openai.com/api-keys
2. Add it to your `.env` file
3. Never commit your `.env` file to version control

## Development

### Running Tests

```bash
python manage.py test
```

### Accessing Admin Panel

1. Create a superuser (see Installation step 6)
2. Navigate to: `http://localhost:8000/admin/`
3. View uploaded CVs and their extracted text

## Troubleshooting

### Static Files Not Loading

If CSS files aren't loading:
```bash
python manage.py collectstatic
```

### OpenAI API Errors

- Verify your API key is correct in `.env`
- Check your OpenAI account has credits
- Ensure the API key has proper permissions

### PDF Extraction Issues

- Ensure PDFs are text-based (not scanned images)
- Try re-saving the PDF with text layer
- Check file size isn't too large

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- OpenAI for GPT-4o-mini API
- Django framework
- Bootstrap for UI components
- PyPDF2 for PDF processing

## Support

For issues and questions:
- Open an issue on GitHub
- Contact: [mahmoud.gado2002@gmail.com]

---

**Note**: This is a development application. For production use, ensure proper security measures, environment configuration, and deployment best practices.
