import os
import zipfile

# Define the folder structure
folder_structure = {
    "src": {
        "main": {
            "java": {
                "pages": ["BasePage.java", "LoginPage.java", "AdminInterfacePage.java"],
                "utilities": ["ConfigReader.java", "ExcelUtils.java"],
                "framework": ["BaseTest.java", "WebDriverManager.java"]
            },
            "resources": ["config.properties", "testdata.xlsx"]
        },
        "test": {
            "java": {
                "tests": ["LoginTest.java", "AdminInterfaceTest.java", "ServiceInterfaceTest.java"],
                "runners": ["TestRunner.java"]
            }
        }
    }
}

# Function to create folders and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        os.makedirs(path, exist_ok=True)
        if isinstance(content, dict):
            create_structure(path, content)
        elif isinstance(content, list):
            for file in content:
                with open(os.path.join(path, file), 'w') as f:
                    f.write("")

# Function to create a zip file
def create_zip(base_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), base_path))

# Main execution
if __name__ == "__main__":
    base_path = "automation_framework"
    create_structure(base_path, folder_structure)
    create_zip(base_path, "automation_framework.zip")
    print("Folder structure created and zipped successfully!")