# GoogleCalculator
Simple project that test Google Calculator using Selenium and Unittest based on predefined data which is stored in "data\project_data.py" file.

When test is finished Output.png folder will contain png-file with screen for each test cases.
Current PNG-files in output.png folder is used only as example and will be rewritten when test complete.

Project can work only if Firefox or Chrome is installed. If there is no Firefox or Chrome installed the following exception will be raised:
```
   Firefox is not installed and
   system paramer "ChromDriver" is not defined.
   Please add it with path to ChromDriver binary.
   See https://sites.google.com/a/chromium.org/chromedriver/home
   for more information or install Firefox.
```