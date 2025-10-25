class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # すでに出たドメイン名 or フルアドレスを格納する
        prevaddress = {}
        for email in emails:
            # 文字列操作を行い+があるかどうかで条件分岐
        # +がある場合は+〜@の間は無視した文字列を重複しているか調査する対象にする
