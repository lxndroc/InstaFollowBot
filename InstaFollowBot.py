"""
---------------------------------------------------
                    InstaFollowBot 2020
                    by @lxndroc-@aoctut
---------------------------------------------------
Finds & copies to clipboard all Instagram
a) followers,
b) following,
c) non-followers,
d) non-following,
e) new followers, &
f) unfollowers.
---------------------------------------------------
Requires Python 3, Chrome, the packages pyperclip & selenium, & chromedriver.
Inspired by @Harshp20/Instagram_Bot
---------------------------------------------------
Uses the MVC design pattern & automated browsing via Selenium
that sends & displays actions onto the web browser with appropriate delays.
---------------------------------------------------
Login process description ran when the program starts
1. Ask username & password from user
2. Visit Instagram website
3. Wait 1 sec
4. Enter the username & password
5. Wait 3 sec
6. Visit user profile
7. Wait 1 sec
---------------------------------------------------
Process description that collects followers ran when followers are requested.
1. Visit user profile
2. Wait 1 sec
3. Click on followers button
4. Wait 1 sec
5. Click on scroll bar repeatedly every 0.5 secs
6. Collect all followers' usernames.
---------------------------------------------------
The collected usernames can be copied to clipboard upon request.
There is a similar process to collect the following list.
The tool can also discover the non-followers & non-following
by taking the difference between the followers & following lists.
Finally, it can discover the new followers & unfollowers
by taking the difference between the current followers
& the followers previously saved in a specified file.
---------------------------------------------------
Example results showing the numbers & 1st 2 names of the profiles follow.
---
202 @aoctut Followers 18/05/2020-09:56
stone_sense
gemma_cormack
...
198 @aoctut Following 18/05/2020-09:56
jadahsellner
emilyryanlikes
...
23 @aoctut Non-Followers 18/05/2020-09:57
alexbeadon
azurewill
...
27 @aoctut Non-Following 18/05/2020-09:57
2youngtolose
_mastermarketers_
...
7 @aoctut New Followers 12/05/2020-11:52 - 18/05/2020-09:57
2youngtolose
beautypreneur.ie
...
6 @aoctut Unfollowers 12/05/2020-11:52 - 18/05/2020-09:57
brain_whisperer
drsukhi_mysticface
...
"""

from datetime import datetime
from getpass import getpass
from pyperclip import copy
from selenium import webdriver
from time import sleep

class Model:
    def __init__(self):
        # change this to your chromedriver path and filename
        self._driver_path = 'chromedriver'
        self._driver = webdriver.Chrome(self._driver_path)
        self._insta_url = 'https://www.instagram.com/'
        self._followers_filename = ''
        self._username = ''
        self._password = ''
        self._sleep_time = 1
        self._followers = []
        self._saved_followers = []
        self.saved_time = ''
        self._following = []
        self._non_followers = []
        self._non_following = []
        self._new_followers = []
        self._unfollowers = []

    @property
    def driver(self):
        return self._driver

    @property
    def insta_url(self):
        return self._insta_url

    @property
    def followers_filename(self):
        return self._followers_filename

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def sleep_time(self):
        return self._sleep_time

    @property
    def followers(self):
        return self._followers

    @property
    def saved_followers(self):
        return self._saved_followers

    @property
    def saved_time(self):
        return self._saved_time

    @property
    def following(self):
        return self._following

    @property
    def non_followers(self):
        return self._non_followers

    @property
    def non_following(self):
        return self._non_following

    @property
    def new_followers(self):
        return self._new_followers

    @property
    def unfollowers(self):
        return self._unfollowers

    @username.setter
    def username(self, username):
        self._username = username

    @password.setter
    def password(self, password):
        self._password = password

    @followers.setter
    def followers(self, followers):
        self._followers = followers

    @saved_followers.setter
    def saved_followers(self, saved_followers):
        self._saved_followers = saved_followers

    @saved_time.setter
    def saved_time(self, saved_time):
        self._saved_time = saved_time

    @following.setter
    def following(self, following):
        self._following = following

    @non_followers.setter
    def non_followers(self, non_followers):
        self._non_followers = non_followers

    @non_following.setter
    def non_following(self, non_following):
        self._non_following = non_following

    @new_followers.setter
    def new_followers(self, new_followers):
        self._new_followers = new_followers

    @unfollowers.setter
    def unfollowers(self, unfollowers):
        self._unfollowers = unfollowers

