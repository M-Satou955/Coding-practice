929. Unique Email Addresses

## 問題文

有効なメールアドレスは、ローカル名とドメイン名から構成され、'@'記号で区切られています。小文字のアルファベットに加え、メールアドレスには 1 つ以上の'.'または'+'が含まれる場合があります。

例えば、"alice@leetcode.com" の場合、"alice" がローカル名、"leetcode.com" がドメイン名となります。
メールアドレスのローカル名部分において、特定の文字間にドット「.」を追加すると、そのメールはローカル名のドットを除いた同じアドレスに転送されます。ただし、このルールはドメイン名には適用されません。

例えば、"alice.z@leetcode.com" と "alicez@leetcode.com" は同じメールアドレスに転送されます。
ローカル名部分にプラス記号 '+' を追加すると、プラス記号の直後以降のすべての文字が無視されます。この仕組みにより、特定のメールをフィルタリングすることが可能です。ただし、このルールはドメイン名には適用されません。

例えば、"m.y+name@email.com" は "my@email.com" に転送されます。
これら 2 つのルールは同時に適用することが可能です。

文字列配列 emails が与えられており、各 emails[i] に対して 1 通ずつメールを送信する場合、実際にメールを受信する異なるアドレスの数 を返してください。

例 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
例 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

制約：

1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] は小文字の英字、'+'、'.'、および '@' で構成されています。
各 emails[i] には正確に 1 つの '@' 文字が含まれています。
すべてのローカル名とドメイン名は空ではありません。
ローカル名は '+' 文字で始まってはいけません。
ドメイン名は ".com" で終わるサフィックスを持ちます。
ドメイン名には、".com" サフィックスの前に少なくとも 1 文字含まれている必要があります。

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
```
