# TwitterFrontendFlow

----
----
<!> This project is not maintained. Use [twitter_openapi_python](https://github.com/fa0311/twitter_openapi_python) and [tweepy_authlib](https://github.com/tsukumijima/tweepy-authlib)

----
----

Twitter の内部 API を叩く

ログイン: [TwitterFrontendFlow](https://github.com/fa0311/TwitterFrontendFlow) /
取得: [TweetURLtoData](https://github.com/fa0311/TweetURLtoData) /
スペース: [TwitterSpacesWiretap](https://github.com/fa0311/TwitterSpacesWiretap)

## P.S. restriction bypass (Fixed)

[hackerone.com](https://hackerone.com/reports/1439026)

## proxy

[requests-docs](https://requests-docs-ja.readthedocs.io/en/latest/user/advanced/#proxies)

```python
TwitterFrontendFlow(proxies={
        "http":"",
        "https":""
})
```

## login flow

### 通常ログイン

```python
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSO("電話番号/メールアドレス/ユーザー名")
      .LoginEnterPassword("パスワード").content)
```

### 2 段階認証

```python
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSO("電話番号/メールアドレス/ユーザー名")
      .LoginEnterPassword("パスワード")
      .AccountDuplicationCheck()
      .LoginTwoFactorAuthChallenge("2段階認証のコード").content)
```

### 通常とは異なるログイン操作が行われました

```python
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSO("電話番号/メールアドレス/ユーザー名")
      .LoginEnterAlternateIdentifierSubtask("電話番号/ユーザー名")
      .LoginEnterPassword("パスワード").content)
```

### アカウントの安全のために

```python
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSO("電話番号/メールアドレス/ユーザー名")
      .LoginEnterPassword("パスワード")
      .AccountDuplicationCheck()
      .LoginAcid("メールアドレス / メールアドレスのコード").content)
```

## password reset flow

### 通常リセット

```python
print(TwitterFrontendFlow()
    .password_reset_flow()
    .PwrJsInstrumentationSubtask()
    .PasswordResetBegin("電話番号/メールアドレス/ユーザー名")
    .PasswordResetChooseChallenge()
    .PasswordResetConfirmChallenge("認証コード")
    .PasswordResetNewPassword("新しいパスワード")
    .PasswordResetSurvey("0").content)
```

### 個人情報を確認してください

```python
print(TwitterFrontendFlow()
    .password_reset_flow()
    .PwrJsInstrumentationSubtask()
    .PasswordResetBegin("ユーザー名")
    .PwrKnowledgeChallenge("メールアドレス")
    .PwrKnowledgeChallenge("電話番号")
    .PasswordResetChooseChallenge()
    .PasswordResetConfirmChallenge("認証コード")
    .PasswordResetNewPassword("新しいパスワード")
    .PasswordResetSurvey("0").content)
```

## Save / Load

```python
(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSO("電話番号/メールアドレス/ユーザー名")
      .LoginEnterPassword("パスワード")
      .SaveCookies("user.json"))
```

```python
(TwitterFrontendFlow()
        .LoadCookies("user.json"))
```

## after login

おまけ程度

### ツイート

```python
print(TwitterFrontendFlow()
        .LoadCookies("user.json")
        .CreateTweet("ツイートしたい文字列").content)
```

### いいね

```python
print(TwitterFrontendFlow()
        .LoadCookies("user.json")
        .FavoriteTweet("ツイートid").content)
```

### いいね取り消し

```python
print(TwitterFrontendFlow()
        .LoadCookies("user.json")
        .UnfavoriteTweet("ツイートid").content)
```

### リツイート

```python
print(TwitterFrontendFlow()
        .LoadCookies("user.json")
        .CreateRetweet("ツイートid").content)
```

### リツイート取り消し

```python
print(TwitterFrontendFlow()
        .LoadCookies("user.json")
        .DeleteRetweet("ツイートid").content)
```

### フォロー

未だに新 API への移行が終わってないらしく旧 API での実装

```python
print(TwitterFrontendFlow()
        .LoadCookies("user.json")
        .friendships_create("ユーザーの内部id").content)
```

### フォロー取り消し

未だに新 API への移行が終わってないらしく旧 API での実装

```python
print(TwitterFrontendFlow()
        .LoadCookies("user.json")
        .friendships_destroy("ユーザーの内部id").content)
```

## sample

中身見たほうが早いかも
これが動かないアカウントがあったら詳細を詳しく issue に
[sample.py](https://github.com/fa0311/TwitterFrontendFlow/blob/master/sample.py)

## help

### inappropriate method

LoginFlow のリクエストを送る順番が不適切と検知した場合に表示されます
あくまで検知なのでこれをバイパスする方法があります

```python
flow = TwitterFrontendFlow()
flow.method_check_bypass = True
```
