# For windows
## 1.This creates the virtual Environment
         python -m venv myenv
## 2.This activates the virtual Environment
```python
myenv\Scripts\activate 
```
## 3.Install vs code builder(During installation, select the "C++ build tools" workload and include the "MSVC v142 - VS 2019 C++ x64/x86 build tools" and the "Windows 10 SDK".) this may take some time
## 4.Restart the sys
## 5.Open VS code build click on run then enter cl if no error occured succesfully installed 
## 6.For specific version
```python
pip install pandas==2.1.4 #(This may take some time)
```
## 7.To check installed version in python in cmd type 
```python
import pandas as pd
pd.__version__
```
## 8.TO exit the vertual enveronment type 
```python
deactivate
```
## 9.To check all install version in virtual environment
```python
pip freeze 
```
## 10.To make a text file containing all the data of installed version in Virtual environment
```python
pip freeze > requirements.txt
```
## To install all the version in requirements.txt file then rum
```python
pip install -r requirements.txt
```