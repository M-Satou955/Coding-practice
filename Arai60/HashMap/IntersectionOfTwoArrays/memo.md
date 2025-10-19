Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

2 つの整数配列 nums1 と nums2 が与えられたとき、その共通要素を含む配列を返してください。結果の配列には重複する要素を含めず、任意の順序で要素を返して構いません。

考え方
重複する要素を抜き出したいので、２つの配列を結合して重複を排除するときに排除されたやつを新しい配列にぶち込んでそれ返せばお K

- enumurate 使って index と num にわけて、num だけの配列作って重複してるやつ抜き出す

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = defaultdict(int)
        for num in nums1:
            seen[num] = 1

        res = []
        for num in nums2:
            if seen[num] == 1:
                seen[num] = 0
                res.append(num)
        return res
```

defaultdict を使う理由は存在しないキーにアクセスしても自動的に 0 を返すから

通常の辞書{}だと
存在しないキーにアクセスしようとしたら KeyError が発生する。
if num in seen and seen[num] == 1:

- 明示的＆num in seen が False なら、seen[num]は評価されない
  if seen.get(num, 0) == 1:
- デフォルト値が指定できる: この場合はキーが存在しない場合は 0 を返す

でチェックはできるけどどっちがいいんだろう

```python
# pythonの言語機能をフルで使うとこうかける
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
```

DeepWiki くんで調べた
https://deepwiki.com/search/i-want-to-know-the-implementat_eceba51b-9182-4758-8672-6a751676c32d?mode=fast

Python 3 の set 型は、python/cpython リポジトリ内の Objects/setobject.c ファイルに実装されてるっぽい
