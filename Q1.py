import numpy as np

def generate_random_array(rows, cols):
    """Generate a random 2D array with specified dimensions."""
    np.random.seed(0)  # Seed for reproducibility
    return np.random.rand(rows, cols)

def compute_statistics(A):
    """Calculate the minimum, maximum, median, mean, and standard deviation of the array."""
    min_A = np.min(A)
    max_A = np.max(A)
    median_A = np.median(A)
    mean_A = np.mean(A)
    std_dev_A = np.std(A)
    
    print(f"Minimum: {min_A}")
    print(f"Maximum: {max_A}")
    print(f"Median: {median_A}")
    print(f"Mean: {mean_A}")
    print(f"Standard Deviation: {std_dev_A}")
    
    return min_A, max_A, median_A, mean_A, std_dev_A

def compute_statistics_along_first_dim(A):
    """Compute mean and variance along the first dimension and perform normalization and standardization."""
    mean_along_axis0 = np.mean(A, axis=0)
    variance_along_axis0 = np.var(A, axis=0)
    
    # Normalization and standardization
    min_A = np.min(A, axis=0)
    max_A = np.max(A, axis=0)
    A_normalized = (A - min_A) / (max_A - min_A)
    A_standardized = (A - mean_along_axis0) / np.sqrt(variance_along_axis0)
    
    return mean_along_axis0, variance_along_axis0, A_normalized, A_standardized

def main():
    # Take user input for array dimensions
    try:
        rows = int(input("Enter the number of rows for the 2D array: "))
        cols = int(input("Enter the number of columns for the 2D array: "))
        
        if rows <= 0 or cols <= 0:
            raise ValueError("Dimensions must be positive integers.")
        
        # Generate the random 2D array
        A = 10 + 10 * generate_random_array(rows, cols)
        
        print("\nGenerated 2D Array:")
        print(A)
        
        # Compute statistics
        min_A, max_A, median_A, mean_A, std_dev_A = compute_statistics(A)
        
        # Compute statistics along the first dimension
        mean_along_axis0, variance_along_axis0, A_normalized, A_standardized = compute_statistics_along_first_dim(A)
        
        print("\nMean along the first dimension:", mean_along_axis0)
        print("Variance along the first dimension:", variance_along_axis0)
        
        print("\nNormalized Array:\n", A_normalized)
        print("\nStandardized Array:\n", A_standardized)
    
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()