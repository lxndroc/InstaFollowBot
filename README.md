<h1 align="center">+ InstaFollowBot +</h1>
<p align="center">
  <h3 align='center'>Find & copy to clipboard all Instagram Followers - Following - Non-Followers - Non-Following - New Followers - Unfollowers
  </h3>
</p>
  <p align="center">⭐️ & 🔱</p>
  <p align="center">
    <a href="https://github.com/lxndroc">
      <img src="https://img.shields.io/badge/Coded%20By-@lxndroc--@aoctut-yellow" />
    </a>
    <img src="https://img.shields.io/badge/Version-1.0-yellow" />
    <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
      <img src="https://img.shields.io/badge/Licence-CC%20BY--NC--SA%204.0-yellow" />
    </a>
    <a href="https://instagram.com/aoctut/">
      <img src="https://img.shields.io/badge/Contact-@aoctut-yellow" />
    </a>
  </p>
  <p align="center">
    <a href="https://python.org/">
      <img src="https://img.shields.io/badge/Built%20with-Python3-yellow" />
    </a>
    <a href="https://selenium.dev/selenium/docs/api/py/">
      <img src="https://img.shields.io/badge/Built%20with-Selenium%20WebDriver-yellow" />
    </a>
    <a href="https://google.com/chrome/">
      <img src="https://img.shields.io/badge/Powered%20by-Google%20Chrome-yellow" />
    </a>
  </p>

## Contents
* Purpose
* Method
* Installation
* Execution
* Help
* Contribution

## Purpose
* The bot collects the followers & following list from an Instagram profile.
* The collected usernames can be copied to clipboard upon request.
* The bot can also discover the non-followers & non-following by taking the difference between the followers & following lists.
* Finally, it can discover the new followers & unfollowers by taking the difference between the current followers & the followers previously saved in a specified file.

## Method
* The bot code implements the MVC design pattern & automated browsing via the Selenium WebDriver that sends & displays actions onto the Chrome web browser with appropriate delays.

