# GoogleCalculator
Simple project that test Google Calculator using Selenium and Unittest based on predefined data which is stored in "GoogleCalculator\sample\data\project_data.py" file.

When test is finished "GoogleCalculator\sample\output.png" folder will contain png-file with screen for each test cases.
Current PNG-files in "GoogleCalculator\sample\output.png" folder is stored only as example and will be rewritten when test complete.

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

Project can be executed in different ways. For example:
```
#One way
python -m unittest -q sample.PyGoogleCalc

#Another way
python run_test.py
```
Or if you extracted project into "C:\Project\GoogleCalculator" folder then execute it possibe in following ways.
```
#One way
python -m unittest -q Project.GoogleCalculator.sample.PyGoogleCalc

#Another way
python Project\GoogleCalculator\run_test.py
```

In any case result will be the same.
