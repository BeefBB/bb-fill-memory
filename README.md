# BB 填滿記憶體

實際是個記憶體釋放工具, 只是它不會要求任何程式釋放記憶體  
相反的, 它會在幾秒內盡可能吃光記憶體, 以此強迫 Windows 釋放或管理記憶體  

執行一次大約30秒, 取決於記憶體填充速度  
執行完畢時, 觀察到系統的記憶體使用量比執行前更少  
填滿有時候比清理更有用  

# 下載

### 到 Releases 下載最新版

- [BB Fill Memory.exe](https://github.com/BeefBB/bb-fill-memory/releases)

### 備註

執行時, 記憶體將會持續接近全滿  
Windows 可能不斷增加虛擬記憶體, 或是激進的管理記憶體, 電腦可能會非常卡頓, 甚至崩潰  

# 參數

BB Fill Memory 支援以下命令列參數:  

參數        |預設值 |單位 |說明
:---        |:---   |:--- |:---
`--time`    |`25`   |s    |填滿記憶體後維持的時間
`--free`    |`256`  |MiB  |保留的可用記憶體
`--block`   |`128`  |MiB  |每次增加的記憶體量
`--timeout` |`35`   |s    |逾時中斷時間
`--noshake` |       |     |禁用記憶體填滿時抖動
`--force`   |       |     |忽略記憶體錯誤並繼續執行
`--mute`    |       |     |靜音輸出

> `--timeout` 應該大於 `--time` 以免提前中斷  

### 範例

預設  
```Bash
".\BB Fill Memory.exe"
```

持續 30 秒, 保留 512 MiB, 最長執行 40 秒  
```Bash
".\BB Fill Memory.exe" --time=30 --free=512 --timeout=40
```

預設, 靜音輸出  
```Bash
".\BB Fill Memory.exe" --mute
```

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

打包後會在 `.\dist`  

# 版權

MIT License  