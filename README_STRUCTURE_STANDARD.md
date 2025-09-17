# LeetCode Repository README Structure Standard

This document describes the standardized format for README.md files in this LeetCode repository.

## Standard Format

All README.md files in problem directories should follow this format:

```html
<h2><a href="[LEETCODE_PROBLEM_URL]">[PROBLEM_TITLE]</a></h2> <img src='https://img.shields.io/badge/Difficulty-[DIFFICULTY]-[COLOR]' alt='Difficulty: [DIFFICULTY]' /><hr><div>[PROBLEM_DESCRIPTION_CONTENT]</div>
```

### Components

1. **Header (`<h2>`)**: Contains the problem title as a link to the LeetCode problem page
2. **Difficulty Badge**: Standardized image badge indicating problem difficulty
3. **Horizontal Rule (`<hr>`)**: Separates header from content
4. **Content (`<div>`)**: Contains the complete problem description

### Difficulty Badge Colors

- **Easy**: `brightgreen`
- **Medium**: `orange`
- **Hard**: `red`

### Examples

#### Easy Problem
```html
<h2><a href="https://leetcode.com/problems/two-sum">1. Two Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' /><hr><div>[problem content...]</div>
```

#### Medium Problem
```html
<h2><a href="https://leetcode.com/problems/add-two-numbers">2. Add Two Numbers</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' /><hr><div>[problem content...]</div>
```

#### Hard Problem
```html
<h2><a href="https://leetcode.com/problems/median-of-two-sorted-arrays">4. Median of Two Sorted Arrays</a></h2> <img src='https://img.shields.io/badge/Difficulty-Hard-red' alt='Difficulty: Hard' /><hr><div>[problem content...]</div>
```

## Benefits of Standardization

1. **Consistency**: All problem descriptions follow the same visual format
2. **Accessibility**: Clear difficulty indicators help users quickly identify problem complexity
3. **Navigation**: Direct links to original LeetCode problems
4. **Maintenance**: Easier to maintain and update repository structure
5. **Visual Appeal**: Consistent badges provide visual hierarchy

## Implementation

The standardization was implemented using an automated Python script that:
- Extracts problem title, difficulty, and URL from existing files
- Applies consistent formatting to all README files
- Preserves original problem content while standardizing structure
- Handles various input formats and edge cases

All 193 README files in the repository have been successfully standardized using this format.