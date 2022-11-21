from selenium import webdriver
import os
import pytest

def test_hellow_world(browser):
    browser.get("https://ya.ru/")
    assert "Яндекс" in browser.title


