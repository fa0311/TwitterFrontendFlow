import requests
import json

class TwitterFrontendFlow:
    def __init__(self, proxies={}):
        self.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
        self.AUTHORIZATION =  "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"
        self.proxies = proxies
        self.session = requests.session()
        self.__twitter()
        self.x_guest_token = self.__get_guest_token()

    def __twitter(self):
        headers = {
            "User-Agent": self.USER_AGENT,
        }
        response = self.session.get(
            "https://twitter.com/", headers=headers, proxies=self.proxies
        )

    def __get_guest_token(self):
        headers = {
            "authorization": self.AUTHORIZATION,
            "User-Agent": self.USER_AGENT,
        }
        response = self.session.post(
            "https://api.twitter.com/1.1/guest/activate.json", headers=headers, proxies=self.proxies
        ).json()
        return response["guest_token"]

    def __get_headers(self):
        return {
            "authorization": self.AUTHORIZATION,
            "User-Agent": self.USER_AGENT,
            "Content-type": "application/json",
            "x-guest-token": self.x_guest_token,
            "x-csrf-token": self.session.cookies.get('ct0'),
            "x-twitter-active-user": "yes",
            "x-twitter-client-language": "ja",
        }

    # Cookieの保存(jsonだから本番環境では使わないように)

    def LoadCookies(self, file_path):
        with open(file_path, 'r') as f:
            for cookie in json.load(f):
                self.session.cookies.set_cookie(requests.cookies.create_cookie(**cookie))
        return self

    def SaveCookies(self, file_path):
        cookies=[]
        for cookie in self.session.cookies:
            cookie_dict = dict(
                version=cookie.version,
                name=cookie.name,
                value=cookie.value,
                port=cookie.port,
                domain=cookie.domain,
                path=cookie.path,
                secure=cookie.secure,
                expires=cookie.expires,
                discard=cookie.discard,
                comment=cookie.comment,
                comment_url=cookie.comment_url,
                rfc2109=cookie.rfc2109,
                rest=cookie._rest
            )
            cookies.append(cookie_dict)

        with open(file_path, 'w') as f:
            json.dump(cookies, f, indent=4)
        return self

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
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data, params=params, proxies=self.proxies
        ).json()
        self.content = response
        self.flow_token = self.content["flow_token"]
        self.subtask_id = self.content["subtasks"][0]["subtask_id"]
        return self

    def flow(self):
        data = {
            "flow_token": self.flow_token,
            "subtask_inputs":[{
                "subtask_id": self.subtask_id,
            }]
        }
        print(data)
        response = self.session.post(
            "https://twitter.com/i/api/1.1/onboarding/task.json", headers=self.__get_headers(), json=data, proxies=self.proxies
        ).json()
        self.content = response

        for i, subtask in enumerate(self.content["subtasks"]):
            if "check_logged_in_account" in subtask:
                for ii, link in enumerate(subtask["check_logged_in_account"]):
                    print("{0}:{1}: {2}".format(i, ii, link["link_id"]))
            else:
                print("{0}: {1}".format(i, subtask["subtask_id"]))

        subtask = self.content["subtasks"][int(input())]
        
        
        
        # for i, subtask in enumerate(self.content["subtasks"]):subtask["settings_list"]["settings"]
        
        if "check_logged_in_account" in subtask:
            self.subtask_id = subtask["check_logged_in_account"][int(input())]["link_id"]
        else:
            self.subtask_id = subtask["subtask_id"]

        self.flow_token = self.content["flow_token"]
        return self

    # ログイン後

    def CreateTweet(self, tweet_text):
        data = {
            "queryId": "XyvN0Wv13eeu_gVIHDi10g",
            "variables": json.dumps({
            "tweet_text": tweet_text,
            "media": {
                "media_entities": [],
                "possibly_sensitive": False
            },
            "withDownvotePerspective": False,
            "withReactionsMetadata": False,
            "withReactionsPerspective": False,
            "withSuperFollowsTweetFields": True,
            "withSuperFollowsUserFields": False,
            "semantic_annotation_ids": [],
            "dark_request": False,
            "withBirdwatchPivots": False
            })
        }
        response = self.session.post(
            "https://twitter.com/i/api/graphql/XyvN0Wv13eeu_gVIHDi10g/CreateTweet", headers=self.__get_headers(), json=data
        ).json()
        self.content = response
        return self