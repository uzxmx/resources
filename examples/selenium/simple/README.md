# Selenium example

To run the example, first you need to install python bindings for selenium by
`pip install -r requirements.txt`. Then use a local webdriver or remote one.

## Using local webdriver

Make sure you have `chromedriver` in your PATH. Otherwise, you need to download
it from [here](https://chromedriver.chromium.org/downloads).

## Using remote webdriver

To use the remote webdriver, you should have the selenium server running. You
can run the server by docker.

```
# See https://github.com/SeleniumHQ/docker-selenium#increasing-session-concurrency-per-container
docker run -e SE_NODE_MAX_SESSIONS=10 -e SE_NODE_OVERRIDE_MAX_SESSIONS=true -p 4444:4444 -p 7900:7900 --shm-size 2g selenium/standalone-chrome:107.0-20221104
```
