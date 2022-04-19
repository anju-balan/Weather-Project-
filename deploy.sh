rm /home/ubuntu/weather/Weather-Project-/nohup.out
cd /home/ubuntu/weather/Weather-Project-/
git pull
setsid nohup python3 /home/ubuntu/weather/Weather-Project-/app.py && exit