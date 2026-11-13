#知識卡 #高二上自主學習 #LLM

## 兩種 Prompt

- **System Prompt**：開發者設計，規範 AI 做哪些事情、什麼是不能做等等
	
- **User Prompt**：使用者輸入給 AI 的問題

System Prompt 具有比 User Prompt 更高的優先級，**但並非絕對的界線**。

## Prompt 的成分

- **Instruction**：叫模型做什麼事。
	
- **Context**：AI 可參考外部文件、副檔、先前對話內容等等。
	
- **Input Data**：使用者的問題。
	
- **Output Indicator**：規範輸出方式。

不必四種皆具備。

## LLM 如何看 Prompt

LLM 會在同一個 context 中處理 System Prompt 和 User Prompt，會一起讀完再根據上下文產生回答。