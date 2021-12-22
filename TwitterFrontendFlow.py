import requests
import json

class TwitterFrontendFlow:
    def __init__(self):
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        self.AUTHORIZATION =  "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
        self.session = requests.session()
        self.__twitter()
        self.x_guest_token = self.__get_guest_token()

    def __twitter(self):
        headers = {
            "User-Agent": self.USER_AGENT,
        }
        response = self.session.get(
            "https://twitter.com/", headers=headers
        )

    def __get_guest_token(self):
        headers = {
            "authorization": self.AUTHORIZATION,
            "User-Agent": self.USER_AGENT,
        }
        response = self.session.post(
            "https://api.twitter.com/1.1/guest/activate.json", headers=headers
        ).json()
        return response["guest_token"]

    def __get_headers(self):
        return {
            "authorization": self.AUTHORIZATION,
            "User-Agent": self.USER_AGENT,
            "x-guest-token": self.x_guest_token,
            "x-twitter-active-user": "yes",
            "x-twitter-client-language": "ja"
        }

    # ログイン

    def login_flow(self):
        data = {
            "input_flow_data":{
                "flow_context":{
                    "debug_overrides":{},
                    "start_location":{
                        "location":"splash_screen"
                    }
                }
            },
            "subtask_versions":{
                "contacts_live_sync_permission_prompt":0,
                "email_verification":1,
                "topics_selector":1,
                "wait_spinner":1,
                "cta":4
            }
        }
        params = {
            "flow_name":"login"
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data, params=params
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def LoginJsInstrumentationSubtask(self):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"LoginJsInstrumentationSubtask",
                "js_instrumentation": {
                    "response":json.dumps({
                        "rf": {
                            "af07339bbc6d24ced887d705eb0c9fd29b4a7d7ddc21136c9f94d53a4bc774d2": 88,
                            "a6ce87d6481c6ec4a823548be3343437888441d2a453061c54f8e2eb325856f7": 250,
                            "a0062ad06384a8afd38a41cd83f31b0dbfdea0eff4b24c69f0dd9095b2fb56d6": 16,
                            "a929e5913a5715d93491eaffaa139ba4977cbc826a5e2dbcdc81cae0f093db25": 186
                        },
                        "s": "Q-H-53m1uXImK0F0ogrxRQtCWTH1KIlPbIy0MloowlMa4WNK5ZCcDoXyRs1q_cPbynK73w_wfHG_UVRKKBWRoh6UJtlPS5kMa1p8fEvTYi76hwdzBEzovieR8t86UpeSkSBFYcL8foYKSp6Nop5mQR_QHGyEeleclCPUvzS0HblBJqZZdtUo-6by4BgCyu3eQ4fY5nOF8fXC85mu6k34wo982LMK650NsoPL96DBuloqSZvSHU47wq2uA4xy24UnI2WOc6U9KTvxumtchSYNnXq1HV662B8U2-jWrzvIU4yUHV3JYUO6sbN6j8Ho9JaUNJpJSK7REwqCBQ3yG7iwMAAAAX2Vqcbs"
                    }),
                    "link":"next_link"
                }
            }
        ]}
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def LoginEnterUserIdentifierSSOSubtask(self, user_id):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"LoginEnterUserIdentifierSSOSubtask",
                "settings_list":{
                    "setting_responses":[{
                        "key":"user_identifier",
                        "response_data":{
                            "text_data":{
                                "result":user_id
                            }
                        }
                    }],"link":"next_link"
                }
            }]
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def AccountDuplicationCheck(self):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"AccountDuplicationCheck",
                "check_logged_in_account":{
                    "link":"AccountDuplicationCheck_false"
                }
            }]
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def LoginEnterAlternateIdentifierSubtask(self, text):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"LoginEnterAlternateIdentifierSubtask",
                "enter_text":{
                    "text":text,
                    "link":"next_link"
                }
            }]
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def LoginEnterPassword(self, password):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"LoginEnterPassword",
                "enter_password":{
                    "password":password,
                    "link":"next_link"
                }
            }]
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def LoginTwoFactorAuthChallenge(self, TwoFactorCode):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"LoginTwoFactorAuthChallenge",
                "enter_text":{
                    "text": TwoFactorCode,
                    "link":"next_link"
                }
            }]
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    # パスワードリセット

    def password_reset_flow(self):
        data = {
            "input_flow_data":{
                "flow_context":{
                    "debug_overrides":{},
                    "start_location":{
                        "location":"manual_link"
                    }
                }
            },
            "subtask_versions":{
                "contacts_live_sync_permission_prompt":0,
                "email_verification":1,
                "topics_selector":1,
                "wait_spinner":1,
                "cta":4
            }
        }
        params = {
            "flow_name":"password_reset"
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data, params=params
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def PwrJsInstrumentationSubtask(self):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"PwrJsInstrumentationSubtask",
                "js_instrumentation": {
                    "response":json.dumps({
                        "rf": {
                            "af07339bbc6d24ced887d705eb0c9fd29b4a7d7ddc21136c9f94d53a4bc774d2": 88,
                            "a6ce87d6481c6ec4a823548be3343437888441d2a453061c54f8e2eb325856f7": 250,
                            "a0062ad06384a8afd38a41cd83f31b0dbfdea0eff4b24c69f0dd9095b2fb56d6": 16,
                            "a929e5913a5715d93491eaffaa139ba4977cbc826a5e2dbcdc81cae0f093db25": 186
                        },
                        "s": "Q-H-53m1uXImK0F0ogrxRQtCWTH1KIlPbIy0MloowlMa4WNK5ZCcDoXyRs1q_cPbynK73w_wfHG_UVRKKBWRoh6UJtlPS5kMa1p8fEvTYi76hwdzBEzovieR8t86UpeSkSBFYcL8foYKSp6Nop5mQR_QHGyEeleclCPUvzS0HblBJqZZdtUo-6by4BgCyu3eQ4fY5nOF8fXC85mu6k34wo982LMK650NsoPL96DBuloqSZvSHU47wq2uA4xy24UnI2WOc6U9KTvxumtchSYNnXq1HV662B8U2-jWrzvIU4yUHV3JYUO6sbN6j8Ho9JaUNJpJSK7REwqCBQ3yG7iwMAAAAX2Vqcbs"
                    }),
                    "link":"next_link"
                }
            }
        ]}
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def PasswordResetBegin(self, user_id):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"PasswordResetBegin",
                "enter_text":{
                    "text":user_id,
                    "link":"next_link"
                }
            }]
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def PasswordResetChooseChallenge(self):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"PasswordResetChooseChallenge",
                "choice_selection":{
                    "link":"next_link",
                    "selected_choices":["0"]
                }
            }]
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self

    def PasswordResetConfirmChallenge(self, code):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id":"PasswordResetConfirmChallenge",
                "enter_text":{
                    "text":code,
                    "link":"next_link"
                }
            }]
        }
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data
        ).json()
        self.flow_token = response["flow_token"]
        self.content = response
        return self