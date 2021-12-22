from TwitterFrontendFlow import TwitterFrontendFlow

# print(TwitterFrontendFlow().login_flow().LoginJsInstrumentationSubtask().LoginEnterUserIdentifierSSOSubtask("_kmch4n_").content["subtasks"][0]["check_logged_in_account"]["user_id"])

# print(TwitterFrontendFlow().login_flow().LoginJsInstrumentationSubtask().LoginEnterUserIdentifierSSOSubtask("faa0311").AccountDuplicationCheck().LoginEnterAlternateIdentifierSubtask("不正検知されたとき メアドor電話番号").LoginEnterPassword("").LoginTwoFactorAuthChallenge("340908").content)

proxies = {
    "http":"",
    "https":""
}

print(TwitterFrontendFlow(proxies=proxies).login_flow().LoginJsInstrumentationSubtask().LoginEnterUserIdentifierSSOSubtask("faa0311").AccountDuplicationCheck().LoginEnterPassword("").LoginTwoFactorAuthChallenge("340908").content)

# print(TwitterFrontendFlow().password_reset_flow().PwrJsInstrumentationSubtask().PasswordResetBegin("_kmch4n_").PasswordResetChooseChallenge().PasswordResetConfirmChallenge().content)

# print(TwitterFrontendFlow().password_reset_flow().PwrJsInstrumentationSubtask().PasswordResetBegin("_kmch4n_").content["subtasks"][0]["choice_selection"]["choices"][0]["text"]["text"])