# This post is a bit old, but I believe a better alternative exists: enter update-alternatives. The following will set your /usr/bin/python to default to 2.7 but have 3.6 available when you want:

- [ ] sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 20
- [ ] sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 10
# The highest priority here is used as the "automatic" choice for /usr/bin/python but you can easily switch by running 
- [ ] sudo update-alternatives --config python.
