# Installs nginx and configures it on a remote server

exec {'install':
  provider => shell,
  command  => "apt-get -y update ; apt-get install -y nginx ; sudo ufw allow 'Nginx HTTP' ; sudo mkdir -p /var/www/html/ ; sudo chmod -R 755 /var/www ; echo 'Hello World!' > /var/www/html/index.html ; echo \"Ceci n'est pas une page\" > /var/www/html/404.html ; echo \"server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\tserver_name _;\n\tlocation /redirect_me {\n\t\trewrite ^ https://github.com/IK-18 permanent;\n\t}\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n\terror_page 404 /404.html;\n\tlocation = /404.html {\n\t\tinternal;\n\t}\n}\" | sudo tee /etc/nginx/sites-available/default > /dev/null ; sed -i \"s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOSTNAME\";/\" /etc/nginx/nginx.conf ; service nginx start,",
}
