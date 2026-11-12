"""String comparison examples"""


from ch7.interning_and_compare import are_equal

s1 = "Andrew"
s2 = "andrew"

are_equal(s1, s2)

# 'A' < 'a' because the ASCII value of 'A' is 65 and the ASCII value of 'a' is 97
is_s1_lt_s2 = s1 < s2       # True
is_s1_gt_s2 = s1 > s2       # False