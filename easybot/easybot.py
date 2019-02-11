class Easybot_client:

    def __init__(self, discord_client):
        self.discord_client = discord_client

    def run_from_token_txt(path):
        token_file = open(path, 'r')
        token = token_file.readline().replace('\n', '')
        token_file.close()
        self.discord_client.run(token)
