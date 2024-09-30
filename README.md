# 文面の解析による迷惑メールの分類

## 概要

- 既存の迷惑メール分類では, 送信者のドメイン情報などをもとに分類を行なっている.

- 本モデルでは、メール本文を解析することによる迷惑メール分類を行う.

## 使い方

```
python ja_phishing_mail_detection < email_text.txt
```

メール本文の一例として[example_phishing_email_txt](https://github.com/konno0121/ja_phishing_mail_detection/blob/main/example_phishing_mail.txt), [example_bussiness_email_txt](https://github.com/konno0121/ja_phishing_mail_detection/blob/main/example_business_mail.txt)があります.

## 注意事項

- 使用している翻訳モデルの相性の都合で、**transformersのversionは4.20を使用してください**.
