# helper functions
def print_matrix(a, *args):
  if type(a) != list:
    print(a)
  print("\n" + "-" * 3, "BEGIN PRINT MATRIX", "-" * 3)
  for arg in args:
    print(arg)
  for column_vector in a:
    print(column_vector)
  print("-" * 3, "END PRINT MATRIX", "-" * 3)

def print_complete_matrix(a):
  for row in a:
    val = row.pop(-1)
    row.append("|")
    row.append(val)
  print_matrix(a)

def print_mxn(a):
  print(f"\n-- Matrix M*N --\nm = {len(a)}\nn = {len(a[0])}\n")
