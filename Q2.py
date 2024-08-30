import numpy as np
import time

def dot_product_vectorized(v1, v2):
    """Compute the dot product of two vectors using vectorized operations."""
    return np.dot(v1, v2)

def dot_product_scalar(v1, v2):
    """Compute the dot product of two vectors using a scalar (element-wise) approach in a loop."""
    result = 0.0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

def main():
    # Define the size of the vectors
    size = 10**6
    
    # Generate two large random vectors of the specified size
    v1 = 5 + 5 * np.random.rand(size)
    v2 = 1+ 4 * np.random.rand(size)
    
    # Compute dot product using vectorized operations
    start_time = time.time()
    dot_product_vec = dot_product_vectorized(v1, v2)
    vectorized_time = time.time() - start_time
    
    # Compute dot product using scalar approach
    start_time = time.time()
    dot_product_sca = dot_product_scalar(v1, v2)
    scalar_time = time.time() - start_time
    
    # Print the results
    print(f"Dot product (vectorized): {dot_product_vec}")
    print(f"Dot product (scalar): {dot_product_sca}")
    print(f"Execution time (vectorized): {vectorized_time:.6f} seconds")
    print(f"Execution time (scalar): {scalar_time:.6f} seconds")
    
    # Check if the results are close
    assert np.isclose(dot_product_vec, dot_product_sca), "Results do not match!"

if __name__ == "__main__":
    main()