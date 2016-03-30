# GoogleCalculator
Simple project that test Google Calculator using Selenium and Unittest based on predefined data which is stored in "GoogleCalculator\sample\data\project_data.py" file.
The main idea of this project it's education of new staff that know nothing about Selenium and unittest and need to learn it quickly.
This project doesn't cover all functionality of Selenium and unittest but can get basic knowledges that can help quickly understand main idea of it.

Project starts Firefox or Chrome, open Google Calculator and makes some calculations.
All calculations are verified by unittest and when calculations is finished the "GoogleCalculator\sample\output.png" folder will contain png-file with screen for each test cases.
Current PNG-files in the "GoogleCalculator\sample\output.png" folder is stored only as example and will be rewritten when test complete.

Project can work only if Firefox or Chrome with ChromeDriver is installed. If there is no Firefox or Chrome with ChromeDriver installed the following exception will be raised:
```
   Firefox is not installed and
   system paramer "ChromeDriver" is not defined.
   Please add it with path to ChromDriver binary.
   See https://sites.google.com/a/chromium.org/chromedriver/home
   for more information or install Firefox.
```

In case of Chrome with ChromeDriver used then system parameter "ChromeDriver" should be set.
For example if "chromedriver.exe" located in "C:\ChromeDriver" folder then system parameter ChromeDriver should be set as following:
```
set ChromeDriver=C:\ChromeDriver\chromedriver.exe
```

Project can be executed in different ways. 
For example inside GoogleCalculator folder you can run it as following:
```
#One way
python -m unittest -q sample.PyGoogleCalc

#Another way
python run_test.py

#Or run it as module
python -m sample
```
Or if you extracted project into "Work" folder (where path to project is "Work\GoogleCalculator") then you can execute it outside of work folder as following.
```
#One way
python -m unittest -q Work.GoogleCalculator.sample.PyGoogleCalc

#Another way
python Work\GoogleCalculator\run_test.py

#Or run it as module
python -m Work.GoogleCalculator
```

In any case result will be the same.

But examples above is not whole list of possible type to run this project. 
You can add PYTHONPATH system parameter with path to the folder where project is located as following:

PYTHONPATH=C:\Work

And so on, and so on.
Read "Command line and environment" in Python guide.
https://docs.python.org/3/using/cmdline.html
