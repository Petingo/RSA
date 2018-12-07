# RSA 加密
本篇作為課程作業的筆記，著重在 RSA 加解密的實作流程與加速方法，不涉及其數學證明與推導。
## 公鑰、私鑰的產生：
1. 生成兩質數 $p$ 和 $q$，$p$ 不等於 $q$
2. 計算 $N=p \times q$
3. 由歐拉函數可知，不大 $N$ 且與 $N$ 互質的整數個數為 $(p-1)\times(q-1)$；為方便表達，令 $\varphi = (p-1)\times(q-1)$
4. 隨機挑選一個 $e$ 與 $\varphi$ 互質且小於 $\varphi$
5. 計算 $e$ 對同於 $\varphi$ 的乘法反元素 $d$；意即 $d \times e\equiv1\pmod{\varphi}$ 
6. 得出公鑰 $(N,e)$ 、私鑰 $(N,d)$

## 加密
假設原始消息為 $m$，加密後的訊息為 $c$，則可以利用公鑰 $(N, e)$ 計算
$$c = m ^ e \bmod{N}$$

## 解密
利用私鑰 $(N,d)$ 可以計算出
$$m = c ^ d \bmod{N}$$

## 加速
#### Miller-Rabin Test
快速驗證一個數是否為質數，根據[計算](https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes)，當 key 的長度在 2048 bits 時，迭代的次數最好 ≥ 40。
#### 快速冪
在 Miller-Rabin test 以及加解密的過程中會，需要不斷計算 $x ^ h \bmod N$；可以採用 square and multiply（快速冪）進行加速。
#### 中國剩餘定理
詳細推導可以參考[這篇文章](http://jianiau.blogspot.com/2014/05/rsa-decrypt-with-crt.html)。
當擁有 $p$、$q$ 時，可以下列式子加速運算（$m$ 為明文，$c$ 為密文）：

$d_p = d \bmod{(p-1)}$
$d_q = d \bmod{(q-1)}$
$q_{inv} = q^{-1} \bmod{p}$

上面可以先算好並存起來，每次解密時需要執行：

$m_1 = c^{d_p} \bmod{p}$
$m_2 = c^{d_q} \bmod{q}$
$h = q_{inv} \times (m_1 - m_2) \bmod{p}$
$m = m_2 + h \times q$

## 參考資料
- [RSA 介紹](https://blog.xuite.net/hellothere/blog/49077338-RSA非對稱加密演算法+%2B+公開密鑰加密+%2B+加密+%2B+數位簽章)
- [RSA python 實作](https://github.com/andrew-bodine/rsa)
- [中國剩餘定理推導](http://jianiau.blogspot.com/2014/05/rsa-decrypt-with-crt.html)
