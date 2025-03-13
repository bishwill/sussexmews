import os

import paramiko


class SussexMewsSSHClient:
    def __init__(self, host: str, user: str, private_key_file: str, port: int = 22):
        self.host = host
        self.user = user
        self.private_key_file = private_key_file
        self.port = port

    def execute(self, cmd: str) -> str:
        with paramiko.SSHClient() as client:
            policy = paramiko.AutoAddPolicy()
            client.set_missing_host_key_policy(policy)
            pkey = paramiko.RSAKey.from_private_key_file(self.private_key_file)
            client.connect(self.host, username=self.user, pkey=pkey)
            _, stdout, _ = client.exec_command(cmd)

            return stdout.read().decode()


class CatfordCastleSSHClient(SussexMewsSSHClient):
    def __init__(self):
        super().__init__(
            "192.168.12.4",
            "pi",
            private_key_file=os.environ["CATFORD_CASTLE_PRIVATE_KEY_FILE"],
        )


class CatfordCastleMiniSSHClient(SussexMewsSSHClient):
    def __init__(self):
        super().__init__(
            "192.168.12.5",
            "pi",
            private_key_file=os.environ["CATFORD_CASTLE_MINI_PRIVATE_KEY_FILE"],
        )


if __name__ == "__main__":
    print(CatfordCastleSSHClient().execute("date"))
