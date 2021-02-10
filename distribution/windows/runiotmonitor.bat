set /p mytextfile=< ip.txt
iotmonitor.exe runserver %mytextfile%:8000 --noreload