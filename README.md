# RSA 加密
本篇作為課程作業的筆記，著重在 RSA 加解密的實作流程與加速方法，不涉及其數學證明與推導。

## 程式執行
```bash
git clone https://github.com/Petingo/RSA
cd RSA/code
python3 test.py
```

## 公鑰、私鑰的產生：
1. 隨機生成兩質數 <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> 和 <img src="/tex/d5c18a8ca1894fd3a7d25f242cbe8890.svg?invert_in_darkmode&sanitize=true" align=middle width=7.928106449999989pt height=14.15524440000002pt/>，<img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/> 不等於 <img src="/tex/d5c18a8ca1894fd3a7d25f242cbe8890.svg?invert_in_darkmode&sanitize=true" align=middle width=7.928106449999989pt height=14.15524440000002pt/>
2. 計算 <img src="/tex/99807742b664b5795db8e44c216a5ee0.svg?invert_in_darkmode&sanitize=true" align=middle width=73.20746399999999pt height=22.465723500000017pt/>
3. 由歐拉函數可知，不大 <img src="/tex/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.99998994999999pt height=22.465723500000017pt/> 且與 <img src="/tex/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.99998994999999pt height=22.465723500000017pt/> 互質的整數個數為 <img src="/tex/63eb3ef6157e2497f42fa6c85b8f9e3c.svg?invert_in_darkmode&sanitize=true" align=middle width=118.4815137pt height=24.65753399999998pt/>；為方便表達，令 <img src="/tex/b92139a2a66c1726dda3e1761f6e8e3c.svg?invert_in_darkmode&sanitize=true" align=middle width=151.1525763pt height=24.65753399999998pt/>
4. 隨機挑選一個 <img src="/tex/8cd34385ed61aca950a6b06d09fb50ac.svg?invert_in_darkmode&sanitize=true" align=middle width=7.654137149999991pt height=14.15524440000002pt/> 與 <img src="/tex/417a5301693b60807fa658e5ef9f9535.svg?invert_in_darkmode&sanitize=true" align=middle width=10.75343279999999pt height=14.15524440000002pt/> 互質且小於 <img src="/tex/417a5301693b60807fa658e5ef9f9535.svg?invert_in_darkmode&sanitize=true" align=middle width=10.75343279999999pt height=14.15524440000002pt/>
5. 計算 <img src="/tex/8cd34385ed61aca950a6b06d09fb50ac.svg?invert_in_darkmode&sanitize=true" align=middle width=7.654137149999991pt height=14.15524440000002pt/> 對同餘 <img src="/tex/417a5301693b60807fa658e5ef9f9535.svg?invert_in_darkmode&sanitize=true" align=middle width=10.75343279999999pt height=14.15524440000002pt/> 的乘法反元素 <img src="/tex/2103f85b8b1477f430fc407cad462224.svg?invert_in_darkmode&sanitize=true" align=middle width=8.55596444999999pt height=22.831056599999986pt/>；意即 <img src="/tex/c26a2937d950ea3f50dc38156db13fa2.svg?invert_in_darkmode&sanitize=true" align=middle width=134.2690338pt height=24.65753399999998pt/> 
6. 得出公鑰 <img src="/tex/096daeeb51a014ef0b65694396cb8eff.svg?invert_in_darkmode&sanitize=true" align=middle width=41.83217774999999pt height=24.65753399999998pt/> 、私鑰 <img src="/tex/68c7e361f7dd1bff493ce75c7a902677.svg?invert_in_darkmode&sanitize=true" align=middle width=42.73400339999999pt height=24.65753399999998pt/>

## 加密
假設原始消息為 <img src="/tex/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/>，加密後的訊息為 <img src="/tex/3e18a4a28fdee1744e5e3f79d13b9ff6.svg?invert_in_darkmode&sanitize=true" align=middle width=7.11380504999999pt height=14.15524440000002pt/>，則可以利用公鑰 <img src="/tex/cd1c53037db59ccdf6015d027063c424.svg?invert_in_darkmode&sanitize=true" align=middle width=41.83217774999999pt height=24.65753399999998pt/> 計算
<p align="center"><img src="/tex/7c1f858c19a6da475813954cbb6edadd.svg?invert_in_darkmode&sanitize=true" align=middle width=106.16249655pt height=11.741602949999999pt/></p>

