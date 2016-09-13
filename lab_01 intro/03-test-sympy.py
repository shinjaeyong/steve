#-*- coding: utf8 -*-
#symbolic processor 기능을 가진 sympy를 불러 들여 sp라는 이름과 연결시킴
import  sympy as sp

#sympy d의 symbols 기능을 이용해 기호 x y를 정함
x, y = sp.symbols('x y')

#기호 x y를 이용해 기호 z를 정함
z  =  x +2 *y

#기호 z 를 화면에 표시함
print ('z = %s' %z)

#Sympy Tutorial, http://docs.sympy.org/latest/tutorial/index.html