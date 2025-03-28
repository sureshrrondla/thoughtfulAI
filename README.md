# Package Sorting System

This system classifies packages into three different categories based on their dimensions and mass. The goal is to categorize packages as either **STANDARD**, **SPECIAL**, or **REJECTED** for further processing.

## Rules

- **Bulky Package**: 
  - A package is considered bulky if:
    - Its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³.
    - Or, if any of its dimensions (Width, Height, or Length) is greater than or equal to 150 cm.

- **Heavy Package**:
  - A package is considered heavy if its mass is greater than or equal to 20 kg.

## Stacks

The packages are sorted into the following categories:

- **STANDARD**: 
  - Standard packages that are neither bulky nor heavy.

- **SPECIAL**: 
  - Special packages that are either bulky or heavy.

- **REJECTED**: 
  - Packages that are both bulky and heavy are rejected.

## Function Implementation

### `sort(width, height, length, mass)`

This function sorts a package into one of the three categories based on its dimensions and mass.

#### Parameters:
- `width` (cm) - The width of the package.
- `height` (cm) - The height of the package.
- `length` (cm) - The length of the package.
- `mass` (kg) - The mass of the package.

#### Returns:
- A string: `"STANDARD"`, `"SPECIAL"`, or `"REJECTED"` depending on the package's characteristics.

### Example Usage

```python
# Example 1: Standard package
print(sort(50, 50, 50, 5))  # Output: "STANDARD"

# Example 2: Heavy package
print(sort(50, 50, 50, 25))  # Output: "SPECIAL"

# Example 3: Bulky package
print(sort(200, 50, 50, 10))  # Output: "SPECIAL"

# Example 4: Both bulky and heavy package
print(sort(200, 200, 200, 25))  # Output: "REJECTED"
