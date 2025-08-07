# Medical Bot - Personalized Medical Recommendation System

An AI-powered medical recommendation system that provides personalized health recommendations based on symptoms input by users.

## Features

- **Symptom-based Disease Prediction**: Uses machine learning to predict potential diseases based on symptoms
- **Comprehensive Recommendations**: Provides detailed recommendations including:
  - Disease description
  - Precautionary measures
  - Recommended medications
  - Dietary suggestions
  - Exercise/workout recommendations
- **User-friendly Interface**: Simple command-line interface for easy interaction
- **Extensive Symptom Database**: Covers 132 different symptoms and 41 diseases

## Technologies Used

- **Python 3.x**
- **Machine Learning**: Scikit-learn (SVM classifier)
- **Data Processing**: Pandas, NumPy
- **Model Persistence**: Pickle
- **Jupyter Notebooks**: For development and analysis

## Dataset Information

The system uses multiple CSV files for comprehensive medical information:
- `Training.csv`: Training data for the ML model
- `symtoms_df.csv`: Symptom descriptions
- `precautions_df.csv`: Disease precautions
- `medications.csv`: Recommended medications
- `diets.csv`: Dietary recommendations
- `workout_df.csv`: Exercise recommendations
- `description.csv`: Disease descriptions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SreekarMaddala/medicalbot.git
cd medicalbot
```

2. Create a virtual environment:
```bash
python -m venv medibot_env
source medibot_env/bin/activate  # On Windows: medibot_env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface
Run the medical recommendation system:
```bash
python run_medical_system.py
```

### Jupyter Notebook
Open the notebook for development and analysis:
```bash
jupyter notebook "Medicine Recommendation System.ipynb"
```

## How It Works

1. **Input**: User enters symptoms separated by commas
2. **Processing**: System processes symptoms using trained ML model
3. **Prediction**: Disease is predicted based on symptom patterns
4. **Recommendations**: Comprehensive recommendations are provided based on the predicted disease

## Example Usage

```
Enter your symptoms: itching,skin_rash,fatigue

PREDICTED DISEASE: Fungal infection

DESCRIPTION: Fungal infections are common throughout much of the natural world...

PRECAUTIONS:
1. Keep the affected area clean and dry
2. Use antifungal powder
3. Avoid sharing personal items
4. Wear breathable fabrics

RECOMMENDED MEDICATIONS:
1. Clotrimazole
2. Terbinafine

RECOMMENDED DIET:
1. Probiotic foods
2. Avoid sugary foods

RECOMMENDED WORKOUTS:
1. Light walking
2. Yoga
```

## Model Information

- **Algorithm**: Support Vector Machine (SVM)
- **Accuracy**: High accuracy on training data
- **Features**: 132 binary symptom features
- **Classes**: 41 different diseases

## File Structure

```
medicalbot/
├── run_medical_system.py          # Main CLI application
├── Medicine Recommendation System.ipynb  # Jupyter notebook
├── Training.csv                   # Training dataset
├── symtoms_df.csv                 # Symptom descriptions
├── precautions_df.csv             # Disease precautions
├── medications.csv                # Medication database
├── diets.csv                      # Diet recommendations
├── workout_df.csv                 # Exercise recommendations
├── description.csv                # Disease descriptions
├── svc.pkl                        # Trained SVM model
├── random_forest.pkl              # Alternative RF model
├── requirements.txt               # Python dependencies
├── README.md                      # This file
└── .gitignore                     # Git ignore rules
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Disclaimer

This system is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

For questions or suggestions, please open an issue on GitHub.
