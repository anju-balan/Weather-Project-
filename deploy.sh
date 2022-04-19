rm /home/ubuntu/weather/Weather_Project/nohup.out
cd /home/ubuntu/weather/Weather_Project/
git pull
setsid nohup python3 /home/ubuntu/weather/Weather_Project/app.py && exit