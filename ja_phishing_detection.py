import warnings
from transformers import pipeline
import sys

# FutureWarning を無視
warnings.simplefilter("ignore", FutureWarning)


def ja_phishing_detection(email_text: str) -> list:
    """
    日本語で書かれたメール文を受け取り, フィッシングメール分類を行う

    Args:
        email_text(str): 日本語で書かれたメール文

    Returns:
        list: 分類結果
    """

    # 日本語から英語に翻訳するためのモデル
    translator = pipeline("translation", model="staka/fugumt-ja-en")

    # フィッシングメール分類用の英語モデル
    phishing_model = pipeline(
        "text-classification", model="ealvaradob/bert-finetuned-phishing"
    )

    # 日本語メールを英語に翻訳
    email_text_english = translator(email_text)[0]["translation_text"]

    # 翻訳結果の表示
    print(f"Original Japanese Email:\n{email_text}")
    print(f"Translated English Email:\n{email_text_english}")

    # 翻訳された英語の文章を分類モデルで判定
    return phishing_model(email_text_english)


def main():
    # メールの文面を受け取る
    email_text = sys.stdin.read()

    # フィッシングメール分類
    classification_result = ja_phishing_detection(email_text)

    # 結果を表示
    print(
        f"Phishing Classification: {classification_result[0]['label']} (Score: {classification_result[0]['score']})"
    )


if __name__ == "__main__":
    main()
