
# ������ 36: �������� ������� print_operation_table(operation, num_rows=6, num_columns=6), 
# ������� ��������� � �������� ��������� �������, ����������� ������� �� ������ ������ � �������. 
# ��������� num_rows � num_columns ��������� ����� ����� � �������� �������, ������� ������ ���� �����������. 
# ��������� ����� � �������� ���� � ������� (���������, ������ �� � ����). 
# 
# ����������: �������� ��������� ���������� ����� ��������, � ������� ����� ��� ���������, ���, ��������, � �������� ���������.

# *������:*

# **����:** `print_operation_table(lambda x, y: x * y) ` 
# **�����:**
# 1 2  3  4  5  6
# 2 4  6  8  10 12
# 3 6  9  12 15 18
# 4 8  12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        my_l = list()
        for j in range(1, num_columns + 1):
            my_l.append(operation(i ,j))
        print (*my_l)
        #print(*[f"{my_l:>3}"])

print_operation_table(lambda x, y: x * y) 