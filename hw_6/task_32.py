# ������ 32: ���������� ������� ��������� ������� (������), 
# �������� ������� ����������� ��������� ��������� 
# (�.�. �� ������ ��������� �������� � �� ������ ��������� ���������)

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

inp_min = int(input('Min: '))
inp_max = int(input('Max: '))

# �������� ������ ���� ��������� ������� ����� ���������
# �������� ���� ������������ �� ����� ����� ����� ������ � ������ ))
if inp_min > inp_max:
    inp_min, inp_max = inp_max, inp_min

# �������� ������ (�������� ��������)
if inp_min < min(lst): inp_min = min(lst)
if inp_max > max(lst): inp_max = max(lst)

# ������� ������ ��� ��������
lst_enter = [*range(inp_min, inp_max)]

# �������� ���� ���������
lst_indx = []
for i in range(len(lst)):
    if lst[i] in lst_enter:
        lst_indx.append(i)

print(lst_indx)

