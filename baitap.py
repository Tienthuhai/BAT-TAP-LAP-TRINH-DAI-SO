import numpy as np
A=np.array([[8,2,2],[1,8,2],[6,9,1]])
B=np.array([[5,3,4],[3,5,7],[5,7,7]])
print(A+B)
print(A-B)
print(A.dot(B))
print(A*B)
print(np.linalg.det(A))
print(np.linalg.inv(A))
print(A.T)
print(np.linalg.pinv(A))
print(np.linalg.norm(A))
print(np.linalg.norm(A,1))
print(np.linalg.norm(A,2))
print(A[:2,:2])
print(2*A)
print(A.T.dot(A))
print(np.trace(A))
print(np.linalg.eig(A))
def is_diagonalizable(A):
     eigenvalues, eigenvectors = np.linalg.eig(A)
     return np.linalg.matrix_rank(eigenvectors) == A.shape[0]
if is_diagonalizable(A):
    print("Ma trận A có thể chéo hóa.")
else:
    print("Ma trận A không thể chéo hóa.")
C=np.array([[1,1,1,],[1,1,1],[1,1,1]])
print(C+A)
print(np.random.rand(3, 3))
D =(print(np.random.rand(4,4)))
def is_invertible(D):
    try:
        # Tính ma trận nghịch đảo
        D_inv = np.linalg.inv(D)
        return True, D_inv
    except np.linalg.LinAlgError:
        # Nếu xảy ra lỗi, ma trận không khả nghịch
        return False, None
invertible, D_inv = is_invertible(D)

if invertible:
    print("Ma trận D có khả nghịch.")
    print("Ma trận nghịch đảo D^-1 là:")
    print(D_inv)
else:
    print("Ma trận D không có khả nghịch.")
d=A.T.dot(B).dot(A)
print(d)
print(np.linalg.det(d))
print(np.linalg.inv(d))
e=np.random.rand(4,4)
I4=np.eye(4)
print(e+I4)