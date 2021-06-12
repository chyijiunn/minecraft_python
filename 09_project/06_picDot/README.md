## 畫點陣圖
![執行畫面](https://raw.githubusercontent.com/chyijiunn/minecraft_python/main/09_project/06_picDot/picDot.png)  
使用googleSheet先處理原始圖檔，  
第二個分頁處理座標，設定A欄位為 Y 座標高度數值，第一列為X座標，採用 -X ~ X 相對座標，最大範圍先設定為 28 x 25  
於第一個分頁當中輸入需要的顏色代碼，第二個分頁會讀出三個參數，並於 setBlock 函式當中放入 x , y 和 羊毛 No.35 的副參數當中

上方的dotPicMineCraft.xlsx，是從 googleSheet轉檔過來的[連結檔案](https://docs.google.com/spreadsheets/d/1kZ4rM2EgBAQepYDJAVq_NnGirRVX60CaGsxyM71mmF4/edit?usp=sharing)
