import matplotlib
import matplotlib.pyplot as plt

# List of available backends
backends = matplotlib.rcsetup.all_backends

for backend in backends:
    print(f"Testing backend: {backend}")
    try:
        # Set the backend
        matplotlib.use(backend, force=True)

        # Create a simple plot
        plt.figure()
        plt.plot([0, 1], [0, 1])
        plt.title(f"Backend: {backend}")

        # Display the plot (non-interactive backends may not display)
        plt.show()

        print(f"Backend {backend} works successfully.\n")
    except Exception as e:
        print(f"Backend {backend} failed with error: {e}\n")
    finally:
        plt.close()  # Close the plot