## 解密
利用私鑰 <img src="/tex/68c7e361f7dd1bff493ce75c7a902677.svg?invert_in_darkmode&sanitize=true" align=middle width=42.73400339999999pt height=24.65753399999998pt/> 可以計算出
<p align="center"><img src="/tex/cbe7b2c01880887e3d00aaf945e6b585.svg?invert_in_darkmode&sanitize=true" align=middle width=106.76867684999998pt height=14.77813755pt/></p>

## 加速
#### Miller-Rabin Test
快速驗證一個數是否為質數，根據[計算](https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes)，當 key 的長度在 2048 bits 時，迭代的次數最好 ≥ 40。
#### 快速冪
在 Miller-Rabin test 以及加解密的過程中會，需要不斷計算 <img src="/tex/75034c99247a2e593dd4e250f2209cb9.svg?invert_in_darkmode&sanitize=true" align=middle width=73.55207474999999pt height=27.91243950000002pt/>；可以採用 square and multiply（快速冪）進行加速。
#### 中國剩餘定理
詳細推導可以參考[這篇文章](http://jianiau.blogspot.com/2014/05/rsa-decrypt-with-crt.html)。
當擁有 <img src="/tex/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode&sanitize=true" align=middle width=8.270567249999992pt height=14.15524440000002pt/>、<img src="/tex/d5c18a8ca1894fd3a7d25f242cbe8890.svg?invert_in_darkmode&sanitize=true" align=middle width=7.928106449999989pt height=14.15524440000002pt/> 時，可以下列式子加速運算（<img src="/tex/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> 為明文，<img src="/tex/3e18a4a28fdee1744e5e3f79d13b9ff6.svg?invert_in_darkmode&sanitize=true" align=middle width=7.11380504999999pt height=14.15524440000002pt/> 為密文）：

<img src="/tex/82ec798fca965dfdd0baca4017052d92.svg?invert_in_darkmode&sanitize=true" align=middle width=136.63348874999997pt height=24.65753399999998pt/>
<img src="/tex/9882beb293b70f89a1bc3f9260b51dd5.svg?invert_in_darkmode&sanitize=true" align=middle width=135.95236544999997pt height=24.65753399999998pt/>
<img src="/tex/cb39edbecec5157dfe84dd7fe177bbf8.svg?invert_in_darkmode&sanitize=true" align=middle width=124.32928364999998pt height=26.76175259999998pt/>

上面可以先算好並存起來，每次解密時需要執行：

<img src="/tex/ae3d80a1a50ae4ac132122be4bc084f2.svg?invert_in_darkmode&sanitize=true" align=middle width=114.31543364999997pt height=27.91243950000002pt/>
<img src="/tex/6a0eaee1cf5fbe3564b658a95a0d6810.svg?invert_in_darkmode&sanitize=true" align=middle width=113.60380349999997pt height=27.91243950000002pt/>
<img src="/tex/e35e33d15dd6c3995b65bde61f29baac.svg?invert_in_darkmode&sanitize=true" align=middle width=204.80678954999996pt height=24.65753399999998pt/>
<img src="/tex/f01e6e887ea1c5055934d584df4f2ae8.svg?invert_in_darkmode&sanitize=true" align=middle width=115.73989514999998pt height=22.831056599999986pt/>

## 參考資料
- [RSA 介紹](https://blog.xuite.net/hellothere/blog/49077338-RSA非對稱加密演算法+%2B+公開密鑰加密+%2B+加密+%2B+數位簽章)
- [RSA python 實作](https://github.com/andrew-bodine/rsa)
- [中國剩餘定理推導](http://jianiau.blogspot.com/2014/05/rsa-decrypt-with-crt.html)
