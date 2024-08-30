import numpy as np
import matplotlib.pyplot as plt

def svd_operations(A, k_values):
    """
    Perform Singular Value Decomposition (SVD) and low-rank approximation on a matrix A,
    and plot the reconstruction errors for different values of k.

    Parameters:
    - A: The input matrix to decompose.
    - k_values: List of integers representing different values of k for low-rank approximation.
    
    Returns:
    - None (prints results and plots)
    """
    U, S, VT = np.linalg.svd(A, full_matrices=False)
    Sigma = np.diag(S)
    A_reconstructed = np.dot(U, np.dot(Sigma, VT))
    
    reconstruction_error = np.linalg.norm(A - A_reconstructed, 'fro')
    print(f"Reconstruction error (full SVD): {reconstruction_error:.4e}")
    errors = []

    for k in k_values:
        if k > len(S):
            k = len(S) 

        U_k = U[:, :k]
        S_k = np.diag(S[:k])
        VT_k = VT[:k, :]

        A_reconstructed_k = np.dot(U_k, np.dot(S_k, VT_k))

        reconstruction_error_k = np.linalg.norm(A - A_reconstructed_k, 'fro')
        errors.append(reconstruction_error_k)
        print(f"Reconstruction error (k={k}): {reconstruction_error_k:.4e}")

    plt.figure(figsize=(10, 6))
    plt.plot(k_values, errors, marker='o', linestyle='-', color='r')
    plt.xlabel('Number of Singular Values (k)')
    plt.ylabel('Reconstruction Error')
    plt.title('Reconstruction Error vs. Number of Singular Values')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    np.random.seed(0)
    A = np.random.rand(100, 100)
    k_values = [1, 5, 10, 20]
    svd_operations(A, k_values)