1.运行python的mapper、reduce程序
echo 'hello a b c a b c d e a'  | python mapper.py |sort -k1,1 |python reduce.py
