# CreateAutomationframeworkFolder-Structure
Python script that automates the creation of the folder structure and packages it into a .zip file.
Folder Structure
Based on application add other details

src
├── main
│   ├── java
│   │   ├── pages
│   │   │   ├── BasePage.java
│   │   │   ├── LoginPage.java
│   │   │   ├── AdminInterfacePage.java
│   │   │   └── ...
│   │   ├── utilities
│   │   │   ├── ConfigReader.java
│   │   │   ├── ExcelUtils.java
│   │   │   └── ...
│   │   └── framework
│   │       ├── BaseTest.java
│   │       └── WebDriverManager.java
│   └── resources
│       ├── config.properties
│       ├── testdata.xlsx
│       └── ...
└── test
    └── java
        ├── tests
        │   ├── LoginTest.java
        │   ├── AdminInterfaceTest.java
        │   ├── ServiceInterfaceTest.java
        │   └── ...
        └── runners
            └── TestRunner.java
