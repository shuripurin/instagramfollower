# Instagram Follower Analysis

A simple Python script to analyze your Instagram followers and following data to find:
- **People you follow who DON'T follow you back**
- **People who follow you that you DON'T follow back**

## How to Use

### 1. Download Your Instagram Data

1. Go to your Instagram settings
2. Navigate to **Account Center** → **Your Information and Permissions** → **Download Your Information**
3. Select **Followers and Following** as the data to download
4. Choose JSON format and request your download
5. Wait for Instagram to prepare your files (typically a few hours to a day)
6. Download the file when ready

### 2. Extract the Required Files

From your downloaded Instagram data, extract these JSON files to the project folder:
- `followers_1.json` - Your followers list
- `following.json` - Your following list

You may also have these files in a `connections/followers_and_following/` folder structure. If so, copy them to the root directory of this project.

### 3. Run the Script

```bash
python instagramcalc.py
```

### 4. View Results

The script will:
- Print a summary to the terminal showing:
  - Total number of followers
  - Total number of people you follow
  - List of people you follow who don't follow back
  - List of followers you don't follow back
  
- Create a `not_following_back.txt` file with the unfollowers saved for reference

## File Structure

```
.
├── instagramcalc.py           # Main analysis script
├── followers_1.json           # Your followers data (not tracked in Git)
├── following.json             # Your following data (not tracked in Git)
└── not_following_back.txt     # Output file with results (not tracked in Git)
```

## Requirements

- Python 3.x
- No external dependencies (uses only the standard library)

## Privacy & Security

⚠️ **Important:** Your Instagram JSON files contain personal data. The `.gitignore` file in this repo ensures they will **never** be uploaded to GitHub. Only the Python script is shared.

## License

Feel free to use and modify this script for your personal use.
