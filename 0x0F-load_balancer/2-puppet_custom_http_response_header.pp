# creating a custom HTTP header response whit ppupet
exec {'http_header':
  provider => shell,
  command  => 'sudo apt update -y ;\
               sudo apt-get install nginx -y ;\
               sudo chown -R ubuntu /var/www/ ;\
               echo "Hello World" > /var/www/html/index.nginx-debian.html ;\
               sudo service nginx start ;\
               sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=NdYWuo9OFAw permanent;/" /etc/nginx/sites-available/default ;\
               sudo sed -i "s/^server\s{/server {\n\terror_page 404 \/error-404.html;/1" /etc/nginx/sites-available/default ;\
               sudo sed -i "s/^server\s{/server {\n\tadd_header X-Served-By $HOSTNAME;/1" /etc/nginx/sites-available/default ;\
               sudo service nginx restart',
}
