import json
import random
from datetime import datetime

def run_crawler():
    print("啟動雲端自動爬蟲...")
    
    # 這裡未來可以替換成實際抓取證交所 API 的 requests 程式碼
    # 範例：模擬計算主動式 ETF 的持股買賣超排行
    mock_stocks = ["2330 台積電", "2454 聯發科", "2317 鴻海", "2382 廣達", "3231 緯創"]
    rankings = []
    
    for stock in mock_stocks:
        # 模擬計算：(今日張數 - 昨日張數) * 均價
        change_shares = random.randint(-500, 1000)
        vwap = random.randint(100, 1000)
        net_buy_value = change_shares * vwap
        
        rankings.append({
            "stock": stock,
            "value": net_buy_value
        })
        
    # 依買超金額從大到小排序
    rankings.sort(key=lambda x: x['value'], reverse=True)
    
    # 打包成網頁看得懂的 JSON 格式
    output_data = {
        "update_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "rankings": rankings
    }
    
    # 將計算結果寫入儲存空間
    with open('etf_data.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)
        
    print("資料計算完成，成功寫入 etf_data.json！")

if __name__ == "__main__":
    run_crawler()
