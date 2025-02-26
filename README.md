# Student Dropout Analysis

This tool calculates the dropout risk percentage based on students' marks and attendance. It takes the percentage of marks and attendance as input and applies the following formula to determine the dropout risk:

```sh
Risk = 100 - (marks × 0.5 + attendance × 0.5)
```

The tool also allows users to display student data in a table format with an option to delete entries.

## Features
- Input student marks and attendance to calculate dropout risk.
- Display student data in a tabular format.
- Delete student entries as needed.
- Uses Flask framework for calculations and data storage.

## Technologies Used
- **Flask**: Backend framework to handle calculations and data storage.
- **HTML/CSS**: For the front-end interface.
- **JavaScript**: To manage dynamic table updates.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd dropout-risk-calculator
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```sh
   python app.py
   ```
5. Open the browser and go to `http://127.0.0.1:5000/`.

## Usage
1. Enter marks and attendance percentages in the provided input fields.
2. View entered student data in the table.
3. Delete any student entry if needed.

## Future Enhancements
- Add machine learning-based dropout risk prediction.
- Implement user authentication for secure data access.
- Improve UI for better user experience.

## License
This project is open-source and available under the [MIT License](LICENSE).
