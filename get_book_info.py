# CLI 书籍信息查询系统

# 这段代码的逻辑是这样的：
# 1. 用户在命令行执行"python get_book_info.py '自私的基因'"，'自私的基因'即为参数；回车执行；
# 2.  首先引入 fire\requests两个库；
# 3. 判断是否执行当前的python文件，如果内置变量__name__ == '__main__'，就调用fire库的Fire类，否则不执行；
# 4. 实例化Fire类，Fire类自动把类DouBanBookUtil的方法和变量变成命令行的参数，这样可以直接在命令行里调用python；
# 5. 命令行调用python默认的main()方法；
# 5. 命令行中的"python get_book_info.py '自私的基因'"，表示使用python执行get_book_info.py这个文件，并传递一个参数'自私的基因'；
# 6. 然后实例化DouBanBookUtil类douban，在实例化中，默认调用__init__(self)，设定设定调用的api url；
# 7. 然后douban调用get_book_summary_by_name(self, book_name)方法，并传递参数'自私的基因'；
# 8. 在get_book_summary_by_name（）方法中，先重新定义url，然后调用self._post；
# 9. _post()方法中，先设定url，然后调用requests库的post方法，并传递参数url,_post返回JSON数据data,data包括该书的全部信息；
#10. 最后 book_summary = self._post(url)["books"][0]["summary"]，从data中取出这本书的summary；

import fire
import requests
import configparser

class DouBanBookUtil:
    def __init__(self):
        # 设定调用的api url
        self.url = "https://api.douban.com/v2/book/"
        #print('设定调用的api url')
        
    # 进行POST请求并返回JSON数据
    def _post(self, url):
        # url = self.url + "search?q=" + book_name
        config = configparser.ConfigParser()
        config.read('config.ini')
        DOUBAN_API_KEY  = config['DEFAULT']['DOUBAN_API_KEY']
        data = {"apikey" : DOUBAN_API_KEY}
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"}
        res = requests.post(url, data = data, headers = headers)
        data = res.json()
        #print(data)
        #print('_post()方法在运行')
        return data


        

    # 根据书名获取书籍摘要
    def get_book_summary_by_name(self, book_name):
        url = self.url + "search?q=" + book_name
        book_summary = self._post(url)["books"][0]["summary"]
        #print('get_book_summary_by_name()在运行')
        # print(book_summary)
        return book_summary



    
# def main(book_name):
#     #print('main 方法，实例化DouBanBookUtil，并调用get_book_id_by_name()和get_book_summary_by_name（）')
#     douban = DouBanBookUtil()
#     #douban.get_book_id_by_name(book_name)
#     print(douban.get_book_summary_by_name(book_name))

# if __name__ == '__main__':
#     #print('调用fire.Fire(main)')
#     fire.Fire(main)


    