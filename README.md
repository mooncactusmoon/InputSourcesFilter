# InputSourcesFilter
test input sources filter tool

## UI 操作預期步驟
1. 下拉式選單選擇要比較篩選的裝置(目前先兩個)
2. 點擊送出按鈕
3. 視窗內出現選擇裝置的所有訊號源
  * 兩個的訊號源分別顯示(以列表方式呈現)
  * 若只有其中一方才有的訊號源將會有顏色(e.g.:以紅色顯示)

> 未來擴充 : 多出一格顯示選取裝置都沒有的訊號源

## 程式預期
* 可擴充機種及訊號源(暫時先不用資料庫、以 Json 撰寫)
* 正確的顯示訊號源及比較後的顏色
* 結果所需計算/呈現時間不會過久

> 未來擴充 : 可不只選取兩個機台做比較列出
