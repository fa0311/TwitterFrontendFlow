# TwitterFrontendFlow
TwitterのLogin Flowをいじる

## proxy
```
TwitterFrontendFlow(proxies={
    "http":"",
    "https":""
})
```

## login flow

通常ログイン
```
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSOSubtask("電話番号/メールアドレス/ユーザー名")
      .AccountDuplicationCheck()
      .LoginEnterPassword("パスワード").content)
```
2段階認証
```
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSOSubtask("電話番号/メールアドレス/ユーザー名")
      .AccountDuplicationCheck()
      .LoginEnterPassword("パスワード")
      .LoginTwoFactorAuthChallenge("2段階認証のコード").content)
```
通常とは異なるログイン操作が行われました
```
print(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSOSubtask("電話番号/メールアドレス/ユーザー名")
      .AccountDuplicationCheck()
      .LoginEnterAlternateIdentifierSubtask("電話番号またはメールアドレス")
      .LoginEnterPassword("パスワード").content)
```
## password reset flow

```
print(TwitterFrontendFlow().
    password_reset_flow().
    PwrJsInstrumentationSubtask().
    PasswordResetBegin("電話番号/メールアドレス/ユーザー名").
    PasswordResetChooseChallenge().
    PasswordResetConfirmChallenge("認証コード").content)
```

個人情報を確認してください
```
print(TwitterFrontendFlow().
    password_reset_flow().
    PwrJsInstrumentationSubtask().
    PasswordResetBegin("電話番号/メールアドレス/ユーザー名").
    PwrKnowledgeChallenge("メールアドレス").
    PwrKnowledgeChallenge("電話番号").
    PasswordResetChooseChallenge().
    PasswordResetConfirmChallenge("認証コード").content)
```


## Save / Load
```
(TwitterFrontendFlow()
      .login_flow()
      .LoginJsInstrumentationSubtask()
      .LoginEnterUserIdentifierSSOSubtask("電話番号/メールアドレス/ユーザー名")
      .AccountDuplicationCheck()
      .LoginEnterPassword("パスワード")
      .SaveCookies("user.json"))
```

```
(TwitterFrontendFlow()
        .LoadCookies("user.json"))
```

## after login

ツイート
```
print(
(TwitterFrontendFlow()
        .LoadCookies("user.json")
        .CreateTweet("ツイートしたい文字列").content)
```


## sample
user_idを取得
```
print(TwitterFrontendFlow().
    login_flow().
    LoginJsInstrumentationSubtask().
    LoginEnterUserIdentifierSSOSubtask("電話番号/メールアドレス/ユーザー名").
    content["subtasks"][0]["check_logged_in_account"]["user_id"])
```

メールアドレスを取得
```
print(TwitterFrontendFlow().
    password_reset_flow().
    PwrJsInstrumentationSubtask().
    PasswordResetBegin("電話番号/メールアドレス/ユーザー名").
    content["subtasks"][0]["choice_selection"]["choices"][0]["text"]["text"])
```