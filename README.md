# SpeechToText

## How to run in local:

### Ready
- Editer:  [Visual Studio Code](https://code.visualstudio.com/)
- Environment: [Minicond](https://docs.conda.io/en/latest/miniconda.html)

### pip install ...
- Python: 3.7
- Django: 2.2
- API: `baidu-aip`

### Ready to run
1. Download the ZIP and decompression ;
2. Open the `Visual Studio Code` ;
3. File -> Open Folder -> SpeechToText-master ;
4. project -> server -> SpeechToText ;
5. Right click the `manage.py` ;
6. Open in Terminal ;

### Environment
1. if you are using **conda**,maybe you are in the `base` **Environment**, the `base` **Environment** is a **PublicEnvironment**;
2. if you are in the `base` **Environment** ,You need to type `conda create -n [YourEnvName]` in the Terminal ,to create a new Environment ;
3. And back to the `Visual Studio Code` to change your  **Environment** at lower left quarter;
4. You are in **PersonalEnvironment** after that restart the **Terminal**;
5. Success will be like this `(SpeechToText) c:\Users\wuwil\OneDrive - Kantar\dev\SpeechToText\project\server\SpeechToText>` in **Terminal**,**(SpeechToText)** is my **PersonalEnvironment**.

### Runserver
1. if you in **(PersonalEnvironment)** - **Terminal**;
2. Just type `python manage.py runserver` in **Terminal** ，you can start a simple server.
3. if you got an error , than you must type `pip install [YourMissingModules]` in **Terminal**;

### Start test
- Open the `demo.html` ,start to test.

----
### Other Question?
Sand email to me : `wilson.wu@kantar.com`


