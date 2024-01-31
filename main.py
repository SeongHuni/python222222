# 문자열 속 따옴표 표시
'''
Food = "Python's favorite food is perl"
Say = '"python is very easy." he says.'
'''

food = "python's favorite food is perl"
print(food)

Say = '"python is very easy." he says.'
print(Say)

food = 'python\'s favorite food is perl'
Say = "\"python is very easy.\" he says."
print(food)
print(Say)

#여러줄인 문자열을 변수에 대입
"""
Life is too short
You need python
"""

multiline = "Life is too short \n You need python"
print(multiline)

multiline = '''
   life is too short
   you need python
   '''
print(multiline)