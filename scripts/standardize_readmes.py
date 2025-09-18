#!/usr/bin/env python3
"""
Script to standardize README.md files in the LeetCode repository.
This script will normalize the structure and formatting of all problem descriptions.
"""

import os
import re
import glob
from pathlib import Path

def get_difficulty_badge(difficulty):
    """Return the standardized difficulty badge HTML."""
    color_map = {
        'Easy': 'brightgreen',
        'Medium': 'orange', 
        'Hard': 'red'
    }
    color = color_map.get(difficulty, 'brightgreen')
    return f"<img src='https://img.shields.io/badge/Difficulty-{difficulty}-{color}' alt='Difficulty: {difficulty}' />"

def extract_problem_info(content):
    """Extract problem information from README content."""
    # Extract title and problem number - get the first occurrence
    title_match = re.search(r'<h2><a href="[^"]*">([^<]+)</a></h2>', content)
    if not title_match:
        return None, None, None
    
    title = title_match.group(1)
    
    # Extract difficulty from h3 tag or img badge
    difficulty = None
    h3_match = re.search(r'<h3>(\w+)</h3>', content)
    if h3_match:
        difficulty = h3_match.group(1)
    else:
        badge_match = re.search(r"Difficulty-(\w+)-", content)
        if badge_match:
            difficulty = badge_match.group(1)
    
    # Extract problem URL - get the first occurrence
    url_match = re.search(r'<h2><a href="([^"]*)">', content)
    url = url_match.group(1) if url_match else ""
    
    return title, difficulty, url

def clean_content(content):
    """Clean and normalize the problem description content."""
    # Find the first <hr> tag and take everything after it
    hr_match = re.search(r'<hr>', content)
    if hr_match:
        cleaned = content[hr_match.end():]
    else:
        # If no <hr>, try to find the end of the first header section
        header_end = re.search(r'</h2>\s*(?:<h3>.*?</h3>)?\s*(?:<img[^>]*>)?\s*', content)
        if header_end:
            cleaned = content[header_end.end():]
        else:
            cleaned = content
    
    # Remove any embedded CSS styles
    cleaned = re.sub(r'<style[^>]*>.*?</style>', '', cleaned, flags=re.DOTALL)
    
    # Remove any additional header sections that might be duplicated
    cleaned = re.sub(r'<h2><a href="[^"]*">[^<]+</a></h2>\s*(?:<h3>[^<]*</h3>)?\s*(?:<img[^>]*>)?\s*(?:<hr>)?\s*(?:<div[^>]*>)?', '', cleaned, flags=re.DOTALL)
    
    # Clean up the start - remove any leading divs that wrap everything
    cleaned = cleaned.strip()
    if cleaned.startswith('<div'):
        # Find the end of the opening div tag
        div_end = cleaned.find('>')
        if div_end != -1:
            cleaned = cleaned[div_end + 1:]
    
    # Clean up the end - remove trailing </div> if it's the wrapper
    cleaned = cleaned.strip()
    if cleaned.endswith('</div>'):
        cleaned = cleaned[:-6]
    
    return cleaned.strip()

def standardize_readme(file_path):
    """Standardize a single README.md file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        original_content = f.read()
    
    # Extract problem information
    title, difficulty, url = extract_problem_info(original_content)
    
    if not title or not difficulty:
        print(f"Warning: Could not extract complete info from {file_path}")
        return False
    
    # Clean the content
    clean_desc = clean_content(original_content)
    
    # Create standardized header
    difficulty_badge = get_difficulty_badge(difficulty)
    header = f'<h2><a href="{url}">{title}</a></h2> {difficulty_badge}<hr>'
    
    # Combine header with cleaned content
    if clean_desc:
        standardized_content = f"{header}<div>{clean_desc}</div>"
    else:
        standardized_content = f"{header}<div></div>"
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(standardized_content)
    
    return True

def main():
    """Main function to process all README files."""
    repo_root = "/home/runner/work/LeetCode/LeetCode"
    
    # Find all README.md files in problem directories
    readme_files = glob.glob(os.path.join(repo_root, "*/README.md"))
    
    print(f"Found {len(readme_files)} README files to process...")
    
    success_count = 0
    failed_files = []
    
    for readme_file in sorted(readme_files):
        try:
            if standardize_readme(readme_file):
                success_count += 1
                print(f"✓ Standardized: {os.path.basename(os.path.dirname(readme_file))}")
            else:
                failed_files.append(readme_file)
                print(f"✗ Failed: {os.path.basename(os.path.dirname(readme_file))}")
        except Exception as e:
            failed_files.append(readme_file)
            print(f"✗ Error processing {readme_file}: {e}")
    
    print(f"\nProcessing complete!")
    print(f"Successfully standardized: {success_count} files")
    print(f"Failed to process: {len(failed_files)} files")
    
    if failed_files:
        print("\nFailed files:")
        for file in failed_files:
            print(f"  - {file}")

if __name__ == "__main__":
    main()