
# python學習相關

### HOT KEY
|熱鍵|說明|
|--|--|
|CTRL + /|註解|
|CTRL + SHIFT + P|VSCODE 快速功能搜尋指令視窗|

---
### VSCODE workspace settings

    {
	    "python.pythonPath": "C:\\Users\\~~~\\Python\\Python38\\python.exe",    // python 程式路徑
	    "python.linting.pylintEnabled": true,   // 需要 pip install pylint
	    "python.linting.enabled": true, // 需要 pip install pylint
	    "python.autoComplete.extraPaths": [ // 搭配vscode套件Importmagic，自動引入該目錄底下lib
            "C:\\Users\\Snow\\AppData\\Local\\Programs\\Python\\Python38",
            "D:\\Learning\\Python"
        ],
        "python.autoComplete.addBrackets": true	// 自動加上括號
	}
---