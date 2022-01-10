from TwitterFrontendFlow.TwitterFrontendFlow import TwitterFrontendFlow

flow = TwitterFrontendFlow()

print(
"""login: ログイン
password_reset: パスワードリセット
load: cookieのロード""")

action = input()

if action == "login":
    flow.login_flow()
    flow.LoginJsInstrumentationSubtask()
    if "LoginEnterUserIdentifierSSOSubtask"in flow.get_subtask_ids():
        print("電話番号/メールアドレス/ユーザー名")
        flow.LoginEnterUserIdentifierSSOSubtask(input())
    if "LoginEnterAlternateIdentifierSubtask"in flow.get_subtask_ids():
        print(flow.content["subtasks"][0]["enter_text"]["primary_text"]["text"])
        flow.LoginEnterAlternateIdentifierSubtask(input())
    if "LoginEnterPassword"in flow.get_subtask_ids():
        print(flow.content["subtasks"][0]["enter_password"]["primary_text"]["text"])
        flow.LoginEnterPassword(input())
    if "LoginTwoFactorAuthChallenge"in flow.get_subtask_ids():
        print(flow.content["subtasks"][0]["enter_text"]["header"]["primary_text"]["text"])
        flow.LoginTwoFactorAuthChallenge(input())
    if "LoginSuccessSubtask"in flow.get_subtask_ids():
        print("ログインしました")

elif action == "password_reset":
    flow.password_reset_flow()
    flow.PwrJsInstrumentationSubtask()
    if "PasswordResetBegin"in flow.get_subtask_ids():
        print("電話番号/メールアドレス/ユーザー名")
        flow.PasswordResetBegin(input())
    if "PwrKnowledgeChallenge"in flow.get_subtask_ids():
        print(flow.content["subtasks"][0]["enter_text"]["secondary_text"]["text"])
        flow.PwrKnowledgeChallenge(input())
    if "PwrKnowledgeChallenge"in flow.get_subtask_ids():
        print(flow.content["subtasks"][0]["enter_text"]["secondary_text"]["text"])
        flow.PwrKnowledgeChallenge(input())
    if "PasswordResetChooseChallenge"in flow.get_subtask_ids():
        print("\n".join([choices["id"] + ": " + choices["text"]["text"] for choices in flow.content["subtasks"][0]["choice_selection"]["choices"]]))
        flow.PasswordResetChooseChallenge(input())
    if "PasswordResetConfirmChallenge"in flow.get_subtask_ids():
        print("コードを入力")
        flow.PasswordResetConfirmChallenge(input())
    if "PasswordResetNewPassword"in flow.get_subtask_ids():
        print("新しいパスワードを入力")
        flow.PasswordResetNewPassword(input())
    if "PasswordResetSurvey"in flow.get_subtask_ids():
        print("パスワードを変更した理由を教えてください")
        print("\n".join([choices["id"] + ": " + choices["text"]["text"] for choices in flow.content["subtasks"][0]["choice_selection"]["choices"]]))
        flow.PasswordResetSurvey(input())
    exit()

elif action == "load":
    print("ファイル名")
    flow.LoadCookies(input())

while True:
    print(
"""tweet: ツイート
fav: いいね
unfav: いいね取り消し
rt: リツイート
unrt: リツイート取り消し
follow: フォロー
unfollow: フォロー取り消し
save: cookieの出力
end: 終了""")

    action = input()

    if action == "tweet":
        print("ツイート内容")
        flow.CreateTweet(input())
    elif action == "fav":
        print("ツイートid")
        flow.FavoriteTweet(input())
    elif action == "unfav":
        print("ツイートid")
        flow.UnfavoriteTweet(input())
    elif action == "rt":
        print("ツイートid")
        flow.CreateRetweet(input())
    elif action == "unrt":
        print("ツイートid")
        flow.DeleteRetweet(input())
    elif action == "follow":
        print("ユーザー内部id")
        flow.friendships_create(input())
    elif action == "unfollow":
        print("ユーザー内部id")
        flow.friendships_destroy(input())
    elif action == "save":
        print("ファイル名")
        flow.SaveCookies(input())
    elif action == "end":
        break