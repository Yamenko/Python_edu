#� ���������� ��������� � ������� ���������� �������. 
#��� ����� �� ������� ������, ������ ����� �������� ������ �� ����������. 
#����� �������, � ������� ����� ���� ����� ��� ��������. 

#����� �� ������ ����� N ������.

#��� ����� �������� ������ ������������, ������� �� ������� ����� �� ��� ������� ��������� ����� ���� � �� i-�� ����� ������� ai ����.
#� ���� ���������� ��������� �������� ������� ��������������� ����� �������. ��� ������� ������� �� ������������ ������ � ���������� ���������� �������. ���������� ������ �� ���� �����, �������� ��������������� ����� ��������� ������, �������� ����� � ����� ����� � � ���� �������� � ���.
#�������� ��������� ��� ���������� ������������� ����� ����, ������� ����� ������� �� ���� ����� ���������� ������, �������� ����� ��������� ������ �������� �� ������� ����� ������.


max_berry = 0
kusts = [13, 5, 8, 1, 3, 15, 7, 11, 4, 16, 9]

for i in range(len(kusts), 0, -1):
    tmp_step = kusts[0 - i] + kusts[1 - i] + kusts[2 - i]
    max_berry = tmp_step if max_berry < tmp_step else max_berry

print(max_berry)