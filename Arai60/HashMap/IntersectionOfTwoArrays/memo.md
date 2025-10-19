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

DeepWiki くんで set について調べた
https://deepwiki.com/search/i-want-to-know-the-implementat_eceba51b-9182-4758-8672-6a751676c32d?mode=fast

Python 3 の set 型は、python/cpython リポジトリ内の Objects/setobject.c ファイルに実装されてるっぽい

set_and などの名前？で集合に対する操作が実装されてるっぽい

PyNumberMethods 構造体は、Python オブジェクトが数値演算子（+, -, &など）をどう処理するかを定義してる？

```c
static PyNumberMethods frozenset_as_number = {
    0,                    // nb_add          → + 演算子（未定義）
    set_sub,              // nb_subtract     → - 演算子（差集合）
    0,                    // nb_multiply     → * 演算子（未定義）
    0,                    // nb_remainder    → % 演算子（未定義）
    0,                    // nb_divmod       → divmod()（未定義）
    0,                    // nb_power        → ** 演算子（未定義）
    0,                    // nb_negative     → -x（未定義）
    0,                    // nb_positive     → +x（未定義）
    0,                    // nb_absolute     → abs()（未定義）
    0,                    // nb_bool         → bool()（未定義）
    0,                    // nb_invert       → ~（未定義）
    0,                    // nb_lshift       → <<（未定義）
    0,                    // nb_rshift       → >>（未定義）
    set_and,              // nb_and          → & 演算子（積集合）
    set_xor,              // nb_xor          → ^ 演算子（対称差）
    set_or,               // nb_or           → | 演算子（和集合）
};

```

Python の frozenset 型に対する数値演算子のオーバーロードを定義しているコード？

frozenset で使える演算子

```python
a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

# 以下の演算が可能（上記のC実装による）
a - b   # {1}        差集合
a & b   # {2, 3}     積集合（先ほどの問題で使った！）
a ^ b   # {1, 4}     対称差
a | b   # {1,2,3,4}  和集合

# 以下はエラー（0が設定されているため）
a + b   # TypeError: unsupported operand type(s)
a * 2   # TypeError: unsupported operand type(s)
```

frozenset は集合型なので、集合演算（&, |, -, ^）のみサポートし
算術演算（+, \*など）は集合として意味がないので未定義ぽい

set と list と dict がややこしい

- set(nums1) → 集合型（set クラス）
- 辞書型（dict）は{key: value}の形

```python
x = {}           # これは dict（辞書）
type(x)          # <class 'dict'>

y = set()        # 空のsetを作るにはこう書く
type(y)          # <class 'set'>
```
