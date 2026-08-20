# BB 填滿記憶體

這個程式會在幾秒內盡可能吃光記憶體  
用來強迫Windows釋放或管理記憶體  

# 下載

### 到 Releases 下載最新版

- [BB Fill Memory.exe](https://github.com/BeefBB/bb-fill-memory/releases)

# 想自己編譯?

## 執行

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
```bash
pyinstaller --noconfirm --onefile --name="BB Fill Memory" bb-fill-memory.py
```

打包後會在 `./dist`  

# 版權

MIT License  