class View:
    def __init__(self):
        pass

    def read_username(self):
        return input("\nUsername: ")

    def read_password(self):
        return getpass()

    def read_menu_choice(self):
        return input("""
1. Download Followers From Instagram
    Rerun if fewer followers returned due to download delay
2. Download Following From Instagram
    Rerun if fewer following returned due to download delay
3. Copy Followers To Clipboard
    Runs 1. if not previously done
4. Copy Following From Instagram To Clipboard
    Runs 2. if not previously done
5. Copy Non-Followers To Clipboard
    Runs 1. & 2. if not previously done
6. Copy Non-Following To Clipboard
    Runs 1. & 2. if not previously done
7. Copy New Followers To Clipboard
    Runs 1. & reads followers from file if not previously done
8. Copy Unfollowers To Clipboard
    Runs 1. & reads followers from file if not previously done
0. Exit
Enter option: """)

    def read_filename(self):
        return input("Followers filename: ")

    def load_list_from_file(self, filename):
        with open(filename) as followers_file:
            # read time from header line
            date = followers_file.readline().split()[-1]
            return date, [line.strip() for line in followers_file]

    def copy_list_to_clipboard(self, title, in_list):
        title = f'{len(in_list)} {title}'
        to_print = f'{title} {datetime.now().strftime("%d/%m/%Y-%H:%M")}\n'
        for item in in_list:
            to_print += f'{item}\n'
        print(f'{title} {datetime.now().strftime("%d/%m/%Y-%H:%M")} \
were copied from memory to clipboard')
        copy(to_print)

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.login()
        print(f'@{self.model.username} logged in {datetime.now().strftime("%d/%m/%Y-%H:%M")}')

    def read_user_credentials(self):
        self.model.username = self.view.read_username()
        self.model.password = self.view.read_password()

    def login(self):
        if not self.model.username or not self.model.password:
            self.read_user_credentials()
        self.model.driver.get(self.model.insta_url)
        sleep(self.model.sleep_time)
        self.model.driver.find_element_by_name('username')\
            .send_keys(self.model.username)
        self.model.driver.find_element_by_name('password')\
            .send_keys(self.model.password)
        # Log In button
        self.model.driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF')\
            .click()
        sleep(self.model.sleep_time * 3)
        self.go_to_my_profile()
     
    def go_to_my_profile(self):
        self.model.driver.get(self.model.insta_url + self.model.username)
        sleep(self.model.sleep_time)

    def scroll_down_followers(self, scroll_box):
        previous_height = -1
        while True:
            sleep(self.model.sleep_time / 2)
            current_height = self.model.driver.execute_script('''
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;''', scroll_box)
            if previous_height == current_height:
                break
            previous_height = current_height

    def download_followers_from_instagram(self, is_followers = True):
        self.go_to_my_profile()
        # followers or following text
        if is_followers:
            self.model.driver.find_element_by_xpath\
                (f'//a[@href= "/{self.model.username}/followers/"]').click()
        else:
            self.model.driver.find_element_by_xpath\
                (f'//a[@href= "/{self.model.username}/following/"]').click()
        sleep(self.model.sleep_time)
        # followers or following scroll bar
        scroll_box = self.model.driver.find_element_by_css_selector('.isgrP')
        self.scroll_down_followers(scroll_box)
        follower_links = scroll_box.find_elements_by_tag_name('a')
        if is_followers:
            self.model.followers =\
                [name.text for name in follower_links if name.text != '']
            print(f'{len(self.model.followers)} @{self.model.username} \
followers were downloaded from Instagram to memory \
{datetime.now().strftime("%d/%m/%Y-%H:%M")}')
        else:
            self.model.following\
                = [name.text for name in follower_links if name.text != '']
            print(f'{len(self.model.following)} @{self.model.username} \
following were downloaded from Instagram to memory \
{datetime.now().strftime("%d/%m/%Y-%H:%M")}')

    def load_followers_from_file(self):
        if not self.model.followers_filename:
            self.model.followers_filename = self.view.read_filename()
        self.model.saved_time, self.model.saved_followers\
            = self.view.load_list_from_file(self.model.followers_filename)
        print(f'{len(self.model.saved_followers)} @{self.model.username} \
saved followers were loaded from {self.model.followers_filename} \
to memory {datetime.now().strftime("%d/%m/%Y-%H:%M")}')

    def copy_followers_to_clipboard(self, is_follower = True):
        if is_follower:
            if not self.model.followers:
                self.download_followers_from_instagram()                
            self.view.copy_list_to_clipboard(f'@{self.model.username} \
Followers', self.model.followers)
        else:
            if not self.model.following:
                self.download_following_from_instagram()                
            self.view.copy_list_to_clipboard(f'@{self.model.username} \
Following', self.model.following)

    def download_following_from_instagram(self):
        self.download_followers_from_instagram(False)

    def copy_following_to_clipboard(self):
        self.copy_followers_to_clipboard(False)
        
    def discover_non_followers(self, is_non_followers = True):
        if not self.model.followers:
            self.download_followers_from_instagram()
        if not self.model.following:
            self.download_following_from_instagram()

        if is_non_followers:
            self.model.non_followers = sorted(list(set(self.model.following)
                - set(self.model.followers)))
        else:
            self.model.non_following = sorted(list(set(self.model.followers)
                - set(self.model.following)))

    def copy_non_followers_to_clipboard(self, is_non_followers = True):
        if is_non_followers:
            if not self.model.non_followers:
                self.discover_non_followers()
            self.view.copy_list_to_clipboard(f'@{self.model.username} \
Non-Followers', self.model.non_followers)
        else:
            if not self.model.non_following:
                self.discover_non_following()
            self.view.copy_list_to_clipboard(f'@{self.model.username} \
Non-Following', self.model.non_following)

    def discover_non_following(self):
        self.discover_non_followers(False)

    def copy_non_following_to_clipboard(self):
        self.copy_non_followers_to_clipboard(False)

    def discover_new_followers(self, is_new_followers = True):
        if not self.model.followers:
            self.download_followers_from_instagram()
        if not self.model.saved_followers:
            self.load_followers_from_file()
        if is_new_followers:
            self.model.new_followers = sorted(list
                (set(self.model.followers) - set(self.model.saved_followers)))
        else:
            self.model.unfollowers = sorted(list
                (set(self.model.saved_followers) - set(self.model.followers)))

    def copy_new_followers_to_clipboard(self, is_new_followers = True):
        if is_new_followers:
            if not self.model.new_followers:
                self.discover_new_followers()
            self.view.copy_list_to_clipboard(f'@{self.model.username} \
New Followers {self.model.saved_time} -',
                self.model.new_followers)
        else:
            if not self.model.unfollowers:
                self.discover_unfollowers()
            self.view.copy_list_to_clipboard(f'@{self.model.username} \
Unfollowers {self.model.saved_time} -',
                self.model.unfollowers)

    def discover_unfollowers(self):
        self.discover_new_followers(False)

    def copy_unfollowers_to_clipboard(self):
        self.copy_new_followers_to_clipboard(False)

    def run_menu(self):
        while True:
            choice = self.view.read_menu_choice()
            print()
            # 1. Download Followers From Instagram
            if choice == '1':
                self.download_followers_from_instagram()
            # 2. Download Following From Instagram
            elif choice == '2':
                self.download_following_from_instagram()
            # 3. Copy Followers To Clipboard
            elif choice == '3':
                self.copy_followers_to_clipboard()
            # 4. Copy Following To Clipboard
            elif choice == '4':
                self.copy_following_to_clipboard()
            # 5. Copy Non-Followers To Clipboard
            elif choice == '5':
                self.copy_non_followers_to_clipboard()
            # 6. Copy Non-Following To Clipboard
            elif choice == '6':
                self.copy_non_following_to_clipboard()
            # 7. Copy New Followers To Clipboard
            elif choice == '7':
                self.copy_new_followers_to_clipboard()
            # 8. Copy Unfollowers To Clipboard
            elif choice == '8':
                self.copy_unfollowers_to_clipboard()
            # 0. Exit
            elif choice == '0':
                print('Program exited')
                break
            # Invalid option
            else:
                print('Invalid option, retry')
                continue

class InstaFollowBot:
  def __init__(self):
    Controller().run_menu()

InstaFollowBot()
