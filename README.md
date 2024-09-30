# 文面の解析による迷惑メールの分類

## 概要

- 既存の迷惑メール分類では, 送信者のドメイン情報などをもとに分類を行なっています.

- 本モデルでは, メール本文を解析することによる迷惑メール分類を行います.

## 使い方

```
python ja_phishing_mail_detection.py < email_text.txt
```

- 迷惑メールの可能性が低ければ`benign`が出力されます.

- 迷惑メールの可能性が高ければ`phishing`が出力されます.

- メール本文のサンプルとして[example_phishing_email_txt](https://github.com/konno0121/ja_phishing_mail_detection/blob/main/example_phishing_mail.txt), [example_bussiness_email_txt](https://github.com/konno0121/ja_phishing_mail_detection/blob/main/example_business_mail.txt)があります.

## 注意事項

- 使用している翻訳モデルの相性の都合で, **transformersのversionは4.20を使用してください**.

## 使用させていただいているモデル

- 翻訳モデル: [staka/fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en?text=%E7%8C%AB%E3%81%AF%E3%81%8B%E3%82%8F%E3%81%84%E3%81%84%E3%81%A7%E3%81%99%E3%80%82)

- 分類モデル: [bert-finetuned-phishing](https://huggingface.co/ealvaradob/bert-finetuned-phishing)
