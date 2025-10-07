    {
      "functions": {
        "api/**/*.py": {
          "runtime": "python3.9" // or other supported Python version
        }
      },
      "rewrites": [
        {
          "source": "/api/(.*)",
          "destination": "/api" // Routes all /api requests to your Python function
        }
      ]
    }
