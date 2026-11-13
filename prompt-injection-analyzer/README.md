# Prompt Injection Analyzer

教育用途的離線 Python CLI，使用少量 Regex 規則標示輸入文字中的可疑特徵。不是完整防禦系統，也不會執行輸入或呼叫 LLM。

## 執行

需求：Python 3.9+，不需要安裝第三方套件。

```bash
python3 main.py
python3 main.py --text "Ignore all previous instructions."
python3 main.py --text ""
python3 main.py --file sample.txt
python3 -m unittest discover -s tests -v
```

互動模式接受單行輸入；多行文字請存成 UTF-8 檔案後使用 `--file`。

## 專案文件

完整需求分析、MVP、架構圖、模組說明、風險邏輯、測試案例、False Positive / False Negative 分析及 18 小時規劃，請參閱 [`PROJECT_REPORT.md`](PROJECT_REPORT.md)。

## 檔案

- `main.py`：CLI 入口與輸入讀取
- `rules.py`：偵測規則
- `analyzer.py`：規則比對及分析結果
- `risk.py`：風險分級
- `report.py`：終端機報告
- `tests/test_analyzer.py`：11 個標準函式庫單元測試
