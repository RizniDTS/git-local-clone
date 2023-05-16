# Git Local Clone Environment Setup

1. Create a new file called `env.py` 

2. Inside `env.py`, define the following variables:
```python
source_dir = "/path/to/local/git/.git"
target_base_dir = "/path/to/target/dir"
```
Be sure to replace `/path/to/local/git/.git` with the actual path to the Git repository you want to clone, and `/path/to/target/dir` with the directory where you want to store the cloned repository.

3. Save the `env.py` file.

4. To use the environment variables in your main Python script, you can import them like this:
```python
from env import source_dir, target_base_dir
```
