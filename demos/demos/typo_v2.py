import requests
import json
import re


class TypoV2:
    def __init__(self):
        self.key = 'DZZgwYoI0GN6R4CaLqOJagTNdAzXb01r'
        self.api = 'https://api.a3rt.recruit-tech.co.jp/proofreading/v2/typo'

    def get(self, inputtext):
        url = self.api
        quoted_text = inputtext
        r = requests.post(url,
                          {'apikey': self.key,
                           'sentence': quoted_text,
                           'sensitivity': 'medium'})
        data = json.loads(r.text)
        rets = []
        if data['status'] == 1:
            rets = '疑わしい部分と判定した箇所あります。</br>ハイライトされた箇所を確認してください。</br><hr>'
            text = data['checkedSentence']
            rets = rets + self.__trans_word(text)
        elif data['status'] == 0:
            rets = "この文章に誤字脱字はありません。</br>指摘すべき修正を見つけられませんでした。"
        else:
            rets = "エラーがありました。</br>応答コードは" + data['status'] + "です。"
        return rets

    def __trans_word(self, inputtext):
        replacements = {
            '<<': '<span class="mark font-weight-bold text-danger">',
            '>>': '</span>'}
        return re.sub('({})'.format('|'.join(map(
            re.escape, replacements.keys()))), lambda m: replacements[m.group()], inputtext)
