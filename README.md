使用pycharm建置python開發爬蟲程式，利用selenium進行網頁內容讀取，試圖獲得書名/作者/分類/原價/折扣價...

時間:11/6~11/9  (11/5到外縣市面試)
這4天內設計這支程式的流程，大致分為
第一天
尋找可使用的爬蟲方式
設計selenium抓取網頁的方法
將換行內容替換成空字串，並在陣列中處理空字串
第二天
查詢轉換json格式寫法，處理中文轉碼問題
透過抓取出的網址連結，進入書本明細頁面，取得明細內容
第三天
發生error('Connection aborted.', OSError("(10054, 'WSAECONNRESET')"))
經過requests與headers的處理，試圖取得明細卻再次失敗
第四天
試著處理問題，尋找解決方案，設計開啟多分頁的方式進入書本明細，但設計上有流程上的失誤(需再次點入)
