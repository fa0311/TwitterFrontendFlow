# TwitterFrontendFlow
Twitterの内部APIを叩く<br>
ログイン: [TwitterFrontendFlow](https://github.com/fa0311/TwitterFrontendFlow) /
取得: [TweetURLtoData](https://github.com/fa0311/TweetURLtoData) /
スペース: [TwitterSpacesWiretap](https://github.com/fa0311/TwitterSpacesWiretap)

## proxy
```
TwitterFrontendFlow(proxies={
        "http":"",
        "https":""
})
```

## login flow

### 通常ログイン
```
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSOSubtask("電話番号/メールアドレス/ユーザー名")
      .LoginEnterPassword("パスワード").content)
```
### 2段階認証
```
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSOSubtask("電話番号/メールアドレス/ユーザー名")
      .LoginEnterPassword("パスワード")
      .LoginTwoFactorAuthChallenge("2段階認証のコード").content)
```
### 通常とは異なるログイン操作が行われました
```
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSOSubtask("電話番号/メールアドレス/ユーザー名")
      .LoginEnterAlternateIdentifierSubtask("電話番号/ユーザー名")
      .LoginEnterPassword("パスワード").content)
```
## password reset flow

### 通常リセット
```
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
```
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
```
(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSOSubtask("電話番号/メールアドレス/ユーザー名")
      .LoginEnterPassword("パスワード")
      .SaveCookies("user.json"))
```

```
(TwitterFrontendFlow()
        .LoadCookies("user.json"))
```

## after login
おまけ程度
### ツイート
```
print(TwitterFrontendFlow()
        .LoadCookies("user.json")
        .CreateTweet("ツイートしたい文字列").content)
```


## sample
中身見たほうが早いかも<br>
[sample.py](https://github.com/fa0311/TwitterFrontendFlow/blob/master/sample.py)

## help

### inappropriate method
LoginFlowのリクエストを送る順番が不適切と検知した場合に表示されます<br>
あくまで検知なのでこれをバイパスする方法があります
```
flow = TwitterFrontendFlow()
flow.method_check_bypass = True
```