## Installation
### 1. `Python 3.6` & above
* [Download](https://python.org/downloads/) the installer.
* Run & follow the steps of the installer.
* This is the used programming language.
### 2. `Selenium WebDriver for Chrome`
* [Download](http://chromedriver.chromium.org/downloads) the compressed `chromedriver` installer corresponding to your Chrome version & OS version.
* The used Chrome version is on the 1st output line when requesting `chrome://version` in Chrome's search bar.
* The filename to download is `chromedriver_win32.zip` for Windows & `chromedriver_mac64.zip` for Mac.
* Unzip the compressed installer.
* Run & follow the steps of the installer.
* This is the automatic driver for Chrome.
### 3. `selenium` package
* Install with `pip install selenium` from the terminal.
* These are the Python bindings to the `Selenium Webdriver`.
### 4. `pyperclip` package
* Install with `pip install pyperclip` from the terminal.
* This is the connection to the clipboard of the OS.
### 5. `Google Chrome`
* [Download](https://google.com/chrome/) the installer.
* Run & follow the steps of the installer.
* This is the web browser Chrome.
### 6. `InstaBotFollow`
* [Download](https://github.com/lxndroc/InstaBotFollow/InstaBotFollow.py) the Python source.
* Set the value of `self._driver_path` on line 82 to the path of the chromedriver executable on your operating system (OS), e.g. `self._driver_path = 'D:/utils/net/chromedriver.exe'` or `self._driver_path = '/users/username/utils/net/chromedriver'`. 
* This is the source code of the bot.

## Execution
* Run `InstaBotFollow` with `python InstaBotFollow.py` from the terminal.
* Just `InstaBotFollow.py` or double clicking may also work.

### Login To Instagram
  * Happens as soon as the program runs.
  1. The bot loads Chrome.
  2. It asks the user for their Instagram username and password.
    * The password characters typed remain invisible for a safer entry.
  3. It visits the Instagram website.
  4. It waits 1 sec for the browser to load.
  5. It logins automatically to the profile using the provided details.
  6. It waits 3 sec.
  7. It opens the profile page.
  8. It waits 1 sec.

### Menu Options
#### 1. Download Followers From Instagram
  * Scrolls over the followers on the logged in Instagram profile.
  * Copies the profile names & total number of followers alongside the current time to the program memory.
  * To be rerun if fewer followers than displayed are returned due to delay in downloading.
  * Process description to collect followers
    1. Visit user profile
    2. Wait 1 sec
    3. Click on followers button
    4. Wait 1 sec
    5. Click on scroll bar repeatedly every 0.5 secs
    6. Collect all followers' usernames.
#### 2. Download Following From Instagram
  * Scrolls over the following on the logged in Instagram profile.
  * Copies the profile names & total number of following alongside the current time to the program memory.
  * To be rerun if fewer following than displayed are returned due to delay in downloading.
#### 3. Copy Followers To Clipboard
  * Copies the downloaded profile names & total number of followers from the program memory alongside the current time to the OS clipboard.
  * The profile names appear in reverse chronological order of following.
  * The data can be easily copied to a file with Ctrl-V on Windows or Cmd-V on Mac.
  * Runs 1. if it was not previously done.
#### 4. Copy Following From Instagram To Clipboard
  * Copies the downloaded profile names & total number of following from the program memory alongside the current time to the OS clipboard.
  * The profile names appear in reverse chronological order of following.
  * Runs 2. if it was not previously done.
#### 5. Copy Non-Followers To Clipboard
  * Discovers the profile names & total number of non-followers by subtracting the followers from the following.
  * Copies the discovered profile names & total number of non-followers alongside the current time to the OS clipboard.
  * The profile names appear in alphabetical order.
  * Runs 1. & 2. if it was not previously done.
#### 6. Copy Non-Following To Clipboard
  * Discovers the profile names & total number of non-following by subtracting the following from the followers.
  * Copies the discovered profile names & total number of non-following alongside the current time to the OS clipboard.
  * The profile names appear in alphabetical order.
  * Runs 1. & 2. if it was not previously done.
#### 7. Copy New Followers To Clipboard
  * Discovers the profile names & total number of new followers by subtracting the followers previously saved in a file from the current followers.
  * Copies the discovered profile names & total number of new followers alongside the previously saved & the current time to the OS clipboard.
  * The profile names appear in alphabetical order.
  * Runs 1. if it was not previously done.
  * Asks the user for the filename containing previously saved followers if it was not previously done.
  * Reads followers from the specified file if it was not previously done.
#### 8. Copy Unfollowers To Clipboard
  * Discovers the profile names & total number of unfollowers by subtracting the current followers from the followers previously saved in a file.
  * Copies the discovered profile names & total number of unfollowers alongside the previously saved & the current time to the OS clipboard.
  * The profile names appear in alphabetical order.
  * Runs 1. if it was not previously done.
  * Asks the user for the filename containing previously saved followers if it was not previously done.
  * Reads followers from the specified file if it was not previously done.
#### 0. Exit
  * Exits the program.

### Sample Output Copied From Clipboard
Only the 1st 2 Instagram profile names are displayed for brevity.

#### Menu Option 3.
```
202 @aoctut Followers 18/05/2020-09:56
stone_sense
gemma_cormack
...
```
#### Menu Option 4.
```
198 @aoctut Following 18/05/2020-09:56
jadahsellner
emilyryanlikes
...
```
#### Menu Option 5.
```
23 @aoctut Non-Followers 18/05/2020-09:57
alexbeadon
azurewill
...
```
#### Menu Option 6.
```
27 @aoctut Non-Following 18/05/2020-09:57
2youngtolose
_mastermarketers_
...
```
#### Menu Option 7.
```
7 @aoctut New Followers 12/05/2020-11:52 - 18/05/2020-09:57
2youngtolose
beautypreneur.ie
...
```
#### Menu Option 8.
```
6 @aoctut Unfollowers 12/05/2020-11:52 - 18/05/2020-09:57
brain_whisperer
drsukhi_mysticface
...
```

## Licence
InstaFollowBot is released with the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) licence](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Help
To ask for help with running the bot, you can contact us on [Instagram](https://instagram.com/aoctut/).

## Contribution
  * To offer us suggestions or financial support to improve the bot, you can contact us on [Instagram](https://instagram.com/aoctut/).
  * To contribute to this project, you can fork this repository, make improvements, and submit them via a pull request.

#### + THANK YOU FOR BEING HERE 🙏+
