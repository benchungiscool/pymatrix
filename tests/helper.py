# helper functions
def print_matrix(a):
  print("\n" + "-" * 3, "BEGIN PRINT MATRIX", "-" * 3)
  for column_vector in a:
    print(column_vector)
  print("-" * 3, "END PRINT MATRIX", "-" * 3)

def print_mxn(a):
  print(f"\n-- Matrix M*N --\nm = {len(a)}\nn = {len(a[0])}\n")
