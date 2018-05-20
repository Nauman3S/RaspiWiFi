import os

def install_prereqs():
	project_path = os.path.dirname(os.path.abspath(__file__))

	os.system('clear')
	os.system('apt update')
	os.system('clear')
	os.system('apt install python3 python3-rpi.gpio bundler nodejs libsqlite3-dev dnsmasq hostapd libxml2-dev libxslt-dev -y')
	os.system('clear')

def copy_configs():
	os.system('mkdir /usr/lib/raspi-wifi')
	os.system('cp -a libs/* /usr/lib/raspi-wifi/')
	os.system('sudo rm -f /etc/wpa_supplicant/wpa_supplicant.conf')
	os.system('rm -f ./tmp/*')
	os.system('sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.original')
	os.system('sudo cp -a /usr/lib/raspi-wifi/reset_device/static_files/dnsmasq.conf /etc/')
	os.system('sudo cp -a /usr/lib/raspi-wifi/reset_device/static_files/hostapd.conf /etc/hostapd/')
	os.system('sudo mv /etc/dhcpcd.conf /etc/dhcpcd.conf.original')
	os.system('sudo cp -a /usr/lib/raspi-wifi/reset_device/static_files/dhcpcd.conf /etc/')
	os.system('mkdir /etc/cron.raspiwifi')
	os.system('sudo cp -a /usr/lib/raspi-wifi/reset_device/static_files/aphost_bootstrapper /etc/cron.raspiwifi')
	os.system('echo "# RaspiWiFi Startup" >> /etc/crontab')
	os.system('echo "@reboot root run-parts /etc/cron.raspiwifi/" >> /etc/crontab')

def post_install_procs():
	os.system('gem install nokogiri --no-document -v 1.6.6.2 -- --use-system-libraries')
	os.system('clear')
	os.system('bundle install --gemfile=/usr/lib/raspi-wifi/configuration_app/Gemfile')
	os.system('clear')
