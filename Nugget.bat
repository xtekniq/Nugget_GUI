@echo off
title Nugget (Leminlimez) Gui by everxqzw
cls
echo Press any button , if you have python already installed
pause
echo Checking Modules Installation..
cd data
pip install -r requirements.txt
ping localhost -n 2 >nul
cls
echo Loading..
ping localhost -n 5 >nul
start main_app.py
ping localhost -n 10000 >nul