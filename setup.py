from setuptools import setup, find_packages
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements from a given file.
    It removes '-e .' if it exists in the list of requirements.
    
    Args:
        file_path (str): Path to the requirements.txt file.

    Returns:
        List[str]: Cleaned list of requirements.
    """
    requirements = []

    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
        
        # Clean each line (strip newline and surrounding spaces)
        requirements = [req.strip() for req in requirements]

        # Remove '-e .' if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return requirements
# Configuration du package
setup(
    name='mlproject',
    version='0.0.1',
    author='Karim',
    author_email='kelarrouf@insea.ac.ma',
    description='Un projet Python pour démonstration',
    packages=find_packages(),  # Trouver automatiquement les packages dans le répertoire actuel
    install_requires=get_requirements('requirements.txt'),  # Charger les dépendances sans "-e ."
  
)