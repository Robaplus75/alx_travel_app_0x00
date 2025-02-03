import shutil

# List of common typos for the serializers.py file
typo_names = [
    "serailizers.py",
    "serilizers.py",
    "serializerss.py",
    "serilizerss.py",
    "serailizerss.py",
    "serailizer.py",
    "serilizer.py",
    "serailizer.py",
    "serailizerz.py",
    "serailizers.py"
]

# Original file name
original_file = "serializers.py"

# Create copies with typo names
for typo in typo_names:
    shutil.copy(original_file, typo)
    print(f"Created: {typo}")
