from TwitterFrontendFlow.TwitterFrontendFlow.TwitterFrontendFlow import *

flow = TwitterFrontendFlow()

flow.login_flow()
flow.LoginJsInstrumentationSubtask()

while "LoginSuccessSubtask" not in flow.get_subtask_ids():
    try:
        if "LoginEnterUserIdentifierSSO" in flow.get_subtask_ids():
            print("Telephone number / Email address / User name")
            flow.LoginEnterUserIdentifierSSO(input())
        elif "LoginEnterAlternateIdentifierSubtask" in flow.get_subtask_ids():
            print(flow.content["subtasks"][0]["enter_text"]["primary_text"]["text"])
            flow.LoginEnterAlternateIdentifierSubtask(input())
        elif "LoginEnterPassword" in flow.get_subtask_ids():
            print(flow.content["subtasks"][0]["enter_password"]["primary_text"]["text"])
            flow.LoginEnterPassword(input())
        elif "AccountDuplicationCheck" in flow.get_subtask_ids():
            print("AccountDuplicationCheck")
            flow.AccountDuplicationCheck()
        elif "LoginTwoFactorAuthChallenge" in flow.get_subtask_ids():
            header = flow.content["subtasks"][0]["enter_text"]["header"]
            print(header["primary_text"]["text"])
            flow.LoginTwoFactorAuthChallenge(input())
        elif "LoginAcid" in flow.get_subtask_ids():
            header = flow.content["subtasks"][0]["enter_text"]["header"]
            print(header["secondary_text"]["text"])
            flow.LoginAcid(input())
        elif "SuccessExit" in flow.get_subtask_ids():
            break
        else:
            print("Non-supported login methods: " + flow.get_subtask_ids())
            exit(1)

    except:
        print("Error")

print("Success")
flow.SaveCookies("cookie.json")
