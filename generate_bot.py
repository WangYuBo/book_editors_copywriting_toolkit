import os
from fastapi import FastAPI,Form,Request
import zhipuai
from get_book_info import DouBanBookUtil
import configparser

# 生成式Bot，能够根据图书摘要生成小红书文案；
class GenerateBot():
    #调用智谱ai，生成小红书文案，参数book_data
    def genBook(self, book_name):
         # 从配置文件中读取智谱API key
        config = configparser.ConfigParser()
        config.read('config.ini')
        zhipuai.api_key  = config['DEFAULT']['ZHIPU_API_KEY']
   
        # 调用豆瓣读书api获取图书详细
        book_summary = DouBanBookUtil().get_book_summary_by_name(book_name)
        #print(book_summary)

        # 读取小红书prompt.txt
        with open("W3/hard_work/prompt.txt", "r", encoding="utf-8") as f:
            sys_prompt = f.read()

        # 调用智谱AI来生成小红书文案
        response = zhipuai.model_api.sse_invoke(
            model="chatglm_turbo",
            prompt=[
                {"role": "user", "content": f"{sys_prompt}"},
                {"role": "assistant", "content": "你好，请问有什么可以帮到您的吗？"},
                {"role": "user", "content" : f"{book_name},{book_summary}"}

            ],
            temperature= 0.9,
            top_p= 0.7,
            incremental=True
        )
   

        for event in response.events():
             yield event.data
            # if event.event == "add":
            #     print(event.data, end="")
            # elif event.event == "error" or event.event == "interrupted":
            #     print(event.data, end="")
            # elif event.event == "finish":
            #     print(event.data)
            # #print(event.meta, end="")
            # else:
            #     print(event.data, end="")

        

# if __name__ == "__main__":
    
#     print(GenerateBot().genBook("从拖延到行动"))
    
