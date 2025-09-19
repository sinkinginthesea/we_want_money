import asyncio
import nodriver as uc

async def main():
    # 啟動瀏覽器
    browser = await uc.start()
    
    # 開啟新分頁並前往 KKTIX
    page = await browser.get('https://kktix.com/')
    
    # 印出頁面標題 (title 是屬性，不是方法)
    print(f"頁面標題: {page.title}")
    
    # 讓瀏覽器保持開啟，直到手動關閉
    print("瀏覽器已開啟，請手動關閉程式來結束")
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("程式已結束")
        await browser.close()

if __name__ == '__main__':
    # 使用 asyncio.run() 來執行異步的 main 函式
    asyncio.run(main())