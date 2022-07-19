# 12 리스트 2 추가, 수정, 삭제

#리스트 추가, 수정, 삭제

eng_scores = [90, 60, 70, 100, 85]

#추가 -> append() 사용 (맨 뒤에 추가)
eng_scores.append(99)

print("추가 - ", eng_scores)
'''
추가 -  [90, 60, 70, 100, 85, 99]
'''

#수정 -> index 사용
eng_scores[-1] = 38
print("수정 - ", eng_scores)
'''
수정 -  [90, 60, 70, 100, 85, 38]
'''

#삭제 -> del과 index 사용
del eng_scores[-1]
print("삭제 - ", eng_scores)
'''
삭제 -  [90, 60, 70, 100, 85]
'''