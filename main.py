import hashlib
import logging

from aiogram import types
from aiogram.utils import executor
from youtube_search import YoutubeSearch

from config import dp


def searcher(text):
    res = YoutubeSearch(text, max_results=10).to_dict()
    return res

@dp.inline_handler()
async def inline_handler(query : types.InlineQuery):
    text = query.query or 'echo'
    links = searcher(text)

    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(f'{link["id"]}'.encode()).hexdigest(),
        title=f'{link["title"]}',
        url=f'https://www.youtube.com/watch?v={link["id"]}',
        input_message_content=types.InputTextMessageContent(
            message_text=f'https://www.youtube.com/watch?v={link["id"]}')

    ) for link in links]

    await query.answer(articles, cache_time=60, is_personal=True)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)


# def searcher():
#     res = YoutubeSearch('python 16_1 Daniyar Tg_BOT', max_results=1).to_dict()
#     # with open('text.py', 'w', encoding='utf-8') as r:
#     #     r.write(str(res))
#     return res

# def seacher():
#     responce = requests.get('https://www.youtube.com/results?search_query=python')
#     soup = BeautifulSoup(responce.content, 'html.parser')
#     search = soup.find_all('script')[32]
#     key = '"videoID:"'
#     data = re.findall(key+r"([^*]{11})", str(search))
#     print(data)
#
# seacher()
