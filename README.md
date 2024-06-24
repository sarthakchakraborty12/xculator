# xculator
It is a open souce python-tkinter based simple calculator app.
I used python and tkinter, a python GUI library to make the calculator app. Since it is made this way, the app needs to use the console to run. But imagine every time you open the calculator and the commannd line opens with it, so basically when we made the .exe file out of the project, basically we made two versions. one which works with terminal and another also runs on terminal obviously because that's basically a python code doing all the things. so the second version desn't show the terminal at all but runs the program in background as normal applications run their processes.
So, the main version doesn't open the console, so that some of the antivirus softwares including in built windows security can make false virus recognition as it is running code in console in the background. That is why we decided to make our first project open source so that there's no second question about transparency. If you still find it difficult to somehow run the app, then you can consider the consoled version of the app.

![python-powered-w-200x80](https://github.com/sarthakchakraborty12/xculator/assets/97733790/5ce7f360-f2e8-4c86-a474-3b78feea5df8)

__________________________________________________________________
* For Users

If you have trouble running the app, make sure python is installed and up to date in your computer. Also, if needed you can install th tkinter GUI library after installing python by typing this command on your terminal :

```pip install Tk```

__________________________________________________________________
* For Devs

make sure to have the latest python, tkinter and pyinstaller installed on your system to ensure better capability. In case you don't know, these are the code snippets to install pyinstaller and tkinter :

pyinstaller :
```pip install pyinstaller```

tkinter :
```pip install Tk```

If you are having trouble running the pyinstaller command you can use this :


```python -m PyInstaller --onefile --noconsole XCulator.py```


or if you are building the consoled version then build it without the 'noconsole' flag like this : 

```python -m PyInstaller --onefile XCulator.py```

Now, for now the project is very basic. it has a fixed width and height. but in case you want a flexible and responsive UI, just change the root.resizable to 'true' like this :
```root.resizable(True,True)```

You can play around with everything. the possibility is endless. you can make it more useful by adding different functions and extending its functionality.
note, the main version will be intact from our side and we will update the main branch only with our code. That means you can't directly contribute to this project but still make your own version of this app.
