from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient


class OAuth2ConfidentialClientExample:

    # エンドポイント情報
    token_endpoint = 'http://localhost:5000/token'
    user_endpoint = 'http://localhost:5000/users/{user_id}'
    # 認証資格情報
    credentials = {
        'client_id': 'my_client_id',
        'client_secret': 'my_client_id_secret'
    }

    def init_session(self):
        """
        OAuth2セッションを開始します。
        """
        client = BackendApplicationClient(
            client_id=self.credentials['client_id'])
        self._sess = OAuth2Session(client=client)

    def fetch_token(self):
        """
        アクセストークンを取得します。
        """
        return self._sess.fetch_token(
            token_url=self.token_endpoint,
            client_id=self.credentials['client_id'],
            client_secret=self.credentials['client_secret']
        )
    
    def get_user(self, user_id):
        """
        ユーザー情報を取得します。
        """
        return self._sess.get(self.user_endpoint.format(user_id=user_id))

dummy_token = {
     'access_token': 'dummy_access_token',
     'token_type': 'bearer',
     'expires_in': 9999,
     'scope': 'dummy_scope'
 }


 
{'access_token': 'dummy_access_token', 'token_type': 'bearer', 'expires_in': 9999, 'scope': ['dummy_scope'], 'expires_at': 1558495687.1986227}
